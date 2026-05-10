import pandas as pd
from typing import List


def format_decimal(value: float, digits: int = 2) -> str:
    if pd.isna(value):
        return "-"
    return f"{value:.{digits}f}".replace(".", ",")


def format_pct(value: float, digits: int = 1) -> str:
    if pd.isna(value):
        return "-"
    return f"{value * 100:.{digits}f}%".replace(".", ",")


def format_int(value: int) -> str:
    return f"{value:,}".replace(",", ".")


def join_labels(items: List[str]) -> str:
    if not items:
        return ""
    if len(items) == 1:
        return items[0]
    return f"{', '.join(items[:-1])} e {items[-1]}"
