import pandas as pd
import numpy as np
from strategy.filters import apply_filters


def evaluate_thresholds(
    preds_1h,
    y_real,
    preds_4h=None,
    preds_1d=None,
    fee=0.001
):
    thresholds = np.arange(0.022, 0.023, 0.0001)

    results = []
    preds_1h = np.array(preds_1h)
    y_real = np.array(y_real)

    if preds_4h is not None:
        preds_4h = np.array(preds_4h)

    if preds_1d is not None:
        preds_1d = np.array(preds_1d)

    for t in thresholds:
        all_rets = []
        last_trade_index = None

        for i in range(len(preds_1h)):

            # -------- FILTROS TIMEFRAME --------
            if not apply_filters(
                index=i,
                preds_1h=preds_1h,
                preds_4h=preds_4h,
                preds_1d=preds_1d,
                last_trade_index=last_trade_index
            ):
                continue

            # -------- SINAIS --------
            if preds_1h[i] >= t:
                ret = y_real[i] - fee
                all_rets.append(ret)
                last_trade_index = i

            elif preds_1h[i] <= -t:
                ret = -y_real[i] - fee
                all_rets.append(ret)
                last_trade_index = i

        n_trades = len(all_rets)

        if n_trades < 10:
            continue

        all_rets = np.array(all_rets)

        wins = all_rets[all_rets > 0]
        losses = all_rets[all_rets <= 0]

        win_rate = len(wins) / n_trades
        total_ret = np.sum(all_rets)
        avg_ret = np.mean(all_rets)

        gross_profit = np.sum(wins)
        gross_loss = np.abs(np.sum(losses))
        pf = gross_profit / gross_loss if gross_loss > 0 else np.inf

        std_dev = np.std(all_rets)
        sharpe = (avg_ret / std_dev) if std_dev > 0 else 0

        results.append({
            'threshold': round(t, 4),
            'trades': n_trades,
            'winrate': round(win_rate, 4),
            'avg_ret': round(avg_ret, 5),
            'profit_factor': round(pf, 2),
            'sharpe': round(sharpe, 4),
            'total_acc': round(total_ret, 4)
        })

    columns = [
        'threshold', 'trades', 'winrate',
        'avg_ret', 'profit_factor', 'sharpe', 'total_acc'
    ]

    df_results = pd.DataFrame(results, columns=columns)

    if df_results.empty:
        return df_results

    return df_results.sort_values('sharpe', ascending=False).reset_index(drop=True)
