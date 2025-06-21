import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Perfiles Clínicos Psiquiátricos", layout="wide")
st.title("🧠 Análisis de Perfiles Clínicos en Hospitalización Psiquiátrica")

Cargar datos desde GitHub (ajusta con tu enlace RAW)
url = "https://github.com/JorgePizza/ProyectoML.git"
df = pd.read_csv(url)

Filtro por clúster
cluster = st.selectbox("Selecciona un clúster para explorar:", sorted(df['Cluster'].unique()))
df_filtrado = df[df['Cluster'] == cluster]

Mostrar resumen
st.subheader("Resumen del Clúster Seleccionado")
st.write(f"*Total de pacientes:* {len(df_filtrado)}")
st.dataframe(df_filtrado)

Estadísticas agrupadas
st.subheader("Promedios del Clúster")
st.write(df_filtrado[['Edad', 'Días_internamiento']].describe())

Visualización con Plotly
fig = px.scatter(df, x='Edad', y='Días_internamiento', color=df['Cluster'].astype(str),
                 title="Distribución de pacientes por Edad y Días de Internamiento",
                 labels={"color": "Clúster"})
st.plotly_chart(fig, use_container_width=True)
