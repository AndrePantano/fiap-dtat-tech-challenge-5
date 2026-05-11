import joblib
import pandas as pd
from typing import Tuple
from pathlib import Path
from src.config import MODEL_FILE
from src.constants import FEATURES

# Carregando modelo
model = joblib.load(MODEL_FILE)

# Função de predição
def predict_risk(model, input_series: pd.Series) -> Tuple[int, float]:

    payload = pd.DataFrame(
        [[input_series[feature] for feature in FEATURES]],
        columns=FEATURES
    )

    prediction  = int(model.predict(payload)[0])       
    probability = float(model.predict_proba(payload)[0][1])

    return prediction, probability