import os

import pandas as pd
import streamlit as st

from src.utils import load_csv, load_json, maturity_level


def _priority_score(row) -> float:
    return (row["impacto"] * 0.35) + (row["urgencia"] * 0.35) + (row["riesgo"] * 0.20) - (row["esfuerzo"] * 0.10)


def render() -> None:
    base_data = os.path.join(os.path.dirname(__file__), "..", "data")
    company = load_json(os.path.join(base_data, "company_profile.json"))
    maturity = load_json(os.path.join(base_data, "maturity_sample.json"))
    problems_df = load_csv(os.path.join(base_data, "problems_sample.csv"))

    st.title("🏛️ Comité de Dirección")
    st.caption("Decisión ejecutiva para iniciar la implantación de Data Governance tras el assessment.")
    st.divider()

    if not company or not maturity or problems_df.empty:
        st.error("No se pudieron cargar datos suficientes para construir la recomendación ejecutiva.")
        return

    dim_scores = [float(v.get("score", 0)) for v in maturity.values() if isinstance(v, dict)]
    global_score = round(sum(dim_scores) / len(dim_scores), 2) if dim_scores else 0
    level_name, _ = maturity_level(global_score)

    ranking_df = problems_df.copy()
    ranking_df["score"] = ranking_df.apply(_priority_score, axis=1).round(2)
    ranking_df = ranking_df.sort_values("score", ascending=False).reset_index(drop=True)

    critical_issues = int((ranking_df["score"] >= 4.0).sum())

    decision = "GO"
    confidence = "Alta"
    rationale = (
        "Existe capacidad tecnológica y presión regulatoria suficiente para justificar arranque inmediato "
        "del programa de gobierno del dato con enfoque por dominios."
    )

    if global_score < 2.5:
        decision = "GO CONDICIONADO"
        confidence = "Media"
        rationale = (
            "Se recomienda arranque condicionado a reforzar sponsorship ejecutivo y ownership de dominio "
            "en los primeros 90 días."
        )

    k1, k2, k3, k4 = st.columns(4)
    k1.metric("Empresa", company.get("nombre", "N/D"))
    k2.metric("Madurez actual", f"{global_score}/5 ({level_name})")
    k3.metric("Problemas críticos", str(critical_issues))
    k4.metric("Decisión recomendada", decision)

    st.divider()

    if decision == "GO":
        st.success(f"Recomendación Comité: {decision} · Confianza {confidence}")
    else:
        st.warning(f"Recomendación Comité: {decision} · Confianza {confidence}")

    st.write(rationale)

    st.divider()

    st.subheader("Presupuesto estimado (12 meses)")
    budget_df = pd.DataFrame(
        [
            ["Gobierno organizativo (Council + Data Office)", "350.000", "Patrocinio, PMO, gobierno y cambio"],
            ["Data Quality e inventario omnicanal", "420.000", "Reglas, scorecards, observabilidad y operación"],
            ["Catálogo, glosario y linaje", "380.000", "Plataforma metadata + adopción negocio"],
            ["MDM Producto e Inventario", "650.000", "Diseño, integración y despliegue por dominios"],
            ["ESG/Privacidad/AI Act Controls", "300.000", "Controles de cumplimiento y auditabilidad"],
        ],
        columns=["Bloque", "Estimación EUR", "Notas"],
    )
    total_budget = "2.100.000"

    st.dataframe(budget_df, use_container_width=True, hide_index=True)
    st.info(f"Inversión estimada total programa (12 meses): EUR {total_budget}")

    st.divider()

    st.subheader("Riesgos de ejecución y mitigaciones")
    risk_df = pd.DataFrame(
        [
            ["Falta de ownership real", "Alto", "Nombramiento formal de Data Owners con objetivos trimestrales"],
            ["Sobrecarga de equipos IT", "Medio-Alto", "Modelo federado con participación de negocio y priorización estricta"],
            ["Fragmentación KPI por dominios", "Alto", "Glosario único y governance board de definiciones"],
            ["Bloqueos de cumplimiento regulatorio", "Alto", "Controles privacy/ESG/AI-by-design desde Q1"],
            ["Baja adopción en negocio", "Medio", "Plan de change management y comunicación ejecutiva"],
        ],
        columns=["Riesgo", "Impacto", "Mitigación"],
    )
    st.dataframe(risk_df, use_container_width=True, hide_index=True)

    st.divider()

    st.subheader("Resolución propuesta")
    st.markdown("1. Aprobar arranque del programa de gobierno del dato con foco en 4 dominios críticos.")
    st.markdown("2. Liberar presupuesto por fases con revisión de hitos al cierre de cada trimestre.")
    st.markdown("3. Nombrar sponsor ejecutivo y comité de seguimiento mensual.")
