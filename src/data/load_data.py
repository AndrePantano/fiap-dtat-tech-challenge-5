from pathlib import Path
import pandas as pd

# raiz do projeto
BASE_DIR = Path(__file__).resolve().parents[2]

ARQUIVO = BASE_DIR / "data" / "raw" / "BASE DE DADOS PEDE 2024 - DATATHON.xlsx"

def carregar_dados():
    df_2022 = pd.read_excel(ARQUIVO, sheet_name="PEDE2022")
    df_2023 = pd.read_excel(ARQUIVO, sheet_name="PEDE2023")
    df_2024 = pd.read_excel(ARQUIVO, sheet_name="PEDE2024")

    return df_2022, df_2023, df_2024