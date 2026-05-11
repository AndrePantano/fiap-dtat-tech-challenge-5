
import pandas as pd
from typing import Optional

from src.constants import (
    FEATURES,
    FEATURES_RESUMIDAS,
    FEATURES_INDICATORS,    
    DEFAULT_SAMPLE_SIZE,
    DEFAULT_IMPORTANCES
)

def get_feature_importances(model) -> pd.Series:
    
    try:
        importances = pd.Series(model.feature_importances_, index=FEATURES, dtype="float64")
        return importances.sort_values(ascending=False)
    except Exception:
        return DEFAULT_IMPORTANCES.sort_values(ascending=False)
    
def get_benchmarks(df: Optional[pd.DataFrame]) -> pd.DataFrame:
    
    # usado como exemplo no carregamento do app
    cols_round = [col for col in FEATURES if col not in ['fase', 'idade']]
    df_exemplo = df.loc[(df['inde_24'] > 9) & (df['fase'] > 0), FEATURES].head(1).copy()
    df_exemplo[cols_round] = df_exemplo[cols_round].round(2)        
    
    summary = pd.DataFrame({
        "media": df[FEATURES].mean(numeric_only=True),
        "mediana": df[FEATURES].median(numeric_only=True),
        "q25": df[FEATURES].quantile(0.25, numeric_only=True),        
        "exemplo":df_exemplo[FEATURES].iloc[0],
        "exemplo_resumido":df_exemplo[FEATURES_RESUMIDAS].iloc[0]
    })

    return summary


def get_year_summary(df: Optional[pd.DataFrame]) -> pd.DataFrame:

    columns = ["inde"] +  FEATURES
    return df.groupby("ano_base")[columns].mean(numeric_only=True).reindex([2022, 2023, 2024])
    

def get_year_summary_all_indicators(df: Optional[pd.DataFrame]) -> pd.DataFrame:

    columns = ["inde"] +  FEATURES_INDICATORS
    return  df.groupby("ano_base")[columns].mean(numeric_only=True).reindex([2022, 2023, 2024])
    

def get_correlations(df: Optional[pd.DataFrame]) -> pd.Series:

    corr = df[["inde"] + FEATURES_INDICATORS].corr(numeric_only=True)
    return corr["inde"].drop(labels=["inde"]).sort_values(ascending=False)
    

def get_sample_size(df: Optional[pd.DataFrame]) -> int:
    if df is None:
        return DEFAULT_SAMPLE_SIZE
    return int(df["ra"].notna().sum())


def get_institution_count(df: Optional[pd.DataFrame]) -> Optional[int]:
    return int(df['instituicao_de_ensino'].dropna().nunique())
    