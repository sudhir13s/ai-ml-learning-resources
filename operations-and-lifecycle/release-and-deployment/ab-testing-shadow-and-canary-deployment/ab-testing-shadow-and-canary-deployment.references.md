---
id: "18-mlops/ab-testing-shadow-and-canary-deployment/references"
topic: "A/B Testing · Shadow & Canary Deployment — References"
parent: "18-mlops/ab-testing-shadow-and-canary-deployment"
type: references
updated: 2026-09-13
---

# A/B Testing, Shadow and Canary Deployment — references

> Companion link library for **[A/B Testing, Shadow and Canary Deployment](/ai-ml/ai-ml-learning-resources/operations-and-lifecycle/release-and-deployment/ab-testing-shadow-and-canary-deployment/ab-testing-shadow-and-canary-deployment)** (the teaching page). Internal links and external sources, grouped by type and alphabetical within each group.

**Start here — suggested path**:

1. **See a rollout run itself** — watch [Progressive Delivery Made Easy With Argo Rollouts](https://www.youtube.com/watch?v=C34TJFDsq-s). *Analysis that promotes or aborts from live metrics, no human in the loop.*
2. **Get the canary right** — read [Canary Release](https://martinfowler.com/bliki/CanaryRelease.html), then [Canarying Releases](https://sre.google/workbook/canarying-releases/). *The ramp, the gate metrics, and sizing a canary so its signal is real.*
3. **Shadow before you expose anyone** — read [Shadow tests (Amazon SageMaker)](https://docs.aws.amazon.com/sagemaker/latest/dg/shadow-tests.html). *Mirror live traffic, serve none of it.*
4. **Run the controller** — read [A/B Testing, Shadow and Canary Deployment](/ai-ml/ai-ml-learning-resources/operations-and-lifecycle/release-and-deployment/ab-testing-shadow-and-canary-deployment/ab-testing-shadow-and-canary-deployment) and run its canary. *Stable-hash routing, the ramp, and a blast radius you can count.*
5. **Get the A/B statistics right** — go to [Mathematical Foundations](/ai-ml/ai-ml-learning-resources/foundations/mathematical-foundations/readme). *Hypothesis tests, power and variance reduction live there.*

**In this platform**:
- [CI/CD for ML and Continuous Training](/ai-ml/ai-ml-learning-resources/operations-and-lifecycle/release-and-deployment/cicd-for-ml-and-continuous-training/cicd-for-ml-and-continuous-training) — the evaluation gate a model passes before any of these strategies begin.
- [Data and Concept Drift Detection](/ai-ml/ai-ml-learning-resources/operations-and-lifecycle/monitoring-and-reliability/data-and-concept-drift-detection/data-and-concept-drift-detection) — what changes after a successful rollout.
- [Mathematical Foundations](/ai-ml/ai-ml-learning-resources/foundations/mathematical-foundations/readme) — the A/B-test statistics: hypothesis tests, power, variance reduction.
- [ml-platform](/python/python-production-examples/ml-platform/readme) — the runnable service with canary, blue-green, shadow and A/B routing.
- [Model Monitoring and Observability](/ai-ml/ai-ml-learning-resources/operations-and-lifecycle/monitoring-and-reliability/model-monitoring-and-observability/model-monitoring-and-observability) — where the gate's live error-rate and latency signals come from.
- [Model Registry and Governance](/ai-ml/ai-ml-learning-resources/operations-and-lifecycle/governance-and-economics/model-registry-and-governance/model-registry-and-governance) — the versions a rollout moves traffic between.
- [Model Serving](/ai-ml/ai-ml-learning-resources/inference-and-serving/packaging-and-serving/model-serving/model-serving) — the runtime the router sends requests to.
- [Rollback and Recovery for ML Systems](/ai-ml/ai-ml-learning-resources/operations-and-lifecycle/release-and-deployment/rollback-and-recovery-for-ml-systems/rollback-and-recovery-for-ml-systems) — what happens when the canary fails.

**Videos**:
- [Progressive Delivery Made Easy With Argo Rollouts](https://www.youtube.com/watch?v=C34TJFDsq-s) — **CNCF (Kevin Dubois, Red Hat)** — canary and blue-green as a Kubernetes controller, with automated metric analysis deciding promote-or-abort.
- [Testing & Deployment — course overview](https://www.youtube.com/watch?v=Dk-95mt0MLA) — **The Full Stack** — why offline tests never settle the question, and what shipping behind a traffic split buys you.

**Courses**:
- [Made With ML — MLOps Course](https://madewithml.com/courses/mlops/) — **Goku Mohandas** — safe rollout within the production workflow.

**Articles**:
- [BlueGreenDeployment](https://martinfowler.com/bliki/BlueGreenDeployment.html) — **Martin Fowler** — the canonical definition of two environments and one switch.
- [Canary Release](https://martinfowler.com/bliki/CanaryRelease.html) — **Martin Fowler** — the canonical definition of progressive rollout.
- [Continuous Delivery for Machine Learning (CD4ML)](https://martinfowler.com/articles/cd4ml.html) — **Sato, Wider & Windheuser (martinfowler.com)** — model rollout inside the delivery pipeline.
- [Rules of Machine Learning](https://developers.google.com/machine-learning/guides/rules-of-ml) — **Google** — "measure the metric that matters" and launch discipline.

**Papers**:
- [Challenges in Deploying Machine Learning: A Survey of Case Studies](https://arxiv.org/abs/2011.09926) — **Paleyes, Urma & Lawrence (2020)** — why offline metrics mislead and rollout safety matters.
- [The ML Test Score: A Rubric for ML Production Readiness](https://research.google/pubs/the-ml-test-score-a-rubric-for-ml-production-readiness-and-technical-debt-reduction/) — **Breck et al. (Google, 2017)** — testing in production as part of production readiness.

**Documentation**:
- [Argo Rollouts — Analysis and progressive delivery](https://argo-rollouts.readthedocs.io/en/stable/features/analysis/) — **Argo Project (CNCF)** — analysis runs as the promotion gate for each ramp step.
- [Argo Rollouts — Documentation](https://argo-rollouts.readthedocs.io/en/stable/) — **Argo Project (CNCF)** — canary and blue-green as a Kubernetes resource.
- [KServe — canary rollout](https://kserve.github.io/website/latest/modelserving/v1beta1/rollout/canary/) — **KServe maintainers** — traffic-split canaries applied directly to model servers.
- [Shadow tests (Amazon SageMaker)](https://docs.aws.amazon.com/sagemaker/latest/dg/shadow-tests.html) — **AWS** — production shadow-testing mechanics and the metrics compared.

**Books**:
- [*Designing Machine Learning Systems* — Ch. 9 "Continual Learning & Test in Production"](https://huyenchip.com/mlops/) — **Chip Huyen** — shadow, canary, A/B and bandits as test-in-production strategies.
- [*Machine Learning Engineering* — Ch. 8 "Model Deployment"](http://www.mlebook.com/wiki/doku.php) — **Andriy Burkov** — deployment strategies; read-first chapters online.
- [*The Site Reliability Workbook* — "Canarying Releases"](https://sre.google/workbook/canarying-releases/) — **Google SRE** — sizing a canary, choosing the evaluation window, and the failure modes of "it looked fine at 1%".
