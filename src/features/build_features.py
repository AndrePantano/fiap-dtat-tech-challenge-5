# Feature Engineering

# Importando as Bibliotecas
import pandas as pd
from src.config import DATA_PATH, PROCESSED_DATA_DIR, ML_DATASET_FILE
from src.constants import FEATURES

def run_build_features():

    # Importando o dataset
    df_completo = pd.read_csv(DATA_PATH, sep=";")

    # A escolha da lógica
    # Vamos usar a lógica longitudinal da Pergunta 5. 
    df_ml = df_completo.sort_values(by=['ra', 'ano_base']).copy()
    
    # O "Target" (Alvo) será 1 (Risco) se a defasagem no ano seguinte for maior que 0
    df_ml['defasagem_futura'] = df_ml.groupby('ra')['defasagem'].shift(-1)
    df_ml['risco_futuro'] = df_ml['defasagem_futura'].apply(lambda x: 1 if x > 0 else 0)

    # Selecionando as features (indicadores do ano atual) e removendo nulos
    df_ml = df_ml.dropna(subset=FEATURES + ['risco_futuro'])

    # Criando o dataset para o modelo
    PROCESSED_DATA_DIR.mkdir(parents=True, exist_ok=True)

    df_ml.to_csv(ML_DATASET_FILE, sep=";", index=False)

# executa o script
if __name__ == "__main__":
    run_build_features()