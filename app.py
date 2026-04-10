import os

import streamlit as st

from src import company_context, diagnostics, exporter, findings, prioritization, recommendations
from src.utils import load_json


st.set_page_config(page_title="DG Assessment Tool", layout="wide", page_icon="🔍")


def render_home() -> None:
    st.title("🔍 Data Governance Assessment Tool")
    st.markdown("### Herramienta de diagnóstico inicial para proyectos de gobierno del dato")
    st.write(
        "Esta aplicación simula el trabajo de discovery de un consultor de gobierno del dato "
        "cuando entra por primera vez en una compañía."
    )

    st.warning(
        "Esta herramienta corresponde a la fase de ASSESSMENT INICIAL: diagnóstico, "
        "descubrimiento y priorización. No representa el modelo objetivo final ni el roadmap definitivo."
    )

    st.divider()

    col_left, col_right = st.columns([1.2, 1])

    with col_left:
        st.markdown(
            """
            #### ¿Qué cubre este assessment?
            - Contexto empresarial y presión regulatoria.
            - Nivel actual de madurez de la gestión del dato.
            - Hallazgos operativos y organizativos observados.
            - Priorización de problemas según impacto, urgencia, riesgo y esfuerzo.
            - Síntesis ejecutiva para preparar la propuesta posterior.
            """
        )

    with col_right:
        st.markdown(
            """
            <div style="background:#f2f6fb;border-left:5px solid #1f4e79;padding:0.85rem 1rem;border-radius:0.4rem;">
                <b>Resultado esperado</b><br>
                Una base diagnóstica sólida para diseñar después:
                <br>1) Modelo Objetivo<br>
                2) Estrategia del Dato<br>
                3) Roadmap de Implantación
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.divider()

    st.markdown("#### Estructura de secciones")
    section_data = [
        ["🏢 Perfil de Empresa", "Contexto inicial: estructura, sistemas, regulación y alcance del assessment."],
        ["📊 Diagnóstico de Madurez", "Evaluación de 6 dimensiones clave con score global y visualización."],
        ["🔍 Hallazgos", "Registro de problemas detectados antes de priorizar y definir iniciativas."],
        ["⚖️ Priorización", "Ranking de problemas con fórmula ponderada y matriz visual de decisión."],
        ["📋 Resumen Ejecutivo", "Consolidación del diagnóstico y exportación del informe en Markdown."],
        ["💡 Recomendaciones", "Quick wins y líneas preliminares para preparar la fase posterior."],
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
        ],
    )

    st.divider()
    if company:
        st.markdown(f"**Empresa:** {company.get('nombre', 'N/D')}")
    else:
        st.error("No se pudo cargar data/company_profile.json")

    st.markdown(
        "<p style='font-size:0.8rem;'><i>Assessment inicial · base para propuesta de gobierno del dato</i></p>",
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
