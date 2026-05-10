import joblib
import pandas as pd
from typing import Tuple
from pathlib import Path

# Caminhos
BASE_DIR = Path(__file__).resolve().parents[2]
MODEL_FILE = BASE_DIR / "models" / "modelo_risco_passos_magicos.pkl"

FEATURES = ['ida', 'ieg', 'ips', 'ipp', 'iaa']

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