import pandas as pd
import streamlit as st


def render() -> None:
    st.title("🧭 Modelo Objetivo")
    st.caption("Diseño objetivo de gobierno del dato para escalar el modelo omnicanal de Inditex.")
    st.success("Esta sección traduce el diagnóstico en un modelo operativo objetivo de referencia.")
    st.divider()

    st.subheader("Principios del modelo")
    principles = [
        "Gobierno federado por dominios con estándares corporativos comunes.",
        "Ownership explícito del dato con responsabilidad ejecutiva en negocio.",
        "Datos como producto: calidad, trazabilidad y reutilización por diseño.",
        "Cumplimiento regulatorio integrado en procesos operativos y analíticos.",
    ]
    for item in principles:
        st.markdown(f"- {item}")

    st.divider()

    st.subheader("Capacidades objetivo")
    capabilities = pd.DataFrame(
        [
            ["Gobierno organizativo", "Data Governance Council + Oficina del Dato + Data Owners/Stewards", "Alto"],
            ["Gestión de dominios", "Inventario, Producto, Proveedores/ESG y Cliente con ownership formal", "Alto"],
            ["Calidad del dato", "Reglas, scorecards y observabilidad para dominios críticos", "Muy alto"],
            ["Metadata y linaje", "Catálogo corporativo, glosario y trazabilidad de KPIs", "Muy alto"],
            ["Privacidad y cumplimiento", "Controles RGPD/AI Act/CSRD embebidos en pipelines", "Alto"],
            ["MDM", "Golden records para Producto e Inventario", "Alto"],
        ],
        columns=["Capacidad", "Diseño objetivo", "Prioridad"],
    )
    st.dataframe(capabilities, use_container_width=True, hide_index=True)

    st.divider()

    st.subheader("Estructura de roles objetivo")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("**Nivel corporativo**")
        st.markdown("- Data Governance Council")
        st.markdown("- Oficina del Dato (Data Office)")
        st.markdown("- Arquitectura de datos y seguridad")
    with col2:
        st.markdown("**Nivel dominio**")
        st.markdown("- Data Owner por dominio")
        st.markdown("- Data Steward por proceso crítico")
        st.markdown("- Product Owner analítico por caso de uso")

    st.divider()

    st.info(
        "Resultado esperado del modelo objetivo: decisiones de negocio consistentes, "
        "reducción de riesgo regulatorio y escalabilidad analítica con control."
    )
