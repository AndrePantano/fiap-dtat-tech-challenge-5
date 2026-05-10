
import pandas as pd
from typing import Optional

from src.constants import (
    FEATURES,
    DEFAULT_BENCHMARKS,
    DEFAULT_CORRELATIONS,
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
    
    summary = pd.DataFrame(
        {
            "media": df[FEATURES].mean(numeric_only=True),
            "mediana": df[FEATURES].median(numeric_only=True),
            "q25": df[FEATURES].quantile(0.25, numeric_only=True),
        }
    )

    return summary


def get_year_summary(df: Optional[pd.DataFrame]) -> pd.DataFrame:

    columns = ["inde"] +  FEATURES
    summary = df.groupby("ano_base")[columns].mean(numeric_only=True).reindex([2022, 2023, 2024])
    return summary


def get_correlations(df: Optional[pd.DataFrame]) -> pd.Series:
    if df is None:
        return DEFAULT_CORRELATIONS.copy()

    corr = df[["INDE"] + FEATURES].corr(numeric_only=True)
    series = corr["INDE"].drop(labels=["INDE"]).sort_values(ascending=False)
    return series.fillna(DEFAULT_CORRELATIONS)


def get_sample_size(df: Optional[pd.DataFrame]) -> int:
    if df is None:
        return DEFAULT_SAMPLE_SIZE
    return int(df["ra"].notna().sum())


def get_institution_count(df: Optional[pd.DataFrame]) -> Optional[int]:
    return int(df['instituicao_de_ensino'].dropna().nunique())
    