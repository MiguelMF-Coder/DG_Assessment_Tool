import os

import streamlit as st

from src.utils import badge, load_json


def render() -> None:
    data_path = os.path.join(os.path.dirname(__file__), "..", "data", "company_profile.json")
    company = load_json(data_path)

    st.title("🏢 Perfil de Empresa")
    st.caption("Contexto organizativo y operativo para enmarcar el assessment inicial.")
    st.info("Este perfil contextualiza el assessment antes de evaluar la madurez.")
    st.divider()

    if not company:
        st.error("No se pudo cargar data/company_profile.json")
        return

    col_left, col_right = st.columns(2)

    with col_left:
        st.markdown(f"## {company.get('nombre', 'N/D')}")
        st.write(f"**Sector:** {company.get('sector', 'N/D')}")
        st.write(f"**Tamaño:** {company.get('tamaño', 'N/D')}")
        st.write(f"**Presencia geográfica:** {company.get('presencia_geografica', 'N/D')}")
        st.write(f"**Fecha del assessment:** {company.get('fecha', 'N/D')}")
        st.write(f"**Consultor / proyecto:** {company.get('consultor', 'N/D')}")
        st.write(f"**Tiendas FY2025:** {company.get('unidades_comerciales', 'N/D')}")
        st.write(f"**Ventas FY2025:** {company.get('ventas_fy2025', 'N/D')}")
        st.write(f"**Ventas online FY2025:** {company.get('ventas_online_fy2025', 'N/D')}")
        st.write(f"**Mercados:** {company.get('mercados', 'N/D')}")

    with col_right:
        st.write(f"**Nivel de digitalización:** {company.get('nivel_digitalizacion', 'N/D')}")
        st.write(f"**Presión regulatoria:** {company.get('presion_regulatoria', 'N/D')}")
        st.write(f"**Contexto del assessment:** {company.get('contexto_assessment', 'N/D')}")

    st.divider()

    sistemas = company.get("sistemas_relevantes", [])
    st.subheader("Sistemas relevantes")
    if isinstance(sistemas, list) and sistemas:
        code_tags = " ".join([f"`{sistema}`" for sistema in sistemas])
        st.markdown(code_tags)
    else:
        st.write("Sin información de sistemas relevantes.")

    st.divider()

    st.subheader("Señales de arquitectura y dato")
    st.markdown("- Integración omnicanal con RFID y SINT como base operativa.")
    st.markdown("- Arquitectura digital modular con Inditex Open Platform y event bus.")
    st.markdown("- Capacidades de Big Data, cloud, reporting ESG y control corporativo.")

    st.divider()

    areas = company.get("areas_negocio", [])
    st.subheader("Áreas de negocio")
    if isinstance(areas, list) and areas:
        badges = "".join([badge(area, "#1f4e79") for area in areas])
        st.markdown(badges, unsafe_allow_html=True)
    else:
        st.write("Sin áreas de negocio definidas.")
