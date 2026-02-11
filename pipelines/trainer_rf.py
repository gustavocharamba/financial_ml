import pandas as pd
import numpy as np

from processing.pre_processing import get_preprocessing
from indicators.technical.loader_technical import get_technical_indicators
from indicators.statistical.loader_statistical import get_statistical_indicators
from processing.target import get_target

from validation.walk_forward import walk_forward
from validation.evaluate_thresholds import evaluate_thresholds
from models.random_forest import random_forest_model

def run_pipeline_rf(data_path, horizon, name):
    df = pd.read_csv(data_path)
    df = get_preprocessing(df)
    df = get_technical_indicators(df)
    df = get_statistical_indicators(df)

    df = get_target(df, horizon, name)

    df = df.dropna()

    y = df['Target']
    X = df.drop(columns=['Target', 'Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume', 'Date'], errors='ignore')

    preds, avg_metrics = walk_forward(random_forest_model, X, y, train_size=0.7, step_size=0.1)

    print(f"\n===== Performance Média do Modelo: {name} =====")
    print(avg_metrics)
    print("================================================")

    valid_idx = ~np.isnan(preds)
    results = evaluate_thresholds(preds[valid_idx], y[valid_idx])

    return results

results_5m = run_pipeline_rf("../data/btcusd_5m.csv", 12, "5 Min")
results_15m = run_pipeline_rf("../data/btcusd_15m.csv", 16, "15 Min")
results_1h = run_pipeline_rf("../data/btcusd_1h.csv", 24, "1H")

print("\n===== Melhores Thresholds 5 Min =====")
print(results_5m.head(5))

print("\n===== Melhores Thresholds 15 Min =====")
print(results_15m.head(5))

print("\n===== Melhores Thresholds 1H =====")
print(results_1h.head(5))