import os
from io import BytesIO

import streamlit as st
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

from src.utils import load_csv, load_json, maturity_level


DIMENSIONS = {
    "estrategia_dato": "Estrategia del Dato",
    "organizacion_roles": "Organización y Roles",
    "calidad_dato": "Calidad del Dato",
    "uso_negocio": "Uso en Negocio",
    "tecnologia_arquitectura": "Tecnología y Arquitectura",
    "gobierno_control": "Gobierno y Control",
}


def _priority_score(row) -> float:
    return (row["impacto"] * 0.35) + (row["urgencia"] * 0.35) + (row["riesgo"] * 0.20) - (row["esfuerzo"] * 0.10)


def _safe_pdf_text(text: str) -> str:
    return text.encode("latin-1", "ignore").decode("latin-1")


def generate_pdf(markdown_text: str) -> bytes:
    buffer = BytesIO()
    pdf = canvas.Canvas(buffer, pagesize=A4)
    width, height = A4
    margin_x = 40
    y = height - 40

    lines = markdown_text.splitlines()
    for line in lines:
        clean = _safe_pdf_text(line.replace("#", "").replace("*", "").strip())
        if not clean:
            y -= 8
        else:
            max_chars = 110
            chunks = [clean[i : i + max_chars] for i in range(0, len(clean), max_chars)]
            for chunk in chunks:
                if y < 40:
                    pdf.showPage()
                    y = height - 40
                pdf.drawString(margin_x, y, chunk)
                y -= 14

        if y < 40:
            pdf.showPage()
            y = height - 40

    pdf.save()
    return buffer.getvalue()


def generate_markdown(company, maturity, problems_df, notes) -> str:
    nombre = company.get("nombre", "Empresa sin nombre")
    company_rows = [
        ("Nombre", nombre),
        ("Sector", company.get("sector", "N/D")),
        ("Tamaño", company.get("tamaño", "N/D")),
        ("Presencia geográfica", company.get("presencia_geografica", "N/D")),
        ("Nivel de digitalización", company.get("nivel_digitalizacion", "N/D")),
        ("Tiendas FY2025", company.get("unidades_comerciales", "N/D")),
        ("Ventas FY2025", company.get("ventas_fy2025", "N/D")),
        ("Ventas online FY2025", company.get("ventas_online_fy2025", "N/D")),
        ("Mercados", company.get("mercados", "N/D")),
        ("Sistemas relevantes", ", ".join(company.get("sistemas_relevantes", []))),
        ("Presión regulatoria", company.get("presion_regulatoria", "N/D")),
        ("Áreas de negocio", ", ".join(company.get("areas_negocio", []))),
        ("Contexto del assessment", company.get("contexto_assessment", "N/D")),
        ("Consultor", company.get("consultor", "N/D")),
        ("Fecha", company.get("fecha", "N/D")),
    ]

    maturity_lines = []
    dim_scores = []
    for key, label in DIMENSIONS.items():
        score = float(maturity.get(key, {}).get("score", 0))
        dim_scores.append(score)
        level_name, _ = maturity_level(score)
        observacion = maturity.get(key, {}).get("observacion", "")
        maturity_lines.append(f"| {label} | {score:.1f} | {level_name} | {observacion} |")

    global_score = round(sum(dim_scores) / len(dim_scores), 2) if dim_scores else 0
    global_level, global_desc = maturity_level(global_score)

    problems_rows = []
    for _, row in problems_df.iterrows():
        problems_rows.append(
            f"| {row['titulo']} | {row['area_afectada']} | {row['dominio_dato']} | {row['impacto']} | {row['urgencia']} | {row['riesgo']} |"
        )

    ranking_df = problems_df.copy()
    ranking_df["score"] = ranking_df.apply(_priority_score, axis=1).round(2)
    ranking_df = ranking_df.sort_values("score", ascending=False).reset_index(drop=True)
    ranking_df["rank"] = ranking_df.index + 1
    top3 = ranking_df.head(3)

    top3_sections = []
    for _, row in top3.iterrows():
        top3_sections.append(
            "\n".join(
                [
                    f"### {int(row['rank'])}. {row['titulo']}",
                    f"**Score de priorización:** {row['score']}",
                    f"**Descripción:** {row['descripcion']}",
                    f"**Impacto en negocio:** {row['impacto_negocio']}",
                ]
            )
        )

    notas_clave = "\n".join([f"- {item}" for item in notes.get("notas_clave", [])])
    quick_wins = "\n".join([f"- {item}" for item in notes.get("quick_wins", [])])
    areas_profundizar = "\n".join([f"- {item}" for item in notes.get("areas_profundizar", [])])
    lineas_actuacion = "\n".join([f"- {item}" for item in notes.get("lineas_actuacion", [])])
    dominios = ", ".join(notes.get("dominios_prioritarios", []))

    company_table_rows = "\n".join([f"| {k} | {v} |" for k, v in company_rows])
    maturity_table_rows = "\n".join(maturity_lines)
    findings_table_rows = "\n".join(problems_rows)
    top3_markdown = "\n\n".join(top3_sections)

    markdown = f"""# Assessment de Gobierno del Dato — {nombre}
*Generado con Data Governance Assessment Tool*
---
## 1. Contexto de la Empresa
| Campo | Valor |
|---|---|
{company_table_rows}

## 2. Diagnóstico de Madurez
| Dimensión | Puntuación | Nivel | Observación |
|---|---:|---|---|
{maturity_table_rows}

**Puntuación global:** {global_score}/5  
**Nivel global:** {global_level} ({global_desc})

## 3. Hallazgos Detectados ({len(problems_df)} problemas)
| Título | Área | Dominio | Impacto | Urgencia | Riesgo |
|---|---|---|---:|---:|---:|
{findings_table_rows}

## 4. Top 3 Problemas Priorizados
{top3_markdown}

## 5. Notas del Consultor
{notas_clave}

## 6. Recomendaciones Iniciales
**Quick Wins**
{quick_wins}

**Áreas a profundizar**
{areas_profundizar}

**Líneas de actuación**
{lineas_actuacion}

**Dominios prioritarios**
- {dominios}

## 7. Conclusión del Assessment
{notes.get("conclusion_general", "Sin conclusión disponible.")}

---
*Este documento es la base para la propuesta de modelo objetivo, estrategia del dato y roadmap de implantación.*
"""
    return markdown


