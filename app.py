
import streamlit as st
import pandas as pd
import joblib

# Cargar paquete del modelo
paquete = joblib.load("modelo_tiempo_viaje_flaml.pkl")

modelo = paquete["modelo"]
preprocesador = paquete["preprocesador"]
categorias_app = paquete["categorias_app"]

st.set_page_config(
    page_title="Predicción de tiempo de viaje",
    page_icon="🚗",
    layout="centered"
)

st.title("Predicción del tiempo de viaje en Medellín")
st.write(
    "Aplicación predictiva basada en Machine Learning para estimar el tiempo de viaje "
    "en minutos a partir del mes, día de la semana, hora, punto de inicio y punto final del tramo."
)

st.subheader("Ingrese las condiciones del viaje")

mes = st.selectbox("Mes", categorias_app["MES"])
nombre_dia = st.selectbox("Día de la semana", categorias_app["NOMBRE_DÍA"])
hora = st.selectbox("Hora", categorias_app["HORA"])
inicio = st.selectbox("Punto de inicio", categorias_app["INICIO"])
fin = st.selectbox("Punto final", categorias_app["FIN"])

if st.button("Predecir tiempo de viaje"):
    entrada = pd.DataFrame([{
        "MES": str(mes),
        "NOMBRE_DÍA": nombre_dia,
        "HORA": str(hora),
        "INICIO": inicio,
        "FIN": fin
    }])

    entrada_transformada = preprocesador.transform(entrada)
    prediccion = modelo.predict(entrada_transformada)

    st.success(f"Tiempo estimado de viaje: {prediccion[0]:.2f} minutos")

    st.write("### Datos ingresados")
    st.dataframe(entrada)

st.markdown("---")
st.caption("Modelo final: FLAML AutoML - XGBoost")
