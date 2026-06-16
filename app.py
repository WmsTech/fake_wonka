import streamlit as st
import pandas as pd
import joblib
import plotly.graph_objects as go
import numpy as np
import base64


# --- CONFIGURAÇÃO INICIAL ---
st.set_page_config(page_title="Fake Wonka", page_icon="🍫", layout="wide", initial_sidebar_state="collapsed")

# --- BASE DE DADOS SIMULADA ---
dados_alimentos = pd.DataFrame({
    "Alimento": ["Chocolate ao Leite", "Salsicha", "Suco de Caixinha", "Biscoito Recheado"],
    "Resumo": ["Atenção: Possíveis traços de metais pesados.", "Atenção: Risco de Listeria no lote atual.", "Atenção: Alto índice de micotoxinas.", "Atenção: Excesso de corantes artificiais banidos."],
})

def carregar_imagem_base64(caminho):
    try:
        with open(caminho, "rb") as image_file:
            encoded = base64.b64encode(image_file.read()).decode()
            return f"data:image/png;base64,{encoded}"
    except FileNotFoundError:
        return "data:image/gif;base64,R0lGODlhAQABAAD/ACwAAAAAAQABAAACADs="

CAMINHO_DA_LOGO = "logo_sem_fundo.png" # Certifique-se de que o nome está correto
logo_b64 = carregar_imagem_base64(CAMINHO_DA_LOGO)

# Gerenciador de Estado
if 'entrou_no_site' not in st.session_state:
    st.session_state['entrou_no_site'] = False

# ==========================================
# CSS GLOBAL E CORREÇÕES AVANÇADAS
# ==========================================
st.markdown("""
<style>
    .stApp { background-color: #301f1b; color: #F8F3E6; }
    [data-testid="collapsedControl"] { display: none; }
    header { visibility: hidden; }

    /* --- CORREÇÃO DA BARRA DE PESQUISA --- */
    /* Remove o fundo escuro das caixas protetoras do Streamlit */
    div[data-baseweb="input"], div[data-baseweb="base-input"] {
        background-color: transparent !important;
        border: none !important;
    }
    
    /* Pinta apenas o campo de digitação com borda redonda e bege */
    .stTextInput input { 
        background-color: #E2C792 !important; 
        color: black !important; 
        border-radius: 30px !important; 
        padding: 12px 20px !important; 
        border: none !important; 
        box-shadow: none !important;
    }
    .stTextInput input::placeholder { color: #5c4033 !important; }
</style>
""", unsafe_allow_html=True)


# ==========================================
# TELA 1: HOME
# ==========================================
if not st.session_state['entrou_no_site']:
    
    # CSS Exclusivo da Home para o Botão Saiba Mais
    st.markdown("""
    <style>
        /* --- CORREÇÃO DO BOTÃO SAIBA MAIS --- */
        .stButton > button {
            background: linear-gradient(90deg, #A67C00 0%, #E2B922 50%, #A67C00 100%) !important;
            color: black !important;
            font-family: serif !important;
            font-weight: 900 !important;
            font-size: 24px !important;
            border: none !important;
            border-radius: 0px !important; /* Tira borda redonda padrão */
            box-shadow: none !important;
            clip-path: polygon(5% 0, 95% 0, 100% 50%, 95% 100%, 5% 100%, 0% 50%) !important;
            height: 60px !important;
            transition: transform 0.3s !important;
        }
        .stButton > button:hover { transform: scale(1.05) !important; }
    </style>
    """, unsafe_allow_html=True)

    st.write("\n" * 4) 
    st.markdown(f"""
        <div style="display: flex; justify-content: center; align-items: center; margin-bottom: 30px;">
            <img src="{logo_b64}" style="max-width: 600px; height: auto;">
        </div>
    """, unsafe_allow_html=True)
    
    # Colunas para alinhar ao centro
    col1, col_centro, col3 = st.columns([1, 1, 1])
    with col_centro:
        # AQUI ESTAVA O ERRO: Adicionado o use_container_width=True para esticar a fita
        if st.button("SAIBA MAIS", use_container_width=True):
            st.session_state['entrou_no_site'] = True
            st.rerun()

# ==========================================
# TELA 2: CATÁLOGO E PESQUISA
# ==========================================
else:
    # Topo com a Logo Menor
    col_logo, col_vazia, col_voltar = st.columns([1, 6, 1])
    with col_logo:
        st.markdown(f'<img src="{logo_b64}" style="max-height: 250px;">', unsafe_allow_html=True)
    with col_voltar:
        if st.button("🏠 Home", use_container_width=True):
            st.session_state['entrou_no_site'] = False
            st.rerun()

    st.write("\n")
    
    # Campo de busca
    col_espaco1, col_busca, col_espaco2 = st.columns([1, 2, 1])
    with col_busca:
        busca = st.text_input("Buscar", placeholder="🔍 Pesquise aqui...", label_visibility="collapsed")
    
    st.write("\n" * 2)

    # Lógica de Busca
    if busca:
        resultados = dados_alimentos[dados_alimentos["Alimento"].str.contains(busca, case=False)]
    else:
        resultados = dados_alimentos

    # Renderização dos Cards
    if not resultados.empty:
        for index, row in resultados.iterrows():
            card_html = f"""
<div style="display: flex; gap: 15px; margin-bottom: 20px; align-items: stretch; justify-content: center;">
    <div style="background-color: #E2C792; border-radius: 15px; width: 25%; padding: 30px; text-align: center; color: #21130d; display: flex; align-items: center; justify-content: center; font-weight: bold; min-height: 120px;">
        Foto do<br>produto
    </div>
    <div style="background-color: #7B4E31; border-radius: 15px; width: 60%; padding: 20px; color: white; display: flex; flex-direction: column; justify-content: center;">
        <h4 style="margin: 0; color: #E2C792;">{row['Alimento']}</h4>
        <p style="margin: 5px 0 0 0; font-size: 14px;">{row['Resumo']}</p>
    </div>
</div>
"""
            st.markdown(card_html, unsafe_allow_html=True)
    else:
        st.markdown("<p style='text-align: center; color: #E2C792;'>Nenhum alimento encontrado com esse nome.</p>", unsafe_allow_html=True)
