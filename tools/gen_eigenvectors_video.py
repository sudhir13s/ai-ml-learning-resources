# /// script
# requires-python = ">=3.11"
# dependencies = ["manim>=0.19", "numpy>=1.26"]
# ///
"""Render the eigenvectors video for the Eigenvalues & Eigenvectors page with Manim.

The symmetric matrix A = [[2, 1], [1, 2]] transforms the plane. Two ordinary vectors,
(1, 0) and (-1, 2), are turned off the line they started on; the two eigenvectors,
(1, 1) and (-1, 1), stay on their own lines and are only scaled, by the eigenvalues
3 and 1. Every number on screen and in the captions comes from numpy: the eigenpairs
from numpy.linalg.eigh, the landing points from A @ v, the turn angles from atan2.

Outputs, written to the page's images/ folder:
  eigenvectors_stay_on_their_line.mp4         H.264, 1280x720, muted, faststart
  eigenvectors_stay_on_their_line_poster.png  the still shown before playback
  eigenvectors_stay_on_their_line.en.vtt      WebVTT captions, timed to the scene's beats

Run from the repository root (needs ffmpeg on PATH; no LaTeX: every label is Text):
  uv run tools/gen_eigenvectors_video.py
"""

from __future__ import annotations

import math
import subprocess
import tempfile
from dataclasses import dataclass
from pathlib import Path

import numpy as np
from manim import (
    DOWN,
    LEFT,
    RIGHT,
    UP,
    Arrow,
    Create,
    DashedLine,
    FadeIn,
    Indicate,
    Line,
    NumberPlane,
    Rectangle,
    Scene,
    SurroundingRectangle,
    Text,
    ValueTracker,
    VGroup,
    Write,
    always_redraw,
    tempconfig,
)
from manim.animation.transform import ApplyMatrix

# ── The mathematics ─────────────────────────────────────────────────────────
MATRIX = np.array([[2.0, 1.0], [1.0, 2.0]])
ORDINARY_VECTORS = (np.array([1.0, 0.0]), np.array([-1.0, 2.0]))
NUMERIC_TOLERANCE = 1e-9

# ── The frame ───────────────────────────────────────────────────────────────
PIXEL_WIDTH = 1280
PIXEL_HEIGHT = 720
FPS = 30
FRAME_HEIGHT_UNITS = 8.0                 # Manim's default frame: 14.22 x 8 scene units
CAPTION_BAND = 0.17                      # bottom share of the frame left empty for the caption box
CAPTION_BAND_TOP = -FRAME_HEIGHT_UNITS / 2 + CAPTION_BAND * FRAME_HEIGHT_UNITS
GRID_UNIT = 0.55                         # scene units per grid unit
GRID_EXTENT = 9                          # grid spans -9..9 so its image still covers the viewport
VIEWPORT_CENTER = np.array([-3.35, 0.2, 0.0])
VIEWPORT_WIDTH = 6.6
VIEWPORT_HEIGHT = 5.3
PANEL_LEFT = 0.35                        # left edge of the text panel, in scene units
MASK_OVERLAP = 0.05                      # how far neighbouring mask panels overlap
FONT = "Helvetica Neue"                  # Pango falls back to the system sans if it is missing

# ── The beats (seconds); the captions use the same table ────────────────────
INTRO_SECONDS = 6.0
TRANSFORM_SECONDS = 3.5
TRANSFORM_BEAT_SECONDS = 5.0
ORDINARY_BEAT_SECONDS = 7.0
EIGEN_BEAT_SECONDS = 9.0
TAKEAWAY_BEAT_SECONDS = 8.0

# ── Colors: a neutral light canvas that reads the same on both page themes ──
CANVAS = "#F8FAFC"
INK = "#1E293B"
MUTED_INK = "#475569"
STATIC_GRID = "#E2E8F0"
MOVING_GRID = "#93B4D6"
MOVING_AXES = "#475569"
VIEWPORT_BORDER = "#94A3B8"
ORDINARY_COLORS = ("#B4405A", "#A16207")
EIGEN_COLORS = ("#2F6EA8", "#15803D")

OUTPUT_DIR = (Path(__file__).resolve().parent.parent / "foundations" / "mathematical-foundations"
              / "eigenvalues-and-eigenvectors" / "images")
