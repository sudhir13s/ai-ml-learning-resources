---
id: "18-mlops/model-monitoring-and-observability/references"
topic: "Model Monitoring & Observability — References"
parent: "18-mlops/model-monitoring-and-observability"
type: references
updated: 2026-09-13
---

# Model Monitoring and Observability — references

> Companion link library for **[Model Monitoring and Observability](/ai-ml/ai-ml-learning-resources/operations-and-lifecycle/monitoring-and-reliability/model-monitoring-and-observability/model-monitoring-and-observability)** — grouped by type, alphabetical within each group.

**Start here — suggested path**:
1. **Hear what to watch and why** — watch [ML Monitoring — Stanford CS329S guest lecture](https://www.youtube.com/watch?v=uVqfYkcodeE) (**WhyLabs, Alessya Visnjic**). *What to log, what to alert on, and why model quality is the last layer you can measure.*
2. **Understand the delayed-label problem** — read [Data Distribution Shifts and Monitoring](https://huyenchip.com/2022/02/07/data-distribution-shifts-and-monitoring.html) (**Chip Huyen**). *What degrades, what you can observe, and what arrives too late.*
3. **Lay out the layers** — read [How to Monitor Machine Learning Models](https://christophergs.com/machine%20learning/2020/03/14/how-to-monitor-machine-learning-models/) (**Christopher Samiullah**). *The operational, data and model layers the page's pyramid is built from.*
4. **See why ML systems erode silently** — read [Hidden Technical Debt in Machine Learning Systems](https://papers.nips.cc/paper/2015/file/86df7dcfd896fcaf2674f757a2463eba-Paper.pdf) (**Sculley et al., 2015**). *The monitoring-and-testing debt that makes this discipline necessary.*
5. **Run a monitoring service** — run [ml-platform](/python/python-production-examples/ml-platform/readme) (**this platform**). *The page's signals wired into working code.*

## References

- **In this platform**:
  - [AI Incident Response and Postmortems](/ai-ml/ai-ml-learning-resources/operations-and-lifecycle/monitoring-and-reliability/ai-incident-response-and-postmortems/ai-incident-response-and-postmortems) — what happens after a monitoring alert turns out to be real.
  - [Calibration and Reliability Diagrams](/ai-ml/ai-ml-learning-resources/classical-machine-learning/model-selection-and-evaluation/calibration-and-reliability-diagrams/calibration-and-reliability-diagrams) — score calibration as a quality proxy before labels arrive.
  - [Continuous Training](/ai-ml/ai-ml-learning-resources/operations-and-lifecycle/lifecycle-and-reproducibility/continuous-training/continuous-training) — why models decay, and the retraining loop a drift alert triggers.
  - [Data and Concept Drift Detection](/ai-ml/ai-ml-learning-resources/operations-and-lifecycle/monitoring-and-reliability/data-and-concept-drift-detection/data-and-concept-drift-detection) — the statistical tests behind the drift layer.
  - [LLMOps](/ai-ml/ai-ml-learning-resources/operations-and-lifecycle/governance-and-economics/llmops/llmops) — the large-language-model flavour of operating a model.
  - [ML Lifecycle and MLOps Maturity](/ai-ml/ai-ml-learning-resources/operations-and-lifecycle/lifecycle-and-reproducibility/ml-lifecycle-and-mlops-maturity/ml-lifecycle-and-mlops-maturity) — where monitoring sits in the lifecycle.
  - [ml-platform](/python/python-production-examples/ml-platform/readme) — the runnable monitoring service.
  - [Model Monitoring and Observability](/ai-ml/ai-ml-learning-resources/operations-and-lifecycle/monitoring-and-reliability/model-monitoring-and-observability/model-monitoring-and-observability) — the teaching page this list supports.
  - [Model Serving](/ai-ml/ai-ml-learning-resources/inference-and-serving/packaging-and-serving/model-serving/model-serving) — where the operational layer's signals originate.
  - [Monitoring and Observability workflow](/ai-ml/practitioner-workflows/evaluation-and-safety/monitoring-and-observability) — the application layer: tracing, token dashboards, service-level objectives.
  - [Rollback and Recovery for ML Systems](/ai-ml/ai-ml-learning-resources/operations-and-lifecycle/release-and-deployment/rollback-and-recovery-for-ml-systems/rollback-and-recovery-for-ml-systems) — the response when a release caused the regression.
- **Videos**:
  - [Data Drift & Early Monitoring for ML Models](https://www.youtube.com/watch?v=N12uMO-fj40) — **Datafold (Emeli Dral, Evidently AI)** — meetup talk on what to monitor and why.
  - [ML Model Monitoring Dashboard with Evidently — Batch Architecture](https://www.youtube.com/watch?v=u4Mcu0hXfMA) — **Evidently AI** — code practice for batch monitoring.
  - [ML Model Monitoring Dashboard with Evidently — Online Architecture](https://www.youtube.com/watch?v=2hTRXEOJF8k) — **Evidently AI** — code practice for live-service monitoring.
  - [ML Monitoring — Stanford CS329S guest lecture](https://www.youtube.com/watch?v=uVqfYkcodeE) — **WhyLabs (Alessya Visnjic)** — what to log, what to alert on, and why model quality is the last layer you can measure.
- **Courses**:
  - [Evidently — ML Observability Course](https://learn.evidentlyai.com/ml-observability-course/module-1-introduction/ml-monitoring-observability) — **Evidently AI** — end-to-end open course on monitoring and observability.
  - [Made With ML — Monitoring](https://madewithml.com/courses/mlops/monitoring/) — **Goku Mohandas** — monitor performance, data and drift in a real system.
- **Articles**:
  - [A Practical Guide to Maintaining Machine Learning in Production](https://eugeneyan.com/writing/practical-guide-to-maintaining-machine-learning/) — **Eugene Yan** — model health checks, staleness and what to watch after launch.
  - [Data Distribution Shifts and Monitoring](https://huyenchip.com/2022/02/07/data-distribution-shifts-and-monitoring.html) — **Chip Huyen** — chapter-length treatment of what degrades, what you can observe, and the delayed-label problem.
  - [Evidently — Model Monitoring](https://www.evidentlyai.com/ml-in-production/model-monitoring) — **Evidently AI** — what to track and how, with the delayed-label problem.
  - [How to Monitor Machine Learning Models](https://christophergs.com/machine%20learning/2020/03/14/how-to-monitor-machine-learning-models/) — **Christopher Samiullah** — the three-layer monitoring guide.
  - [Rules of Machine Learning](https://developers.google.com/machine-learning/guides/rules-of-ml) — **Google** — monitoring and "test in production" heuristics.
- **Papers**:
  - [Challenges in Deploying ML: A Survey of Case Studies](https://arxiv.org/abs/2011.09926) — **Paleyes et al. (2020)** — post-deployment monitoring failures across industry.
  - [Hidden Technical Debt in Machine Learning Systems](https://papers.nips.cc/paper/2015/file/86df7dcfd896fcaf2674f757a2463eba-Paper.pdf) — **Sculley et al. (2015)** — "monitoring and testing" debt; why ML systems erode silently.
- **Documentation**:
  - [Evidently Documentation](https://docs.evidentlyai.com/) — **Evidently AI** — reports, test suites and the metric catalog, including LLM outputs.
- **Books**:
  - [Designing Machine Learning Systems — Ch. 8 "Data Distribution Shifts & Monitoring"](https://huyenchip.com/mlops/) — **Chip Huyen** — the canonical chapter on monitoring and shift.
  - [Machine Learning Engineering — Ch. 9 "Model Serving, Monitoring & Maintenance"](http://www.mlebook.com/wiki/doku.php) — **Andriy Burkov** — read-first chapters available on the author's site.
  - [Reliable Machine Learning](https://www.oreilly.com/library/view/reliable-machine-learning/9781098106218/) — **Chen, Murphy, Parisa et al. (2022)** — site reliability engineering practices applied to models in production.
