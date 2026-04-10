# Data Governance Assessment Tool

## Herramienta de diagnóstico inicial para proyectos de gobierno del dato

Esta aplicación está diseñada para la **fase de assessment inicial** en un proyecto de Data Governance.
Su objetivo es diagnosticar la situación actual de una organización, descubrir problemas críticos y priorizar acciones.

> Importante: esta herramienta **no** representa la solución final (modelo objetivo, estrategia completa ni roadmap definitivo).

## ¿Qué hace y por qué existe?

Cuando un consultor entra por primera vez en una compañía, necesita construir una visión clara del estado real del dato:

- Contexto empresarial y regulatorio.
- Madurez actual de gestión del dato.
- Hallazgos operativos, organizativos y tecnológicos.
- Priorización de iniciativas por impacto y viabilidad.
- Resumen ejecutivo exportable como base para la siguiente fase.

## Instalación

```bash
pip install -r requirements.txt
```

## Ejecución

```bash
streamlit run app.py
```

## Estructura funcional (7 secciones)

| Sección | Propósito |
|---|---|
| 🏠 Home | Explica el objetivo del assessment y el alcance de la herramienta. |
| 🏢 Perfil de Empresa | Contexto de negocio, sistemas y presión regulatoria. |
| 📊 Diagnóstico de Madurez | Evaluación de 6 dimensiones de gobierno del dato. |
| 🔍 Hallazgos | Registro detallado de problemas identificados por el consultor. |
| ⚖️ Priorización | Ranking de hallazgos según fórmula de impacto, urgencia, riesgo y esfuerzo. |
| 📋 Resumen Ejecutivo | Vista consolidada y exportación en formato Markdown. |
| 💡 Recomendaciones | Quick wins y líneas preliminares de actuación. |

## Encaje en el ciclo completo del proyecto

**Assessment (esta herramienta) → Modelo Objetivo → Estrategia → Roadmap**

Este repositorio cubre únicamente la primera fase: diagnóstico inicial y base de decisión.

## Uso con datos reales

Sustituye los archivos en la carpeta data por información real de la organización evaluada:

- data/company_profile.json
- data/maturity_sample.json
- data/problems_sample.csv
- data/assessment_notes.json

## Stack tecnológico

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?logo=python&logoColor=white) ![Streamlit](https://img.shields.io/badge/Streamlit-App-FF4B4B?logo=streamlit&logoColor=white) ![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-150458?logo=pandas&logoColor=white) ![Plotly](https://img.shields.io/badge/Plotly-Visualización-3F4F75?logo=plotly&logoColor=white)
