---
title: "Put preprocessing inside the pipeline"
date: 2026-05-22
slug: preprocessing-inside-pipeline
tags:
  - python
  - scikit-learn
  - data-science
excerpt: "Fit preprocessing steps on the training split only to avoid data leakage."
draft: true
---

A common mistake in sklearn workflows: scaling, imputation, or encoding the full dataset **before** the train/test split.

## The mistake

```python
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

# WRONG: scaler sees the whole dataset
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y)
```

The test set has already influenced the scaling parameters (mean, variance). This is a mild form of data leakage.

## The fix

```python
from sklearn.pipeline import Pipeline
from sklearn.svm import SVC

pipe = Pipeline([
    ("scale", StandardScaler()),
    ("clf", SVC()),
])

# scaler fits only on X_train
pipe.fit(X_train, y_train)
score = pipe.score(X_test, y_test)
```

## Why pipelines are better

- They enforce the correct fit/transform split automatically.
- They compose: stack preprocessing, dimensionality reduction, and prediction into one object.
- They serialise as a single unit (`pickle.dump(pipe, f)`).
- They play nicely with `cross_validate` and `GridSearchCV`.

## Rule of thumb

If it calls `.fit()` on data, it belongs **inside** the cross-validation loop.