BASE_NAME = "eigenvectors_stay_on_their_line"
VIDEO_NAME = f"{BASE_NAME}.mp4"
POSTER_NAME = f"{BASE_NAME}_poster.png"
CAPTIONS_NAME = f"{BASE_NAME}.en.vtt"
ENCODE_ARGS = ["-c:v", "libx264", "-pix_fmt", "yuv420p", "-crf", "28", "-preset", "slow",
               "-movflags", "+faststart", "-an"]


@dataclass(frozen=True)
class TrackedVector:
    """One vector the video follows: where it starts, where A sends it, and what that means."""

    start: np.ndarray
    color: str
    eigenvalue: float | None = None

    @property
    def end(self) -> np.ndarray:
        return MATRIX @ self.start

    @property
    def is_eigenvector(self) -> bool:
        return self.eigenvalue is not None

    def turn_degrees(self) -> float:
        """Angle between v and A v, in degrees: zero for an eigenvector with a positive eigenvalue."""
        before = math.atan2(self.start[1], self.start[0])
        after = math.atan2(self.end[1], self.end[0])
        turn = abs(math.degrees(after - before)) % 360
        return min(turn, 360 - turn)  # atan2 wraps at ±180°, so take the shorter way round


def number(value: float) -> str:
    """Format a computed value the way it reads on a whiteboard: 3, not 3.0000; minus as U+2212."""
    rounded = round(value)
    text = f"{rounded:d}" if abs(value - rounded) < NUMERIC_TOLERANCE else f"{value:.2f}"
    return text.replace("-", "−")


def pair(vector: np.ndarray) -> str:
    return f"({number(vector[0])}, {number(vector[1])})"


def eigen_directions() -> list[tuple[float, np.ndarray]]:
    """Eigenpairs from numpy, each direction rescaled to small integers and pointing upward."""
    eigenvalues, eigenvectors = np.linalg.eigh(MATRIX)
    pairs = []
    for eigenvalue, column in sorted(zip(eigenvalues, eigenvectors.T), key=lambda item: -item[0]):
        direction = column / np.min(np.abs(column[np.abs(column) > NUMERIC_TOLERANCE]))
        direction = direction if direction[1] > 0 else -direction
        if not np.allclose(MATRIX @ direction, eigenvalue * direction, atol=NUMERIC_TOLERANCE):
            raise ValueError(f"numpy eigenpair failed A v = λ v for λ = {eigenvalue}")
        pairs.append((float(eigenvalue), direction))
    return pairs


def tracked_vectors() -> tuple[list[TrackedVector], list[TrackedVector]]:
    ordinary = [TrackedVector(v, color) for v, color in zip(ORDINARY_VECTORS, ORDINARY_COLORS)]
    for vector in ordinary:
        if abs(np.linalg.det(np.column_stack([vector.start, vector.end]))) < NUMERIC_TOLERANCE:
            raise ValueError(f"{pair(vector.start)} is an eigenvector; pick an ordinary vector")
    eigen = [TrackedVector(direction, color, eigenvalue)
             for (eigenvalue, direction), color in zip(eigen_directions(), EIGEN_COLORS)]
    return ordinary, eigen


def matrix_text() -> str:
    rows = ", ".join(f"[{number(row[0])}, {number(row[1])}]" for row in MATRIX)
    return f"[{rows}]"


def turn_phrase(vectors: list[TrackedVector]) -> str:
    """'each turns 26.6°' when the computed angles agree to one decimal, else both angles."""
    angles = [f"{vector.turn_degrees():.1f}°" for vector in vectors]
    return f"each turns {angles[0]}" if len(set(angles)) == 1 else f"they turn {' and '.join(angles)}"


