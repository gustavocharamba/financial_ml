import numpy as np
import pandas as pd
from models.random_forest import random_forest_model


def walk_forward(X, y, train_size=0.6, step_size=0.1):
    preds = np.full(len(y), np.nan)
    all_metrics = []

    n = len(X)
    train_end = int(n * train_size)
    step = int(n * step_size)

    while train_end < n:
        X_train = X.iloc[:train_end]
        y_train = y.iloc[:train_end]
        X_test = X.iloc[train_end:train_end + step]

        model, metrics_df = random_forest_model(X_train, y_train)
        all_metrics.append(metrics_df)

        y_pred = model.predict(X_test)
        preds[train_end:train_end + len(y_pred)] = y_pred
        train_end += step

    # Consolida e tira a média de tudo
    metrics_summary = pd.concat(all_metrics).mean(numeric_only=True)

    return pd.Series(preds, index=y.index), metrics_summary