
# Predicción del tiempo de viaje en Medellín

Este proyecto desarrolla una aplicación web en Streamlit para predecir el tiempo de viaje en minutos en corredores viales de Medellín.

## Dataset

El proyecto utiliza el dataset **Velocidad y tiempo de viaje GT**, proveniente de datos abiertos.

## Variable objetivo

La variable objetivo del modelo es:

- `TV_MINUTOS`: tiempo de viaje en minutos.

## Variables de entrada

El modelo utiliza las siguientes variables:

- `MES`
- `NOMBRE_DÍA`
- `HORA`
- `INICIO`
- `FIN`

## Modelo final

El modelo final seleccionado fue:

- **FLAML AutoML - XGBoost**

Este modelo fue seleccionado porque obtuvo el mejor desempeño en el conjunto de prueba, con menor MAE, menor RMSE y mayor R² frente al modelo manual Voting Regressor.

## Métricas finales

| Modelo | MAE | RMSE | R² |
|---|---:|---:|---:|
| Voting Regressor | 1.8117 | 2.5947 | 0.5034 |
| FLAML AutoML - XGBoost | 1.5822 | 2.3649 | 0.5875 |

## Archivos principales

- `app.py`: aplicación web en Streamlit.
- `modelo_tiempo_viaje_flaml.pkl`: modelo serializado junto con el preprocesador.
- `requirements.txt`: dependencias necesarias para ejecutar la aplicación.
- `README.md`: descripción general del proyecto.

## Ejecución local

Para ejecutar la aplicación localmente:

```bash
streamlit run app.py