def caption_cues(ordinary: list[TrackedVector], eigen: list[TrackedVector]) -> list[tuple[float, float, str]]:
    """Caption text per beat, timed to the scene; every number is computed above.

    The page's transcript repeats these sentences word for word (main() prints them).
    """
    first, second = ordinary
    big, small = eigen
    transform_end = INTRO_SECONDS + TRANSFORM_BEAT_SECONDS
    ordinary_end = transform_end + ORDINARY_BEAT_SECONDS
    eigen_mid = ordinary_end + EIGEN_BEAT_SECONDS / 2
    eigen_end = ordinary_end + EIGEN_BEAT_SECONDS
    takeaway_mid = eigen_end + TAKEAWAY_BEAT_SECONDS / 2
    end = eigen_end + TAKEAWAY_BEAT_SECONDS
    return [
        (0.0, INTRO_SECONDS / 2,
         f"The matrix A = {matrix_text()} is about to transform the whole plane."),
        (INTRO_SECONDS / 2, INTRO_SECONDS,
         "Four vectors start on their own dashed lines: two ordinary ones and two special ones."),
        (INTRO_SECONDS, transform_end,
         "A moves every grid line. Watch where each vector lands."),
        (transform_end, ordinary_end,
         (f"{pair(first.start)} lands on {pair(first.end)} and {pair(second.start)} lands on "
          f"{pair(second.end)}: {turn_phrase(ordinary)}, off its own line.")),
        (ordinary_end, eigen_mid,
         (f"{pair(big.start)} lands on {pair(big.end)}, which is {number(big.eigenvalue)} × "
          f"{pair(big.start)}: it stays on its line, stretched by λ = {number(big.eigenvalue)}.")),
        (eigen_mid, eigen_end,
         (f"{pair(small.start)} lands on {pair(small.end)}, which is {number(small.eigenvalue)} × "
          f"{pair(small.start)}: same line, eigenvalue λ = {number(small.eigenvalue)}.")),
        (eigen_end, takeaway_mid,
         "Eigenvectors are the directions a matrix only scales, never turns. The eigenvalue is the scale."),
        (takeaway_mid, end,
         "Because A is symmetric, its two eigenvector lines are perpendicular: the fact PCA relies on."),
    ]


def vtt_time(seconds: float) -> str:
    minutes, rest = divmod(seconds, 60)
    return f"00:{int(minutes):02d}:{rest:06.3f}"


def write_captions(cues: list[tuple[float, float, str]]) -> None:
    lines = ["WEBVTT", ""]
    for index, (start, stop, text) in enumerate(cues, start=1):
        lines += [str(index), f"{vtt_time(start)} --> {vtt_time(stop)}", text, ""]
    (OUTPUT_DIR / CAPTIONS_NAME).write_text("\n".join(lines), encoding="utf-8")


def to_scene(grid_point: np.ndarray) -> np.ndarray:
    return VIEWPORT_CENTER + GRID_UNIT * np.array([grid_point[0], grid_point[1], 0.0])


def label(text: str, color: str = INK, size: int = 24) -> Text:
    return Text(text, color=color, font_size=size, font=FONT).set_z_index(10)


def masks() -> VGroup:
    """Canvas-colored panels around the viewport: they clip the grid without clipping support."""
    half_w, half_h = VIEWPORT_WIDTH / 2, VIEWPORT_HEIGHT / 2
    left, right = VIEWPORT_CENTER[0] - half_w, VIEWPORT_CENTER[0] + half_w
    bottom, top = VIEWPORT_CENTER[1] - half_h, VIEWPORT_CENTER[1] + half_h
    big = 40.0

    def panel(x_min: float, x_max: float, y_min: float, y_max: float) -> Rectangle:
        rectangle = Rectangle(width=x_max - x_min, height=y_max - y_min, stroke_width=0,
                              fill_color=CANVAS, fill_opacity=1.0)
        return rectangle.move_to([(x_min + x_max) / 2, (y_min + y_max) / 2, 0]).set_z_index(5)

    # Top and bottom panels run the full width and the side panels overlap them, so no
    # anti-aliased seam between two panels lets a grid line show through.
    overlap = MASK_OVERLAP
    border = Rectangle(width=VIEWPORT_WIDTH, height=VIEWPORT_HEIGHT, color=VIEWPORT_BORDER,
                       stroke_width=1.5).move_to(VIEWPORT_CENTER).set_z_index(6)
    return VGroup(panel(-big, big, top, big), panel(-big, big, -big, bottom),
                  panel(-big, left, bottom - overlap, top + overlap),
                  panel(right, big, bottom - overlap, top + overlap), border)


def grid(color: str, axis_color: str, width: float) -> NumberPlane:
    side = 2 * GRID_EXTENT * GRID_UNIT
    plane = NumberPlane(x_range=(-GRID_EXTENT, GRID_EXTENT, 1), y_range=(-GRID_EXTENT, GRID_EXTENT, 1),
                        x_length=side, y_length=side,
                        background_line_style={"stroke_color": color, "stroke_width": width},
                        axis_config={"stroke_color": axis_color, "stroke_width": width + 0.5})
    return plane.move_to(VIEWPORT_CENTER)


def span_line(vector: TrackedVector) -> DashedLine:
    direction = vector.start / np.linalg.norm(vector.start) * GRID_EXTENT * 2
    return DashedLine(to_scene(-direction), to_scene(direction), color=vector.color,
                      stroke_width=2.5, stroke_opacity=0.55, dash_length=0.12)


