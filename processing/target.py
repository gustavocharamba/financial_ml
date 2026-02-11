import pandas as pd
import numpy as np

def get_target(df, horizon, name):
    df['Target'] = (df['Close'].shift(-horizon) / df['Close']) - 1

    df = df.dropna(subset=['Target'])

    total = len(df)
    mean_ret = df['Target'].mean()
    std_ret = df['Target'].std()

    print(f"\n--- Target Regression {name} ---")
    print(f"Janela: {horizon}")
    print(f"Registros: {total}")
    print(f"Retorno Médio: {mean_ret:.4%}")
    print(f"Volatilidade (Std): {std_ret:.4%}")

    return df