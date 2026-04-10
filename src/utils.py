import json
from typing import Any

import pandas as pd


def load_json(path: str) -> dict[str, Any]:
    """Carga un archivo JSON y devuelve un diccionario vacio en caso de error."""
    try:
        with open(path, "r", encoding="utf-8") as file:
            data = json.load(file)
            if isinstance(data, dict):
                return data
            return {}
    except (FileNotFoundError, json.JSONDecodeError, OSError):
        return {}


def load_csv(path: str) -> pd.DataFrame:
    """Carga un CSV y devuelve DataFrame vacio en caso de error."""
    try:
        return pd.read_csv(path)
    except (FileNotFoundError, pd.errors.EmptyDataError, pd.errors.ParserError, OSError):
        return pd.DataFrame()


def score_color(score: float) -> str:
    if score <= 2:
        return "🔴"
    if score <= 3:
        return "🟡"
    return "🟢"


def maturity_level(score: float) -> tuple[str, str]:
    if 1.0 <= score <= 2.0:
        return ("Inicial", "Sin gestion formal del dato")
    if 2.0 < score <= 3.0:
        return ("Reactivo", "Gestion puntual y no estructurada")
    if 3.0 < score <= 4.0:
        return ("Definido", "Procesos basicos establecidos")
    return ("Optimizado", "Gobierno del dato maduro")


def badge(text: str, color: str) -> str:
    return (
        f"<span style='display:inline-block;padding:0.2rem 0.55rem;"
        f"border-radius:999px;background:{color};color:white;"
        f"font-size:0.85rem;margin-right:0.35rem;margin-bottom:0.25rem;'>{text}</span>"
    )
