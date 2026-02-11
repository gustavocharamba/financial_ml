import numpy as np
import pandas as pd

def walk_forward(model_func, X, y, train_size=0.6, step_size=0.1):
    preds = np.full(len(y), np.nan)
    all_metrics = []

    n = len(X)
    train_end = int(n * train_size)
    step = int(n * step_size)

    while train_end < n:
        X_train, y_train = X.iloc[:train_end], y.iloc[:train_end]
        X_test = X.iloc[train_end:train_end + step]

        model, metrics_df = model_func(X_train, y_train)
        all_metrics.append(metrics_df)

        y_pred = model.predict(X_test)
        preds[train_end:train_end + len(y_pred)] = y_pred
        train_end += step

    metrics_summary = pd.concat(all_metrics).mean(numeric_only=True)

    return pd.Series(preds, index=y.index), metrics_summary