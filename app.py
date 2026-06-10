import streamlit as st
import pandas as pd
import joblib
import plotly.graph_objects as go
import numpy as np


st.set_page_config(page_title="Fake Wonka", page_icon="🍫", layout="wide")





st.title("🍫 Fake Wonka - Guia de Alimentação")
st.markdown("Bem-vindo ao catálogo de consulta sobre contaminação e riscos alimentares na indústria.")


st.sidebar.header("🍫 Catalogo")
st.sidebar.markdown("Veja nosso catologo.")

mostrar_catalogo = st.sidebar.button("    Alimentos Cadastrados    ")

busca = st.sidebar.chat_input("Buscar no Catalogo: ")


dados_alimentos = pd.DataFrame({
    "Alimento": ["Chocolate ao Leite", "Salsicha", "Suco de Caixinha"],
    "Contaminação Comum": ["Metais pesados (Cádmio, Chumbo)", "Bactérias (Listeria)", "Fungos (Micotoxinas)"],
    "Riscos": ["Problemas renais e atraso no desenvolvimento", "Infecção alimentar grave", "Alergias crônicas e problemas hepáticos"],
    "Calorias (100g)": [535, 300, 45]
})

if busca:
    st.subheader(f"Resultados para: '{busca}'")
    resultado = dados_alimentos[dados_alimentos["Alimento"].str.contains(busca, case=False)]

    if not resultado.empty:
        for index, row in resultado.iterrows():
            st.write(f"### Dossiê: {row['Alimento']}")
            col1, col2 = st.columns(2)

            with col1:
                st.metric(label="Calorias (por 100g)", value=f"{row['Calorias (100g)']} kcal")
                st.info("**Nota Nutricional:** Alimento com potencial risco rastreado.")

            with col2:
                st.error(f"⚠️ **Agente Contaminante:** {row['Contaminação Comum']}")
                st.warning(f"🚨 **Riscos à Saúde:** {row['Riscos']}")
            st.markdown("---")
    else:
        st.warning("Alimento não encontrado no sistema.")


elif mostrar_catalogo:
    st.subheader("📋 Todos os Alimentos Cadastrados")
    st.dataframe(dados_alimentos, use_container_width=True, hide_index=True)


else:
    st.info("👈 Utilize a barra lateral para pesquisar a ficha de um produto ou visualizar a lista completa de alimentos cadastrados.")

