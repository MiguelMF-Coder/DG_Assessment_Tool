import json
import os

import plotly.graph_objects as go
import streamlit as st

from src.utils import badge, load_json, maturity_level


def render() -> None:
    data_path = os.path.join(os.path.dirname(__file__), "..", "data", "maturity_sample.json")
    maturity = load_json(data_path)

    st.title("📊 Diagnóstico de Madurez")
    st.caption("Resultado consolidado de la evaluación del estado actual de la gestión del dato.")
    st.info("Diagnóstico base ya cerrado para Inditex. Puedes activar simulación para explorar escenarios.")
    st.divider()

    if not maturity:
        st.error("No se pudo cargar data/maturity_sample.json")
        return

    dimensions = {
        "estrategia_dato": "Estrategia del Dato",
        "organizacion_roles": "Organización y Roles",
        "calidad_dato": "Calidad del Dato",
        "uso_negocio": "Uso en Negocio",
        "tecnologia_arquitectura": "Tecnología y Arquitectura",
        "gobierno_control": "Gobierno y Control",
    }

    scores: dict[str, float] = {}
    simulate_mode = st.toggle("Activar simulación de escenarios", value=False)

    st.subheader("Puntuación por dimensión")
    for key, label in dimensions.items():
        default = float(maturity.get(key, {}).get("score", 1))
        if simulate_mode:
            scores[key] = st.slider(label, 1.0, 5.0, default, 0.5)
        else:
            scores[key] = default
            st.write(f"**{label}:** {default}/5")

    st.divider()

    mean_score = round(sum(scores.values()) / len(scores), 2)
    target = 4.0
    delta = round(mean_score - target, 2)

    level_name, level_desc = maturity_level(mean_score)

    metric_col, level_col = st.columns([1, 2])
    with metric_col:
        st.metric("Score global", f"{mean_score}/5", delta=f"{delta} vs nivel objetivo (4.0)")
    with level_col:
        st.markdown(f"**Nivel de madurez:** {level_name}")
        st.write(level_desc)

    if mean_score < 2:
        st.error(f"Interpretación: nivel {level_name}. Riesgo alto por ausencia de gobierno formal.")
    elif mean_score <= 3:
        st.warning(f"Interpretación: nivel {level_name}. Existen prácticas puntuales, pero sin estructura robusta.")
    else:
        st.success(f"Interpretación: nivel {level_name}. Base sólida para evolucionar a un modelo maduro.")

    st.divider()

    display_labels = [dimensions[k] for k in dimensions]
    display_scores = [scores[k] for k in dimensions]

    tab_radar, tab_bar = st.tabs(["Radar", "Barras"])

    with tab_radar:
        radar_fig = go.Figure()
        radar_fig.add_trace(
            go.Scatterpolar(
                r=display_scores + [display_scores[0]],
                theta=display_labels + [display_labels[0]],
                fill="toself",
                name="Madurez actual",
                line=dict(color="#1f4e79"),
                fillcolor="rgba(31, 78, 121, 0.35)",
            )
        )
        radar_fig.update_layout(
            polar=dict(radialaxis=dict(visible=True, range=[0, 5])),
            showlegend=False,
            margin=dict(l=20, r=20, t=20, b=20),
        )
        st.plotly_chart(radar_fig, use_container_width=True)

    with tab_bar:
        colors = ["#d73027" if s <= 2 else "#fee08b" if s <= 3 else "#1a9850" for s in display_scores]
        bar_fig = go.Figure(
            go.Bar(
                x=display_scores,
                y=display_labels,
                orientation="h",
                marker=dict(color=colors),
                text=[f"{v}/5" for v in display_scores],
                textposition="outside",
            )
        )
        bar_fig.update_layout(xaxis=dict(range=[0, 5]), margin=dict(l=20, r=20, t=20, b=20))
        st.plotly_chart(bar_fig, use_container_width=True)

    st.divider()

    st.subheader("Observaciones por dimensión")
    for key, label in dimensions.items():
        with st.expander(label):
            score = scores[key]
            st.markdown(
                badge(f"Score: {score}/5", "#1f4e79"),
                unsafe_allow_html=True,
            )
            st.write(maturity.get(key, {}).get("observacion", "Sin observación disponible."))

    st.divider()

    download_payload = {
        "scores": scores,
        "score_global": mean_score,
        "nivel": level_name,
        "descripcion_nivel": level_desc,
    }
    st.download_button(
        "📥 Descargar diagnóstico actual (JSON)",
        data=json.dumps(download_payload, ensure_ascii=False, indent=2),
        file_name="diagnostico_madurez_actual.json",
        mime="application/json",
    )
