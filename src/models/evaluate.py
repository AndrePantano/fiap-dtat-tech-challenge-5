import pandas as pd
import joblib
import matplotlib.pyplot as plt
import seaborn as sns
import json
from sklearn.metrics import (classification_report, roc_curve, roc_auc_score)
from sklearn.model_selection import train_test_split
from src.config import ML_DATASET_FILE, MODEL_FILE, METRICS_FILE, REPORTS_DIR
from src.constants import FEATURES

def run_evaluate():
    # Carregando dados
    df_ml = pd.read_csv(ML_DATASET_FILE, sep=";")

    X = df_ml[FEATURES]
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

    # Salvar Gráfico
    print("4.1 Gerando o gráfico da curva AUC.")
    plt.figure(figsize=(10, 6))
    sns.set_theme(style="whitegrid")
    plt.plot(fpr,tpr,label=f'Modelo Final (AUC = {auc:.2f})')
    plt.plot([0, 1], [0, 1], 'k--')
    plt.title('Curva ROC')
    plt.xlabel('FPR')
    plt.ylabel('TPR')
    plt.legend()
    plt.savefig(REPORTS_DIR / "roc_curve.png", dpi=300, bbox_inches="tight")
    plt.close()

    # Relatório
    print("4.2 Gerando o arquivo JSON do Classification Report")
    
    report = classification_report(y_test, model.predict(X_test), output_dict=True) 
    
    # adiciona metadados
    report["model_name"] = model.__class__.__name__
    report["auc_score"] = auc

    with open(METRICS_FILE, "w", encoding="utf-8") as f:
        json.dump(report, f, indent=4)


# executa o script
if __name__ == "__main__":
    run_evaluate()