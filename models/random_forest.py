import pandas as pd
import numpy as np
from sklearn.model_selection import TimeSeriesSplit, GridSearchCV
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score


def random_forest_model(X, y):

    split_point = int(len(X) * 0.8)

    X_train, X_test = X.iloc[:split_point], X.iloc[split_point:]
    y_train, y_test = y.iloc[:split_point], y.iloc[split_point:]

    param_grid_rf = {
        'n_estimators': [100],
        'max_depth': [3, 5,7],
        'min_samples_leaf': [100, 200],
        'min_samples_split': [20, 50],
        'max_features': ['sqrt']
    }

    base_rf = RandomForestRegressor(
        random_state=42,
        n_jobs=None,
        bootstrap=True
    )

    tscv = TimeSeriesSplit(n_splits=5)

    grid = GridSearchCV(
        base_rf,
        param_grid_rf,
        scoring='neg_mean_squared_error',
        cv=tscv,
        n_jobs=-1
    )

    grid.fit(X_train, y_train)

    best_rf = grid.best_estimator_

    y_pred_test = best_rf.predict(X_test)
    y_pred_train = best_rf.predict(X_train)

    return best_rf, pd.DataFrame({
        'MAE_teste': [mean_absolute_error(y_test, y_pred_test)],
        'RMSE_teste': [np.sqrt(mean_squared_error(y_test, y_pred_test))],
        'R2_teste': [r2_score(y_test, y_pred_test)],
        'MAE_treino': [mean_absolute_error(y_train, y_pred_train)],
        'Best_Params': [grid.best_params_]
    })
