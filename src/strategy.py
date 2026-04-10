import pandas as pd
import streamlit as st


def render() -> None:
    st.title("🎯 Estrategia del Dato")
    st.caption("Marco estratégico para ejecutar el modelo objetivo de gobierno del dato en Inditex.")
    st.success("Estrategia definida como puente entre assessment cerrado y ejecución del roadmap.")
    st.divider()

    st.subheader("Objetivos estratégicos (12-18 meses)")
    objectives = [
        "Formalizar el gobierno por dominios con ownership y toma de decisiones trazable.",
        "Industrializar calidad de dato en Inventario, Producto, Proveedores/ESG y Cliente.",
        "Reducir riesgo regulatorio mediante controles operativos de privacidad y reporting ESG.",
        "Acelerar analítica confiable con catálogo, glosario y linaje corporativo.",
    ]
    for item in objectives:
        st.markdown(f"- {item}")

    st.divider()

    st.subheader("Líneas estratégicas")
    strategy_df = pd.DataFrame(
        [
            ["Gobierno organizativo", "Council + Data Office + RACI por dominio", "Comité mensual, decisiones priorizadas y actas"],
            ["Data Quality", "Reglas y scorecards por dominio crítico", "Reducción de incidencias y mayor confiabilidad KPI"],
            ["MDM", "Modelo maestro de Producto e Inventario", "Unicidad y consistencia cross-enseña"],
            ["Metadata", "Catálogo, glosario y linaje", "Reutilización de datos y trazabilidad end-to-end"],
            ["Compliance by design", "Controles RGPD/AI Act/CSRD en ciclo de vida del dato", "Menor exposición legal y reputacional"],
        ],
        columns=["Línea", "Iniciativa núcleo", "Resultado esperado"],
    )
    st.dataframe(strategy_df, use_container_width=True, hide_index=True)

    st.divider()

    st.subheader("KPIs de éxito de la estrategia")
    kpi1, kpi2, kpi3, kpi4 = st.columns(4)
    kpi1.metric("Cobertura de dominios con Owner", "100%", "objetivo")
    kpi2.metric("KPIs críticos con definición única", ">90%", "objetivo")
    kpi3.metric("Datasets críticos con linaje", ">80%", "objetivo")
    kpi4.metric("Incidencias de calidad en inventario", "-40%", "objetivo")

    st.divider()

    st.warning(
        "Gobernar primero y escalar después: la estrategia prioriza claridad organizativa y control "
        "antes de ampliar complejidad tecnológica."
    )
