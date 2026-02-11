import pandas as pd
import numpy as np

def evaluate_thresholds(preds, y_real):
    thresholds = np.arange(0.002, 0.02, 0.002)
    results = []

    for t in thresholds:
        # Longs e Shorts
        longs = preds >= t
        shorts = preds <= -t

        trades = longs.sum() + shorts.sum()
        if trades == 0: continue

        # Retorno: Se for short, o ganho real é o inverso do movimento do preço
        ret_longs = y_real[longs]
        ret_shorts = -y_real[shorts]

        all_returns = pd.concat([ret_longs, ret_shorts])

        results.append({
            'threshold': t,
            'total_trades': trades,
            'winrate': (all_returns > 0).mean(),
            'avg_ret_per_trade': all_returns.mean(),
            'total_accumulated': all_returns.sum()  # Soma dos retornos
        })

    return pd.DataFrame(results).sort_values('total_accumulated', ascending=False)