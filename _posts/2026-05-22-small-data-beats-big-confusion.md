---
title: "Small data beats big confusion"
date: 2026-05-22
slug: small-data-beats-big-confusion
tags:
  - data-science
  - machine-learning
  - statistics
excerpt: "When you cannot get more data, think harder about the structure of the problem."
---

More data is not always the answer. When examples are scarce, inductive bias — the assumptions baked into your model — dominates performance.

## The small-data regime

With enough data, almost any reasonable model will converge to the same solution. With little data, the choice of model *is* the experiment.

```python
import numpy as np
from sklearn.gaussian_process import GaussianProcessRegressor
from sklearn.gaussian_process.kernels import RBF, WhiteKernel

# A kernel that encodes smoothness + noise
kernel = RBF(length_scale=1.0) + WhiteKernel(noise_level=0.1)
gp = GaussianProcessRegressor(kernel=kernel)
gp.fit(X_train, y_train)
```

A GP with a well-chosen kernel can extract signal from 20–50 points that a linear model would miss entirely.

## The principle

> All models are wrong, but the right prior makes the small-data problem tractable.

This is not about "using a complicated model" — it is about encoding what you already know: smoothness, additivity, monotonicity, periodicity.

## What this means in practice

- Spend time on feature engineering — it is a stronger prior than any regulariser.
- Use Bayesian methods when you can quantify uncertainty.
- Test on a held-out set even if it is just 5–10 points.
- Report uncertainty intervals, not just point estimates.
