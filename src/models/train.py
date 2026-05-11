# Construção do Modelo

# Importando as Bibliotecas
import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from src.config import ML_DATASET_FILE, MODELS_DIR, MODEL_FILE
from src.constants import FEATURES

def run_train_model():

    # Importando o dataset
    df_ml = pd.read_csv(ML_DATASET_FILE, sep=";")

    # Definindo o X e y
    X = df_ml[FEATURES]
    y = df_ml['risco_futuro']

    # Separação em Treino e Teste (80% treino, 20% teste)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

    # Modelo 1: Regressão Logística
    log_reg = LogisticRegression(random_state=42, class_weight='balanced')
    log_reg.fit(X_train, y_train)

    # Criação do Modelo Treinado
    MODELS_DIR.mkdir(parents=True, exist_ok=True)
    joblib.dump(log_reg, MODEL_FILE)

# executa o script
if __name__ == "__main__":
    run_train_model()