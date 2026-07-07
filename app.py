import pandas as pd
import plotly.express as px
import streamlit as st

car_data = pd.read_csv("vehicles.csv")

st.header("Dashboard de Veículos")

# Botão do histograma
hist_button = st.button("Criar Histograma")

if hist_button:
    st.write("Histograma da quilometragem dos veículos")

    fig = px.histogram(
        car_data,
        x="odometer"
    )

    st.plotly_chart(fig)

scatter_button = st.button("Criar Gráfico de Dispersão")

if scatter_button:
    st.write("Preço x Quilometragem")

    fig = px.scatter(
        car_data,
        x="odometer",
        y="price"
    )

    st.plotly_chart(fig)