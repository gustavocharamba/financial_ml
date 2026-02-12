import pandas as pd
import numpy as np

def get_feature_importance(model, X):
    booster = model.get_booster()
    scores = booster.get_score(importance_type='gain')

    fmap = {f"f{i}": col for i, col in enumerate(X.columns)}

    fi = pd.DataFrame({
        'Feature': [fmap.get(k, k) for k in scores.keys()],
        'Importance': scores.values()
    })

    fi = fi.sort_values(by='Importance', ascending=False).reset_index(drop=True)
    return fi

