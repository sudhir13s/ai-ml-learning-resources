---
id: "18-mlops/data-and-concept-drift-detection/references"
topic: "Data & Concept Drift Detection — References"
parent: "18-mlops/data-and-concept-drift-detection"
type: references
updated: 2026-09-13
---

# Data and Concept Drift Detection — references

> Companion link library for **[Data and Concept Drift Detection](/ai-ml/ai-ml-learning-resources/operations-and-lifecycle/monitoring-and-reliability/data-and-concept-drift-detection/data-and-concept-drift-detection)** — grouped by type, alphabetical within each group.

**Start here — suggested path**:
1. **See how to choose a test** — watch [Is My Data Drifting? Early Monitoring for Machine Learning Models in Production](https://www.youtube.com/watch?v=ukWc6mv8ojw) (**PyData Global 2021, Emeli Dral**). *Picking drift tests by data size and type, from an Evidently co-founder.*
2. **Name the shift** — read [What is Data Drift in ML](https://www.evidentlyai.com/ml-in-production/data-drift) (**Evidently AI**). *`P(X)` shift, the tests that detect it, and how to respond.*
3. **See KS over-react at scale** — read [Which test is the best? We compared 5 methods to detect data drift on large datasets](https://www.evidentlyai.com/blog/data-drift-detection-large-datasets) (**Evidently AI**). *Measured KS over-sensitivity and PSI stability as sample size grows — the page's combined verdict.*
4. **Pin down the statistic** — read [Kolmogorov-Smirnov Goodness-of-Fit Test](https://www.itl.nist.gov/div898/handbook/eda/section3/eda35g.htm) (**NIST/SEMATECH e-Handbook**). *Definition, assumptions and interpretation of the KS statistic the page codes.*
5. **Run a drift monitor** — run [ml-platform](/python/python-production-examples/ml-platform/readme) (**this platform**). *The PSI and KS checks running on real feature streams.*

## References

- **In this platform**:
  - [A/B Testing, Shadow and Canary Deployment](/ai-ml/ai-ml-learning-resources/operations-and-lifecycle/release-and-deployment/ab-testing-shadow-and-canary-deployment/ab-testing-shadow-and-canary-deployment) — how a retrained candidate reaches production safely.
  - [CI/CD for ML and Continuous Training](/ai-ml/ai-ml-learning-resources/operations-and-lifecycle/release-and-deployment/cicd-for-ml-and-continuous-training/cicd-for-ml-and-continuous-training) — the pipeline a confirmed drift alert fires.
  - [Continuous Training — detecting drift with PSI](/ai-ml/ai-ml-learning-resources/operations-and-lifecycle/lifecycle-and-reproducibility/continuous-training/continuous-training#detecting-drift-one-number-that-says-different) — covariate versus concept drift, the PSI formula, worked table and bands.
  - [Data and Concept Drift Detection](/ai-ml/ai-ml-learning-resources/operations-and-lifecycle/monitoring-and-reliability/data-and-concept-drift-detection/data-and-concept-drift-detection) — the teaching page this list supports.
  - [Mathematical Foundations](/ai-ml/ai-ml-learning-resources/foundations/mathematical-foundations/readme) — distribution-shift theory and the probability behind the tests.
  - [ml-platform](/python/python-production-examples/ml-platform/readme) — the runnable PSI and KS drift monitor.
  - [Model Monitoring and Observability](/ai-ml/ai-ml-learning-resources/operations-and-lifecycle/monitoring-and-reliability/model-monitoring-and-observability/model-monitoring-and-observability) — the monitoring layers drift detection sits inside.
- **Videos**:
  - [Concept Drift Detection with NannyML](https://www.youtube.com/watch?v=kBTty6JTW9Q) — **NannyML** — detecting `P(Y|X)` change without labels via confidence-based performance estimation.
  - [Data Drift & Early Monitoring for ML Models](https://www.youtube.com/watch?v=N12uMO-fj40) — **Datafold (Emeli Dral, Evidently AI)** — drift detection methods and their pitfalls.
  - [Deep Dive Into Univariate Drift Detection Methods](https://www.youtube.com/watch?v=ZGQny5KlCbo) — **NannyML** — the statistical tests compared head to head, including when each one cries wolf.
  - [Is My Data Drifting? Early Monitoring for Machine Learning Models in Production](https://www.youtube.com/watch?v=ukWc6mv8ojw) — **PyData Global 2021 (Emeli Dral)** — choosing tests by data size and type, from an Evidently co-founder.
  - [Use Evidently in Jupyter to Evaluate Data & Prediction Drift](https://www.youtube.com/watch?v=g0Z2e-IqmmU) — **Evidently AI** — running the drift report and interpreting it, by the library's authors.
- **Courses**:
  - [Evidently — ML Observability Course (Module 2: Data Drift Deep Dive)](https://learn.evidentlyai.com/ml-observability-course/module-2-ml-monitoring-metrics/data-drift-deep-dive) — **Evidently AI** — the statistical drift tests, hands-on and compared.
  - [Made With ML — Monitoring](https://madewithml.com/courses/mlops/monitoring/) — **Goku Mohandas** — drift detection as part of production monitoring.
- **Articles**:
  - [Embedding drift detection](https://www.evidentlyai.com/blog/embedding-drift-detection) — **Evidently AI** — drift in embedding space: model-based, distance and domain-classifier methods.
  - [What is Concept Drift in ML](https://www.evidentlyai.com/ml-in-production/concept-drift) — **Evidently AI** — `P(Y|X)` shift and how to detect it without fresh labels.
  - [What is Data Drift in ML](https://www.evidentlyai.com/ml-in-production/data-drift) — **Evidently AI** — `P(X)` shift, detection tests, and handling.
  - [Which test is the best? We compared 5 methods to detect data drift on large datasets](https://www.evidentlyai.com/blog/data-drift-detection-large-datasets) — **Evidently AI** — measures KS over-sensitivity and PSI stability as sample size grows.
- **Papers**:
  - [A Survey on Concept Drift Adaptation](https://eprints.bournemouth.ac.uk/22491/) — **Gama et al. (2014)** — the canonical taxonomy of drift types and adaptation methods.
  - [Challenges in Deploying ML: A Survey of Case Studies](https://arxiv.org/abs/2011.09926) — **Paleyes et al. (2020)** — drift-driven degradation in real deployments.
  - [Learning under Concept Drift: A Review](https://arxiv.org/abs/1010.4784) — **Žliobaitė (2010)** — foundational survey of drift detection and handling.
  - [The Kolmogorov-Smirnov Test for Goodness of Fit](https://doi.org/10.1080/01621459.1951.10500769) — **Massey (1951), Journal of the American Statistical Association** — the two-sample test and its tables.
- **Documentation**:
  - [Kolmogorov-Smirnov Goodness-of-Fit Test](https://www.itl.nist.gov/div898/handbook/eda/section3/eda35g.htm) — **NIST/SEMATECH e-Handbook of Statistical Methods** — definition, assumptions and interpretation of the KS statistic.
  - [NannyML Documentation](https://nannyml.readthedocs.io/en/stable/) — **NannyML** — confidence-based performance estimation while labels are still missing.
- **Books**:
  - [Designing Machine Learning Systems — Ch. 8 "Data Distribution Shifts & Monitoring"](https://huyenchip.com/mlops/) — **Chip Huyen** — covariate, label and concept shift, and how to detect each.
  - [Machine Learning Engineering — Ch. 9 "Monitoring & Maintenance"](http://www.mlebook.com/wiki/doku.php) — **Andriy Burkov** — distribution shift as an operational concern; read-first chapters on the author's site.
