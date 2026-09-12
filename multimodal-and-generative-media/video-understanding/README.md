---
id: "13-video-understanding"
topic: "Video Understanding"
level: advanced
built_from: ["computer-vision", "multimodal"]
leads_to: ["agentic-ai"]
updated: 2026-09-07
---

# Video Understanding
> Models that *watch* — temporal representation, action recognition, video-language reasoning,
> and the systems tricks that make hour-long video tractable. Video *generation* lives in
> [Diffusion](/ai-ml/ai-ml-learning-resources/models-and-architectures/generative-model-families/diffusion-models/readme); classic optical flow lives in
> [Computer Vision](/ai-ml/ai-ml-learning-resources/multimodal-and-generative-media/computer-vision/readme).

**⭐ Start here:** [CS231n 2025 Lecture 10 — Video Understanding](https://cs231n.stanford.edu/slides/2025/lecture_10.pdf) — **Ruohan Gao (Stanford)** — the current free map of the whole field, from 3D convolutions to video transformers.

## Concept Index
Every chapter is a self-contained folder (`<topic>/<topic>.md`) with its page.
> Representations first, then tasks, then long-video systems.

### Temporal representations
1. ✅ [Video Representations & Temporal Modeling](/ai-ml/ai-ml-learning-resources/multimodal-and-generative-media/video-understanding/video-representations-and-temporal-modeling/video-representations-and-temporal-modeling) (3D CNNs · two-stream · frame sampling)
2. ✅ [Video Transformers — TimeSformer & ViViT](/ai-ml/ai-ml-learning-resources/multimodal-and-generative-media/video-understanding/video-transformers-timesformer-vivit/video-transformers-timesformer-vivit) (space-time attention trade-offs)
3. ✅ [Self-Supervised Video Pretraining](/ai-ml/ai-ml-learning-resources/multimodal-and-generative-media/video-understanding/self-supervised-video-pretraining-videomae/self-supervised-video-pretraining-videomae) (VideoMAE · V-JEPA · contrastive video)

### Core tasks
4. ✅ [Action Recognition & Video Classification](/ai-ml/ai-ml-learning-resources/multimodal-and-generative-media/video-understanding/action-recognition-and-video-classification/action-recognition-and-video-classification)
5. ✅ [Temporal Localization & Moment Retrieval](/ai-ml/ai-ml-learning-resources/multimodal-and-generative-media/video-understanding/temporal-localization-and-moment-retrieval/temporal-localization-and-moment-retrieval)
6. ✅ [Video-Language Models](/ai-ml/ai-ml-learning-resources/multimodal-and-generative-media/video-understanding/video-language-models/video-language-models) (video captioning · VideoQA · video chat)

### Long video & systems
7. ✅ [Long-Video Understanding](/ai-ml/ai-ml-learning-resources/multimodal-and-generative-media/video-understanding/long-video-understanding/long-video-understanding) (memory · keyframe selection · token budgets)
8. ✅ [Efficient Video Inference](/ai-ml/ai-ml-learning-resources/multimodal-and-generative-media/video-understanding/efficient-video-inference/efficient-video-inference) (streaming · caching · frame-rate scheduling)

### Related concepts (covered in another section)
> Kept in their canonical home to avoid repetition.
- **Optical flow & classic video features** → [Computer Vision · Optical Flow & Video](/ai-ml/ai-ml-learning-resources/multimodal-and-generative-media/computer-vision/optical-flow-and-video/optical-flow-and-video)
- **Object tracking & detection backbones** → [Computer Vision](/ai-ml/ai-ml-learning-resources/multimodal-and-generative-media/computer-vision/readme)
- **Video diffusion / generation** → [Diffusion · Video Diffusion Models](/ai-ml/ai-ml-learning-resources/models-and-architectures/generative-model-families/diffusion-models/readme)
- **VLM fusion architectures** → [Multimodal](/ai-ml/ai-ml-learning-resources/multimodal-and-generative-media/multimodal-learning/readme)

## Courses
- [Stanford CS231n — Deep Learning for Computer Vision](https://cs231n.stanford.edu/) — **Stanford** — free notes and assignments; Lecture 10 of the 2025 edition is a full video-understanding lecture.
- [Community Computer Vision Course — Unit 7: Video Processing](https://huggingface.co/learn/computer-vision-course/en/unit7/video-processing/introduction-to-video) — **Hugging Face** — free, code-first unit from frame decoding to video transformers.
- [MIT 6.5940 — TinyML and Efficient Deep Learning Computing](https://hanlab.mit.edu/courses/2024-fall-65940) — **Song Han (MIT)** — the efficiency half: video FLOPs, streaming, and long-context serving.

## Videos
- [Lecture 18: Videos](https://www.youtube.com/watch?v=A9D6NXBJdwU) — **Michigan Online (Justin Johnson)** — the clearest free lecture deriving every temporal-fusion strategy.
- [V-JEPA: Revisiting Feature Prediction (Explained)](https://www.youtube.com/watch?v=7UkJPwz_N_0) — **Yannic Kilcher** — the latent-prediction alternative to masked pixel reconstruction.
- [EfficientML.ai Lecture 17 — GAN, Video, Point Cloud](https://www.youtube.com/watch?v=o_60Yhb79W8) — **MIT HAN Lab (Song Han)** — what video models cost, measured on real hardware.

## Key Papers
- [Is Space-Time Attention All You Need for Video Understanding? (TimeSformer)](https://arxiv.org/abs/2102.05095) — **Bertasius et al. (2021)** — the video-transformer design space.
- [ViViT: A Video Vision Transformer](https://arxiv.org/abs/2103.15691) — **Arnab et al. (2021)** — factorized space-time attention.
- [VideoMAE](https://arxiv.org/abs/2203.12602) — **Tong et al. (2022)** — self-supervised video pretraining that actually scales down.
- [V-JEPA 2: Self-Supervised Video Models Enable Understanding, Prediction and Planning](https://arxiv.org/abs/2506.09985) — **Assran et al. (2025)** — video pretraining at 1M+ hours, used as a world model for planning.
- [Qwen2.5-VL Technical Report](https://arxiv.org/abs/2502.13923) — **Bai et al. (2025)** — hour-long video with second-level temporal grounding in an open model.

## Articles
- [Video classification](https://huggingface.co/docs/transformers/tasks/video_classification) — **Hugging Face** — hands-on fine-tuning path.
- [Advancing the frontier of video understanding with Gemini 2.5](https://developers.googleblog.com/en/gemini-2-5-video-understanding/) — **Google** — a frontier lab's account of native long-video input.
- [Introducing agentic video understanding with Gemini](https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-agentic-video-in-gemini/) — **Google** — the 2026 move from full-prompt video to agentic search over video.

## In this platform
- Backbones: [Computer Vision](/ai-ml/ai-ml-learning-resources/multimodal-and-generative-media/computer-vision/readme) · Reasoning side: [Multimodal](/ai-ml/ai-ml-learning-resources/multimodal-and-generative-media/multimodal-learning/readme)
- Systems side: [Long-Context Architectures](/ai-ml/ai-ml-learning-resources/models-and-architectures/large-language-models/long-context-architectures/long-context-architectures) · [KV Cache](/ai-ml/ai-ml-learning-resources/inference-and-serving/kv-cache/kv-cache)
