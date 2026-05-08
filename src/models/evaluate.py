import pandas as pd
import joblib
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path
from sklearn.metrics import (classification_report, roc_curve, roc_auc_score)
from sklearn.model_selection import train_test_split

# Caminhos
BASE_DIR = Path(__file__).resolve().parents[2]
DATA_FILE = BASE_DIR / "data" / "processed" / "ml_dataset.csv"
MODEL_FILE = BASE_DIR / "models" / "modelo_risco_passos_magicos.pkl"

# Carregando dados
df_ml = pd.read_csv(DATA_FILE, sep=";")

features = ['ida', 'ieg', 'ips', 'ipp', 'iaa']

X = df_ml[features]
y = df_ml['risco_futuro']

# Mesmo split do treino
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

# Carregando modelo
model = joblib.load(MODEL_FILE)

# Avaliação
y_prob = model.predict_proba(X_test)[:, 1]
auc = roc_auc_score(y_test, y_prob)
fpr, tpr, _ = roc_curve(y_test, y_prob)

# Plot
plt.figure(figsize=(10, 6))
sns.set_theme(style="whitegrid")
plt.plot(fpr,tpr,label=f'Modelo Final (AUC = {auc:.2f})')
plt.plot([0, 1], [0, 1], 'k--')
plt.title('Curva ROC')
plt.xlabel('FPR')
plt.ylabel('TPR')
plt.legend()
plt.show()

# Relatório
print(classification_report(y_test, model.predict(X_test)))