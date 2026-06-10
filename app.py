import streamlit as st
import pandas as pd
import joblib
import plotly.graph_objects as go
import numpy as np

# Definindo o nome da guia do navegador
st.set_page_config(page_title="Fake Wonka", page_icon="🍫", layout="wide")


# Crianção do Layout da Pagina, para isso feita em blocos

# Criação do cabeçalho da Pagina
st.title("🍫 Fake Wonka - Guia de Alimentação")
st.markdown("Catalogo para consulta de alimentos")

# 4. Barra Lateral - Vai ser um simulador para os sensores
st.sidebar.header("🍫 Catalogo")
st.sidebar.markdown("Veja nosso catologo.")

st.sidebar.button("Alimentos Cadastrados")

busca = st.sidebar.chat_input("Buscar no Catalogo: ")




