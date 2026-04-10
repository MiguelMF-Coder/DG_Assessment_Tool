# Data Governance Assessment Tool

## Herramienta de diagnóstico inicial para proyectos de gobierno del dato

Esta aplicación está diseñada para simular un proyecto consultivo **end-to-end** de Data Governance.
Incluye assessment inicial completo y la propuesta posterior de modelo objetivo, estrategia y roadmap.

> Importante: la base del contenido proviene del assessment simulado de Inditex y está preparada como demo consultiva integral.

## ¿Qué hace y por qué existe?

Cuando un consultor entra por primera vez en una compañía, necesita construir una visión clara del estado real del dato:

- Contexto empresarial y regulatorio.
- Madurez actual de gestión del dato.
- Hallazgos operativos, organizativos y tecnológicos.
- Priorización de iniciativas por impacto y viabilidad.
- Resumen ejecutivo exportable en Markdown y PDF.
- Diseño de modelo objetivo de gobierno del dato.
- Estrategia de ejecución y roadmap trimestral.

## Instalación

```bash
pip install -r requirements.txt
```

## Ejecución

```bash
streamlit run app.py
```

## Estructura funcional (11 secciones)

| Sección | Propósito |
|---|---|
| 🏠 Home | Explica el objetivo del assessment y el alcance de la herramienta. |
| 🏢 Perfil de Empresa | Contexto de negocio, sistemas y presión regulatoria. |
| 📊 Diagnóstico de Madurez | Evaluación de 6 dimensiones de gobierno del dato. |
| 🔍 Hallazgos | Registro detallado de problemas identificados por el consultor. |
| ⚖️ Priorización | Ranking de hallazgos según fórmula de impacto, urgencia, riesgo y esfuerzo. |
| 📋 Resumen Ejecutivo | Vista consolidada y exportación en formato Markdown/PDF. |
| 💡 Recomendaciones | Quick wins y líneas preliminares de actuación. |
| 🧭 Modelo Objetivo | Diseño objetivo de capacidades, roles y operating model de dato. |
| 🎯 Estrategia del Dato | Objetivos estratégicos, líneas de acción y KPIs de éxito. |
| 🗺️ Roadmap | Plan de implantación por trimestres con hitos y prioridades. |
| 🏛️ Comité de Dirección | Decisión Go/No-Go, presupuesto estimado y riesgos de ejecución. |

## Encaje en el ciclo completo del proyecto

**Assessment (esta herramienta) → Modelo Objetivo → Estrategia → Roadmap**

Este repositorio cubre todo el flujo anterior en una única aplicación de demostración.

## Stack tecnológico

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?logo=python&logoColor=white) ![Streamlit](https://img.shields.io/badge/Streamlit-App-FF4B4B?logo=streamlit&logoColor=white) ![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-150458?logo=pandas&logoColor=white) ![Plotly](https://img.shields.io/badge/Plotly-Visualización-3F4F75?logo=plotly&logoColor=white)
