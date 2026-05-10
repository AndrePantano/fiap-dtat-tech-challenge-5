import pandas as pd
from src.config import RAW_PATH

def run_load_data():
    df_2022 = pd.read_excel(RAW_PATH, sheet_name="PEDE2022")
    df_2023 = pd.read_excel(RAW_PATH, sheet_name="PEDE2023")
    df_2024 = pd.read_excel(RAW_PATH, sheet_name="PEDE2024")

    return df_2022, df_2023, df_2024