def matrix_mobject() -> VGroup:
    """A written as a bracketed 2x2 grid of Text entries (no LaTeX on the render machine)."""
    entries = VGroup(*[label(number(value), size=30) for value in MATRIX.flatten()])
    entries.arrange_in_grid(rows=2, cols=2, buff=(0.45, 0.2))
    height = entries.height + 0.2
    brackets = VGroup()
    for side, edge in ((LEFT, entries.get_left()), (RIGHT, entries.get_right())):
        x = edge[0] + side[0] * 0.18
        top, bottom = [x, entries.get_center()[1] + height / 2, 0], [x, entries.get_center()[1] - height / 2, 0]
        tick = -side * 0.1
        brackets.add(Line(top, bottom, color=INK, stroke_width=2.5),
                     Line(top, top + tick, color=INK, stroke_width=2.5),
                     Line(bottom, bottom + tick, color=INK, stroke_width=2.5))
    name = label("A =", size=30).next_to(brackets, LEFT, buff=0.2)
    return VGroup(name, brackets.set_z_index(10), entries)


class EigenvectorsScene(Scene):
    """Grid transform by A, then the ordinary vectors, then the eigenvectors, then the takeaway."""

    def construct(self) -> None:
        self.ordinary, self.eigen = tracked_vectors()
        self.progress = ValueTracker(0.0)
        self.camera.background_color = CANVAS
        self.add(masks())
        self.intro_beat()
        self.transform_beat()
        self.ordinary_beat()
        self.eigen_beat()
        self.takeaway_beat()

    def hold_until(self, seconds: float) -> None:
        remaining = seconds - self.time
        if remaining > 1 / FPS:
            self.wait(remaining)

    def arrow(self, vector: TrackedVector) -> Arrow:
        def build() -> Arrow:
            blend = (1 - self.progress.get_value()) * np.eye(2) + self.progress.get_value() * MATRIX
            return Arrow(to_scene(np.zeros(2)), to_scene(blend @ vector.start), buff=0, color=vector.color,
                         stroke_width=6, max_tip_length_to_length_ratio=0.18).set_z_index(3)
        return always_redraw(build)

    def intro_beat(self) -> None:
        title = label("Most vectors get knocked off their line. Eigenvectors don't.", size=32)
        title.to_edge(UP, buff=0.3).set_x(0)
        self.matrix = matrix_mobject().move_to([PANEL_LEFT, 2.15, 0], aligned_edge=LEFT)
        self.moving_grid = grid(MOVING_GRID, MOVING_AXES, 1.5)
        vectors = self.ordinary + self.eigen
        self.arrows = [self.arrow(vector) for vector in vectors]
        self.add(grid(STATIC_GRID, STATIC_GRID, 1.0))
        self.play(Write(title), Create(self.moving_grid), FadeIn(self.matrix), run_time=1.8)
        self.play(*[Create(span_line(vector)) for vector in vectors], run_time=1.2)
        self.play(*[FadeIn(arrow) for arrow in self.arrows], run_time=1.0)
        self.hold_until(INTRO_SECONDS)

    def transform_beat(self) -> None:
        self.play(ApplyMatrix(MATRIX, self.moving_grid, about_point=VIEWPORT_CENTER),
                  self.progress.animate.set_value(1.0), run_time=TRANSFORM_SECONDS)
        self.hold_until(INTRO_SECONDS + TRANSFORM_BEAT_SECONDS)

    def vector_row(self, vector: TrackedVector, anchor: Text | VGroup) -> VGroup:
        """One line in the panel: the move, then what it means (turn angle or eigenvalue)."""
        move_text = f"{pair(vector.start)} → {pair(vector.end)}"
        if vector.is_eigenvector:
            move_text += f" = {number(vector.eigenvalue)} × {pair(vector.start)}"
            verdict = f"λ = {number(vector.eigenvalue)}"
        else:
            verdict = f"turned {vector.turn_degrees():.1f}°"
        move = label(move_text, color=vector.color, size=24)
        note = label(verdict, color=vector.color if vector.is_eigenvector else MUTED_INK, size=22)
        row = VGroup(move, note).arrange(RIGHT, buff=0.35)
        return row.next_to(anchor, DOWN, buff=0.2, aligned_edge=LEFT).set_x(PANEL_LEFT, direction=LEFT)

    def ordinary_beat(self) -> None:
        heading = label("Ordinary vectors: turned", color=MUTED_INK, size=24)
        heading.next_to(self.matrix, DOWN, buff=0.32).set_x(PANEL_LEFT, direction=LEFT)
        rows = [self.vector_row(self.ordinary[0], heading)]
        rows.append(self.vector_row(self.ordinary[1], rows[0]))
        self.play(FadeIn(heading), FadeIn(rows[0]), Indicate(self.arrows[0], color=self.ordinary[0].color))
        self.play(FadeIn(rows[1]), Indicate(self.arrows[1], color=self.ordinary[1].color))
        self.last_row = rows[1]
        self.hold_until(INTRO_SECONDS + TRANSFORM_BEAT_SECONDS + ORDINARY_BEAT_SECONDS)

    def eigen_beat(self) -> None:
        start = INTRO_SECONDS + TRANSFORM_BEAT_SECONDS + ORDINARY_BEAT_SECONDS
        heading = label("Eigenvectors: same line, only scaled", color=MUTED_INK, size=24)
        heading.next_to(self.last_row, DOWN, buff=0.32).set_x(PANEL_LEFT, direction=LEFT)
        anchor: Text | VGroup = heading
        for index, vector in enumerate(self.eigen):
            row = self.vector_row(vector, anchor)
            tag = label(f"×{number(vector.eigenvalue)}", color=vector.color, size=26)
            tag.next_to(to_scene(vector.end), UP + RIGHT if vector.start[0] > 0 else UP + LEFT, buff=0.12)
            arrow = self.arrows[len(self.ordinary) + index]
            self.play(*([FadeIn(heading)] if index == 0 else []), FadeIn(row), FadeIn(tag),
                      Indicate(arrow, color=vector.color, scale_factor=1.15), run_time=1.2)
            anchor = row
            self.hold_until(start + EIGEN_BEAT_SECONDS / 2 * (index + 1))
        self.last_row = anchor

    def takeaway_beat(self) -> None:
        end = INTRO_SECONDS + TRANSFORM_BEAT_SECONDS + ORDINARY_BEAT_SECONDS + EIGEN_BEAT_SECONDS
        rule = label("A v = λ v", size=34)
        meaning = label("same line, scaled by λ", color=MUTED_INK, size=24)
        takeaway = VGroup(rule, meaning).arrange(RIGHT, buff=0.35)
        takeaway.next_to(self.last_row, DOWN, buff=0.4).set_x(PANEL_LEFT + 0.15, direction=LEFT)
        frame = SurroundingRectangle(takeaway, color=INK, stroke_width=2, buff=0.15).set_z_index(10)
        self.play(FadeIn(takeaway), Create(frame), run_time=1.2)
        self.hold_until(end + TAKEAWAY_BEAT_SECONDS)


