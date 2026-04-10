import os

import plotly.express as px
import streamlit as st

from src.utils import load_csv


def _priority_score(row) -> float:
    return (row["impacto"] * 0.35) + (row["urgencia"] * 0.35) + (row["riesgo"] * 0.20) - (row["esfuerzo"] * 0.10)


def _top3_style(row) -> list[str]:
    if row["rank"] <= 3:
        return ["background-color: #d9f2d9"] * len(row)
    return [""] * len(row)


def render() -> None:
    data_path = os.path.join(os.path.dirname(__file__), "..", "data", "problems_sample.csv")
    df = load_csv(data_path)

    st.title("⚖️ Priorización")
    st.caption("Ordenación de hallazgos por valor de negocio, urgencia, riesgo y esfuerzo estimado.")
    st.divider()

    if df.empty:
        st.error("No se pudo cargar data/problems_sample.csv")
        return

    df = df.copy()
    df["score"] = df.apply(_priority_score, axis=1).round(2)
    df = df.sort_values("score", ascending=False).reset_index(drop=True)
    df["rank"] = df.index + 1

    st.subheader("Fórmula de priorización")
    st.code("score = (impacto*0.35) + (urgencia*0.35) + (riesgo*0.20) - (esfuerzo*0.10)", language="python")

    st.divider()

    st.subheader("Top 3 problemas")
    top3 = df.head(3)
    cols = st.columns(3)
    for idx, (_, row) in enumerate(top3.iterrows()):
        cols[idx].metric(f"#{row['rank']} {row['titulo']}", f"{row['score']}")

    st.divider()

    st.subheader("Tabla de ranking completo")
    rank_cols = ["rank", "titulo", "score", "impacto", "urgencia", "esfuerzo", "riesgo", "area_afectada", "dominio_dato"]
    styled = df[rank_cols].style.apply(_top3_style, axis=1)
    st.dataframe(styled, use_container_width=True, hide_index=True)

    st.divider()

    scatter = px.scatter(
        df,
        x="urgencia",
        y="impacto",
        size="riesgo",
        color="score",
        text="titulo",
        title="Matriz de Priorización",
        color_continuous_scale="Blues",
        size_max=40,
    )
    scatter.update_traces(textposition="top center")
    scatter.add_shape(type="line", x0=2.5, x1=2.5, y0=1, y1=5, line=dict(dash="dash", color="gray"))
    scatter.add_shape(type="line", x0=1, x1=5, y0=2.5, y1=2.5, line=dict(dash="dash", color="gray"))

    scatter.add_annotation(x=3.75, y=4.6, text="CRÍTICO", showarrow=False)
    scatter.add_annotation(x=1.5, y=4.6, text="IMPORTANTE", showarrow=False)
    scatter.add_annotation(x=3.75, y=1.4, text="MONITOREAR", showarrow=False)
    scatter.add_annotation(x=1.5, y=1.4, text="DIFERIR", showarrow=False)

    scatter.update_layout(xaxis_range=[1, 5], yaxis_range=[1, 5])
    st.plotly_chart(scatter, use_container_width=True)

    st.caption(
        "La fórmula pondera impacto y urgencia como variables principales, considera riesgo regulatorio "
        "y descuenta esfuerzo para favorecer iniciativas de alto valor con ejecución viable."
    )
