# Feature Engineering

# Importando as Bibliotecas
import pandas as pd
from pathlib import Path

# raiz do projeto
BASE_DIR = Path(__file__).resolve().parents[2]

ARQUIVO = BASE_DIR / "data" / "interim" / "pede_interim.csv"

# Importando o dataset
df_completo = pd.read_csv(ARQUIVO, sep=";")

# A escolha da lógica
# Vamos usar a lógica longitudinal da Pergunta 5. 
df_ml = df_completo.sort_values(by=['ra', 'ano_base']).copy()

# O Target
# O "Target" (Alvo) será 1 (Risco) se a defasagem no ano seguinte for maior que 0
df_ml['defasagem_futura'] = df_ml.groupby('ra')['defasagem'].shift(-1)
df_ml['risco_futuro'] = df_ml['defasagem_futura'].apply(lambda x: 1 if x > 0 else 0)

# As Features
# Selecionando as features (indicadores do ano atual) e removendo nulos
features = ['ida', 'ieg', 'ips', 'ipp', 'iaa']
df_ml = df_ml.dropna(subset=features + ['risco_futuro'])

# Criando o dataset para o modelo
OUTPUT_DIR = BASE_DIR / "data" / "processed"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

OUTPUT_FILE = OUTPUT_DIR / "ml_dataset.csv"

df_completo.to_csv(
    OUTPUT_FILE,
    sep=";",
    index=False
)