def render_scene(work_dir: Path) -> Path:
    settings = {"pixel_width": PIXEL_WIDTH, "pixel_height": PIXEL_HEIGHT, "frame_rate": FPS,
                "background_color": CANVAS, "media_dir": str(work_dir), "output_file": BASE_NAME,
                "disable_caching": True, "verbosity": "WARNING", "progress_bar": "none"}
    with tempconfig(settings):
        scene = EigenvectorsScene()
        scene.render()
        return Path(scene.renderer.file_writer.movie_file_path)


def encode(raw_movie: Path, duration: float) -> None:
    """Re-encode small and web-ready, then pull the poster from the final, fully labelled frame."""
    video = OUTPUT_DIR / VIDEO_NAME
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", str(raw_movie), *ENCODE_ARGS, str(video)],
                   check=True)
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-ss", f"{duration - 0.5:.2f}", "-i", str(video),
                    "-frames:v", "1", str(OUTPUT_DIR / POSTER_NAME)], check=True)


def main() -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    ordinary, eigen = tracked_vectors()
    cues = caption_cues(ordinary, eigen)
    with tempfile.TemporaryDirectory(prefix="manim-eigen-") as work_dir:
        encode(render_scene(Path(work_dir)), duration=cues[-1][1])
    write_captions(cues)
    print("transcript (paste into the page's video fence):")
    for _, _, text in cues:
        print(f"  {text}")
    print(f"duration {cues[-1][1]:.1f} s | eigenpairs "
          + ", ".join(f"λ = {number(v.eigenvalue)} along {pair(v.start)}" for v in eigen))


if __name__ == "__main__":
    main()
