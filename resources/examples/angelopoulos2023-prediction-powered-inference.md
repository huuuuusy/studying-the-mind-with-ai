**English** · [中文](angelopoulos2023-prediction-powered-inference.zh.md)

# Valid conclusions from AI labels and a few human labels

**Study.** Angelopoulos, A. N., Bates, S., Fannjiang, C., Jordan, M. I., & Zrnic, T. (2023). Prediction-powered inference. *Science, 382*(6671), 669–674. [doi:10.1126/science.adi6000](https://doi.org/10.1126/science.adi6000) · [arXiv](https://arxiv.org/abs/2301.09633)

**In the talk.** Not shown; read it with [Part 4, AI in your own research](../../docs/part4-ai-in-your-research.md): if a model codes most of your data, what can you still conclude?

**Question.** Suppose a model labels thousands of items and people label only a few hundred. How can you use both and still get confidence intervals you can trust, without assuming the model is right?

**Method.** A statistical framework. The small set of items labelled by people is used to measure how far the model's predictions are off, and that correction is applied to the estimate from the large set labelled by the model. The framework gives simple algorithms for confidence intervals for means, quantiles, and linear and logistic regression coefficients.

**Finding.** The confidence intervals are provably valid, with no assumptions about the machine-learning system that supplies the predictions. The more accurate the predictions, the smaller the intervals. The method is demonstrated with data from proteomics, astronomy, genomics, remote sensing, census analysis and ecology.

**Why read it.** It answers the statistical question that comes after "can a model code my data?": how to draw valid conclusions when it does, and how many human labels you still need.

**Limits.** The human-labelled items must be a random sample from the same population as the model-labelled ones. The method corrects the model's errors on average; it does not make a biased model's labels valid item by item.

**Data and code.** Python package: [github.com/aangelopoulos/ppi_py](https://github.com/aangelopoulos/ppi_py) (MIT).
