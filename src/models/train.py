# Construção do Modelo

# Importando as Bibliotecas
import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from pathlib import Path

# raiz do projeto
BASE_DIR = Path(__file__).resolve().parents[2]
ARQUIVO = BASE_DIR / "data" / "processed" / "ml_dataset.csv"

# Importando o dataset
df_ml = pd.read_csv(ARQUIVO, sep=";")

# Definindo as Features, X e y
features = ['ida', 'ieg', 'ips', 'ipp', 'iaa']
X = df_ml[features]
y = df_ml['risco_futuro']

# Separação em Treino e Teste (80% treino, 20% teste)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

# Modelo 1: Regressão Logística
log_reg = LogisticRegression(random_state=42, class_weight='balanced')
log_reg.fit(X_train, y_train)

# Criação do Modelo Treinado
OUTPUT_DIR = BASE_DIR / "models"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
OUTPUT_FILE = OUTPUT_DIR / "modelo_risco_passos_magicos.pkl"

joblib.dump(log_reg, OUTPUT_FILE)

print("Modelo salvo com sucesso na sua máquina!")
