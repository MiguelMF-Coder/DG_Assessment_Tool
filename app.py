import os

import streamlit as st

from src import (
    company_context,
    diagnostics,
    exporter,
    findings,
    prioritization,
    recommendations,
    roadmap,
    steering_committee,
    strategy,
    target_model,
)
from src.utils import load_json


st.set_page_config(page_title="DG Assessment Tool", layout="wide", page_icon="🔍")


def render_home() -> None:
    st.title("🔍 Data Governance Assessment Tool")
    st.markdown("### Assessment inicial completado de Data Governance — Caso Inditex")
    st.write(
        "Esta aplicación representa el entregable completo de discovery y diagnóstico "
        "de un consultor de gobierno del dato en su entrada en la compañía."
    )

    st.success(
        "Estado actual: assessment inicial finalizado y consolidado. "
        "La base está lista para diseñar Modelo Objetivo, Estrategia del Dato y Roadmap."
    )

    st.divider()

    kpi1, kpi2, kpi3, kpi4 = st.columns(4)
    kpi1.metric("Tiendas FY2025", "5.460")
    kpi2.metric("Ventas FY2025", "€39,864bn")
    kpi3.metric("Ventas online FY2025", "€10,7bn")
    kpi4.metric("Mercados", "214")

    st.divider()

    col_left, col_right = st.columns([1.2, 1])

    with col_left:
        st.markdown(
            """
            #### ¿Qué cubre este assessment?
            - Contexto empresarial y presión regulatoria ya validados.
            - Nivel actual de madurez de la gestión del dato consolidado.
            - Hallazgos operativos y organizativos documentados.
            - Priorización cerrada según impacto, urgencia, riesgo y esfuerzo.
            - Síntesis ejecutiva preparada para arrancar la fase de propuesta.
            """
        )

    with col_right:
        st.markdown(
            """
            <div style="background:#f2f6fb;border-left:5px solid #1f4e79;padding:0.85rem 1rem;border-radius:0.4rem;">
                <b>Resultado esperado</b><br>
                Este entregable ya deja preparada la transición hacia:
                <br>1) Modelo Objetivo<br>
                2) Estrategia del Dato<br>
                3) Roadmap de Implantación
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.divider()

    st.markdown("#### Estado del trabajo consultivo")
    st.markdown("- ✅ Contexto y alcance del assessment cerrados")
    st.markdown("- ✅ Diagnóstico de madurez consolidado")
    st.markdown("- ✅ Hallazgos y priorización validados")
    st.markdown("- ✅ Recomendaciones iniciales listas para fase siguiente")

    st.divider()

    st.markdown("#### Estructura de secciones")
    section_data = [
        ["🏢 Perfil de Empresa", "Contexto inicial: estructura, sistemas, regulación y alcance del assessment."],
        ["📊 Diagnóstico de Madurez", "Evaluación de 6 dimensiones clave con score global y visualización."],
        ["🔍 Hallazgos", "Registro de problemas detectados y documentados durante el assessment."],
        ["⚖️ Priorización", "Ranking de problemas con fórmula ponderada y matriz visual de decisión."],
        ["📋 Resumen Ejecutivo", "Consolidación del diagnóstico y exportación del informe en Markdown."],
        ["💡 Recomendaciones", "Quick wins y líneas de actuación derivadas del assessment."],
        ["🧭 Modelo Objetivo", "Diseño de gobierno del dato objetivo por capacidades y roles."],
        ["🎯 Estrategia del Dato", "Marco estratégico de ejecución con iniciativas núcleo y KPIs."],
        ["🗺️ Roadmap", "Plan trimestral de implantación con hitos de control y prioridades."],
        ["🏛️ Comité de Dirección", "Decisión ejecutiva, presupuesto y riesgos para activar la implantación."],
    ]
    st.table(section_data)


company_path = os.path.join(os.path.dirname(__file__), "data", "company_profile.json")
company = load_json(company_path)

with st.sidebar:
    st.markdown("## Navegación")
    page = st.radio(
        "Ir a sección",
        [
            "🏠 Home",
            "🏢 Perfil de Empresa",
            "📊 Diagnóstico de Madurez",
            "🔍 Hallazgos",
            "⚖️ Priorización",
            "📋 Resumen Ejecutivo",
            "💡 Recomendaciones",
            "🧭 Modelo Objetivo",
            "🎯 Estrategia del Dato",
            "🗺️ Roadmap",
            "🏛️ Comité de Dirección",
        ],
    )

    st.divider()
    if company:
        st.markdown(f"**Empresa:** {company.get('nombre', 'N/D')}")
    else:
        st.error("No se pudo cargar data/company_profile.json")

    st.markdown(
        "<p style='font-size:0.8rem;'><i>Assessment inicial completado · base para propuesta de gobierno del dato</i></p>",
        unsafe_allow_html=True,
    )

if page == "🏠 Home":
    render_home()
elif page == "🏢 Perfil de Empresa":
    company_context.render()
elif page == "📊 Diagnóstico de Madurez":
    diagnostics.render()
elif page == "🔍 Hallazgos":
    findings.render()
elif page == "⚖️ Priorización":
    prioritization.render()
elif page == "📋 Resumen Ejecutivo":
    exporter.render()
elif page == "💡 Recomendaciones":
    recommendations.render()
elif page == "🧭 Modelo Objetivo":
    target_model.render()
elif page == "🎯 Estrategia del Dato":
    strategy.render()
elif page == "🗺️ Roadmap":
    roadmap.render()
elif page == "🏛️ Comité de Dirección":
    steering_committee.render()
