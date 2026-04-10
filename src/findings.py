import os

import pandas as pd
import streamlit as st

from src.utils import load_csv, score_color


def _highlight_scores(value: float) -> str:
    try:
        value = float(value)
    except (TypeError, ValueError):
        return ""

    if value <= 2:
        return "background-color: #f8d7da"
    if value <= 3:
        return "background-color: #fff3cd"
    return "background-color: #d4edda"


def render() -> None:
    data_path = os.path.join(os.path.dirname(__file__), "..", "data", "problems_sample.csv")
    problems_df = load_csv(data_path)

    st.title("🔍 Hallazgos")
    st.caption("Registro de hallazgos en bruto levantados en entrevistas y análisis documental.")
    st.info("Los hallazgos se registran aquí antes de ser priorizados.")
    st.divider()

    if problems_df.empty:
        st.error("No se pudo cargar data/problems_sample.csv")
        return

    score_cols = ["impacto", "urgencia", "riesgo"]
    summary_cols = ["titulo", "area_afectada", "dominio_dato", "impacto", "urgencia", "riesgo"]

    st.subheader("Resumen de hallazgos")
    styled = problems_df[summary_cols].style.applymap(_highlight_scores, subset=score_cols)
    st.dataframe(styled, use_container_width=True, hide_index=True)

    st.divider()

    for _, row in problems_df.iterrows():
        with st.expander(row["titulo"]):
            col_left, col_right = st.columns([2, 1])

            with col_left:
                st.write(f"**Descripción:** {row['descripcion']}")
                st.write(f"**Origen:** {row['origen']}")
                st.write(f"**Área afectada:** {row['area_afectada']}")
                st.write(f"**Impacto en negocio:** {row['impacto_negocio']}")
                st.write(f"**Dominio de dato:** {row['dominio_dato']}")
                st.write(f"**Calidad del dato:** {row['calidad_dato']}")
                st.write(f"**Observación del consultor:** {row['observacion_consultor']}")

            with col_right:
                st.metric("Impacto", f"{row['impacto']}/5", delta=score_color(row["impacto"]))
                st.metric("Urgencia", f"{row['urgencia']}/5", delta=score_color(row["urgencia"]))
                st.metric("Esfuerzo", f"{row['esfuerzo']}/5", delta=score_color(row["esfuerzo"]))
                st.metric("Riesgo", f"{row['riesgo']}/5", delta=score_color(row["riesgo"]))