def render() -> None:
    base_data = os.path.join(os.path.dirname(__file__), "..", "data")
    company = load_json(os.path.join(base_data, "company_profile.json"))
    maturity = load_json(os.path.join(base_data, "maturity_sample.json"))
    problems_df = load_csv(os.path.join(base_data, "problems_sample.csv"))
    notes = load_json(os.path.join(base_data, "assessment_notes.json"))

    st.title("📋 Resumen Ejecutivo")
    st.caption("Entregable ejecutivo del assessment cerrado y exportación en Markdown.")
    st.divider()

    if not company or not maturity or problems_df.empty or not notes:
        st.error("No se pudieron cargar uno o más archivos de data/ necesarios para el resumen.")
        return

    dim_scores = [float(maturity.get(key, {}).get("score", 0)) for key in DIMENSIONS]
    mean_score = round(sum(dim_scores) / len(dim_scores), 2)
    level_name, _ = maturity_level(mean_score)

    ranking_df = problems_df.copy()
    ranking_df["score"] = ranking_df.apply(_priority_score, axis=1).round(2)
    ranking_df = ranking_df.sort_values("score", ascending=False).reset_index(drop=True)

    top_problem = ranking_df.iloc[0]["titulo"] if not ranking_df.empty else "N/D"

    kpi1, kpi2, kpi3, kpi4 = st.columns(4)
    kpi1.metric("Empresa", company.get("nombre", "N/D"))
    kpi2.metric("Madurez global", f"{mean_score}/5 ({level_name})")
    kpi3.metric("N.º de problemas", str(len(problems_df)))
    kpi4.metric("Top problema", top_problem)

    st.divider()

    markdown_string = generate_markdown(company, maturity, problems_df, notes)
    st.markdown(markdown_string)

    st.divider()

    st.download_button(
        "📥 Descargar resumen .md",
        data=markdown_string,
        file_name="assessment_gobierno_dato.md",
        mime="text/markdown",
    )

    pdf_bytes = generate_pdf(markdown_string)
    st.download_button(
        "📄 Descargar resumen .pdf",
        data=pdf_bytes,
        file_name="assessment_gobierno_dato.pdf",
        mime="application/pdf",
    )
