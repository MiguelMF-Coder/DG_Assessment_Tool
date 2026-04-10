import pandas as pd
import plotly.express as px
import streamlit as st


def render() -> None:
    st.title("🗺️ Roadmap de Implantación")
    st.caption("Plan de despliegue por fases para ejecutar el modelo objetivo y la estrategia del dato.")
    st.success("Roadmap propuesto para los próximos 12 meses con entregables de negocio y control.")
    st.divider()

    roadmap_df = pd.DataFrame(
        [
            ["Q1", "Lanzar Data Governance Council y nombrar Data Owners", "Gobierno organizativo", "Alta", "En 90 días"],
            ["Q1", "Glosario único de KPIs omnicanal", "Metadata y definiciones", "Alta", "En 90 días"],
            ["Q2", "Piloto Data Quality Inventario (RFID/SINT)", "Calidad del dato", "Alta", "120-180 días"],
            ["Q2", "Diseño MDM Producto", "MDM", "Media-Alta", "120-180 días"],
            ["Q3", "Catálogo corporativo con linaje en dominios críticos", "Metadata y linaje", "Alta", "180-270 días"],
            ["Q3", "Pipeline ESG audit-ready para CSRD/ESRS", "ESG y compliance", "Alta", "180-270 días"],
            ["Q4", "Escalado MDM Inventario + Producto", "MDM", "Media", "270-360 días"],
            ["Q4", "Gobernanza de modelos analíticos e IA (AI Act)", "IA y riesgo", "Media", "270-360 días"],
        ],
        columns=["Fase", "Iniciativa", "Bloque", "Prioridad", "Horizonte"],
    )

    st.subheader("Plan por fases")
    st.dataframe(roadmap_df, use_container_width=True, hide_index=True)

    st.divider()

    st.subheader("Vista visual del roadmap")
    phase_order = {"Q1": 1, "Q2": 2, "Q3": 3, "Q4": 4}
    priority_size = {"Alta": 28, "Media-Alta": 22, "Media": 18}

    chart_df = roadmap_df.copy()
    chart_df["fase_num"] = chart_df["Fase"].map(phase_order)
    chart_df["size"] = chart_df["Prioridad"].map(priority_size)

    fig = px.scatter(
        chart_df,
        x="fase_num",
        y="Bloque",
        size="size",
        color="Prioridad",
        text="Iniciativa",
        color_discrete_map={"Alta": "#c0392b", "Media-Alta": "#f39c12", "Media": "#1f4e79"},
        title="Roadmap por trimestre y bloque",
    )
    fig.update_traces(textposition="top center")
    fig.update_layout(
        xaxis=dict(tickmode="array", tickvals=[1, 2, 3, 4], ticktext=["Q1", "Q2", "Q3", "Q4"], range=[0.7, 4.3]),
        yaxis_title="Bloque de trabajo",
    )
    st.plotly_chart(fig, use_container_width=True)

    st.divider()

    st.subheader("Hitos de control")
    st.markdown("1. Comité activo, RACI aprobado y dominios asignados (fin Q1).")
    st.markdown("2. KPI dictionary corporativo aprobado por negocio y dato (fin Q1).")
    st.markdown("3. Scorecard de calidad inventario operativo y revisado mensual (fin Q2).")
    st.markdown("4. Catálogo + linaje activos para datasets críticos (fin Q3).")
    st.markdown("5. Cierre anual con trazabilidad ESG audit-ready y marco AI Act definido (fin Q4).")
