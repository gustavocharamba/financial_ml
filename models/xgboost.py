import pandas as pd
import numpy as np
from xgboost import XGBRegressor
from sklearn.model_selection import GridSearchCV, TimeSeriesSplit
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score


def xgboost_model(X_train, y_train):
    base_xgb = XGBRegressor(
        objective='reg:squarederror',
        random_state=42,
        n_jobs=-1,
        tree_method='hist'
    )

    param_grid_xgb = {
        'n_estimators': [100, 200],
        'max_depth': [3, 5, 7],
        'learning_rate': [0.01, 0.05, 0.1],
        'subsample': [0.8]
    }

    tscv = TimeSeriesSplit(n_splits=3)

    grid = GridSearchCV(
        base_xgb,
        param_grid_xgb,
        scoring='neg_mean_absolute_error',
        cv=tscv,
        n_jobs=-1
    )

    grid.fit(X_train, y_train)
    best_xgb = grid.best_estimator_

    y_pred_train = best_xgb.predict(X_train)

    # Para calculo interno do pipeline, pegamos o ultimo pedaço do treino como "teste"
    split = int(len(X_train) * 0.8)
    X_val, y_val = X_train.iloc[split:], y_train.iloc[split:]
    y_pred_val = best_xgb.predict(X_val)

    metrics = pd.DataFrame({
        'MAE_teste': [mean_absolute_error(y_val, y_pred_val)],
        'RMSE_teste': [np.sqrt(mean_squared_error(y_val, y_pred_val))],
        'R2_teste': [r2_score(y_val, y_pred_val)],
        'MAE_treino': [mean_absolute_error(y_train, y_pred_train)],
        'Best_Params': [str(grid.best_params_)]
    })

    return best_xgb, metrics