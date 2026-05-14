from pathlib import Path

BASE_DIR           = Path(__file__).resolve().parents[1]

DATA_DIR           = BASE_DIR / "data"

RAW_DATA_DIR       = DATA_DIR / "raw"
INTERIM_DATA_DIR   = DATA_DIR / "interim"
PROCESSED_DATA_DIR = DATA_DIR / "processed"

MODELS_DIR         = BASE_DIR / "models"

REPORTS_DIR        = BASE_DIR / "reports"

APP_DIR            = BASE_DIR / "app"
STYLE_DIR          = APP_DIR / "styles"

RAW_PATH           = RAW_DATA_DIR / "BASE DE DADOS PEDE 2024 - DATATHON.xlsx"
DATA_PATH          = INTERIM_DATA_DIR / "pede_interim.csv"
ML_DATASET_FILE    = PROCESSED_DATA_DIR / "ml_dataset.csv"
MODEL_FILE         = MODELS_DIR / "modelo_risco_passos_magicos.pkl"

METRICS_FILE       = REPORTS_DIR / "metrics.json"