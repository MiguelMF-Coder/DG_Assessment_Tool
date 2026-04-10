import os

import streamlit as st

from src.utils import badge, load_json


def render() -> None:
    data_path = os.path.join(os.path.dirname(__file__), "..", "data", "assessment_notes.json")
    notes = load_json(data_path)

    st.title("💡 Recomendaciones")
    st.caption("Síntesis preliminar de acciones sugeridas a partir del assessment inicial.")
    st.warning(
        "Estas recomendaciones son preliminares. La propuesta de modelo objetivo, "
        "estrategia y roadmap se desarrolla en la fase posterior del proyecto."
    )
    st.divider()

    if not notes:
        st.error("No se pudo cargar data/assessment_notes.json")
        return

    st.subheader("⚡ Quick Wins")
    for item in notes.get("quick_wins", []):
        st.success(item)

    st.divider()

    st.subheader("🔍 Áreas a Profundizar")
    for item in notes.get("areas_profundizar", []):
        st.markdown(f"- {item}")

    st.divider()

    st.subheader("📌 Líneas de Actuación")
    for idx, item in enumerate(notes.get("lineas_actuacion", []), start=1):
        st.markdown(f"{idx}. {item}")

    st.divider()

    st.subheader("🎯 Dominios Prioritarios")
    dominios = notes.get("dominios_prioritarios", [])
    if dominios:
        badges = "".join([badge(domain, "#1f4e79") for domain in dominios])
        st.markdown(badges, unsafe_allow_html=True)
    else:
        st.write("Sin dominios definidos.")

    st.divider()

    st.subheader("📝 Notas Clave del Consultor")
    for item in notes.get("notas_clave", []):
        st.markdown(f"- **{item}**")

    st.divider()

    st.markdown(
        """
        <style>
            div[data-testid="stAlert"][kind="info"] {
                border: 1px solid #1f2937;
            }
        </style>
        """,
        unsafe_allow_html=True,
    )
    st.subheader("Conclusión General")
    st.info(notes.get("conclusion_general", "Sin conclusión disponible."))
