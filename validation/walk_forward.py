import numpy as np
import pandas as pd

def walk_forward(model_func, X, y, train_size=0.6, step_size=0.1, min_test_size=30):
    preds = np.full(len(y), np.nan)
    all_metrics = []

    n = len(X)
    train_end = int(n * train_size)
    step = int(n * step_size)

    last_model = None
    fold = 1

    while train_end < n:

        X_train = X.iloc[:train_end]
        y_train = y.iloc[:train_end]

        X_test = X.iloc[train_end:train_end + step]

        # evita fold muito pequeno
        if len(X_test) < min_test_size:
            break

        model, metrics_df = model_func(X_train, y_train)
        last_model = model

        # garante que metrics seja df 2D
        if isinstance(metrics_df, pd.DataFrame):
            metrics_df['fold'] = fold
            all_metrics.append(metrics_df)

        y_pred = model.predict(X_test)
        preds[train_end:train_end + len(y_pred)] = y_pred

        train_end += step
        fold += 1

    # concat correto (corrige erro 3D)
    if len(all_metrics) > 0:
        metrics_df = pd.concat(all_metrics, ignore_index=True)
        metrics_summary = metrics_df.mean(numeric_only=True)
    else:
        metrics_summary = pd.Series()

    return pd.Series(preds, index=y.index), metrics_summary, last_model
