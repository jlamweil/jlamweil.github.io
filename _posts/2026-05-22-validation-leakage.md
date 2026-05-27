---
title: Avoiding Validation Leakage in Small ML Experiments
date: 2026-05-22
slug: validation-leakage
tags:
  - machine-learning
  - data-science
  - evaluation
excerpt: A short note on how leakage sneaks into model selection and how to keep your validation loop honest.
---

Validation leakage usually shows up when preprocessing learns from the full dataset before the split. In small experiments, that can make a weak model look surprisingly strong.

The safest pattern is simple: split first, fit transforms only on the training fold, and keep the test set untouched until the very end.

```python
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

model = Pipeline([
    ("scale", StandardScaler()),
    ("clf", LogisticRegression(max_iter=1000)),
])

model.fit(X_train, y_train)
score = model.score(X_test, y_test)
print(f"Holdout accuracy: {score:.3f}")
```

When the dataset is tiny, cross-validation helps, but only if every step lives inside the CV loop. Otherwise the leakage just becomes harder to see.
