import streamlit as st
import pandas as pd
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
            encoded = base64.b64encode(image_file.read()).decode()import streamlit as st
import pandas as pd
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

# --- CARREGAMENTO DAS IMAGENS ---
logo_b64 = carregar_imagem_base64("logo_sem_fundo.png")
botao_saiba_mais_b64 = carregar_imagem_base64("botao_saiba_mais.png")
botao_sobre_nos_b64 = carregar_imagem_base64("botao_sobre_nos.png")
foto_equipe_b64 = carregar_imagem_base64("foto_equipe.png") 

# --- GERENCIADOR DE PÁGINAS ---
if 'pagina_atual' not in st.session_state:
    st.session_state['pagina_atual'] = 'home'

# CSS Global
st.markdown("""
<style>
    .stApp { background-color: #301f1b; color: #F8F3E6; }
    [data-testid="collapsedControl"] { display: none; }
    header { visibility: hidden; }
            
  
    div[data-baseweb="input"], div[data-baseweb="base-input"] {
        background-color: transparent !important;
        border: none !important;
    }
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
if st.session_state['pagina_atual'] == 'home':
    
    st.markdown(f"""
    <style>
        /* --- BLOCO 1: BOTÃO SAIBA MAIS (Tipo Primário) --- */
        button[kind="primary"], button[kind="primary"]:active, button[kind="primary"]:focus {{
            background-image: url('{botao_saiba_mais_b64}') !important;
            background-size: contain !important;
            background-repeat: no-repeat !important;
            background-position: center !important;
            background-color: transparent !important;
            border: none !important;
            box-shadow: none !important;
            color: transparent !important; 
            height: 70px !important;
            width: 100% !important;
            transition: transform 0.3s !important;
            outline: none !important; 
        }}
        button[kind="primary"]:hover {{ 
            transform: scale(1.05) !important; 
        }}

        /* --- BLOCO 2: BOTÃO SOBRE NÓS (Tipo Secundário) --- */
        button[kind="secondary"], button[kind="secondary"]:active, button[kind="secondary"]:focus {{
            background-image: url('{botao_sobre_nos_b64}') !important;
            background-size: contain !important;
            background-repeat: no-repeat !important;
            background-position: center right !important;
            background-color: transparent !important;
            border: none !important;
            box-shadow: none !important;
            color: transparent !important; 
            height: 45px !important;
            width: 180px !important; 
            
            position: fixed !important;
            bottom: 30px !important;
            right: 30px !important;
            z-index: 999 !important;
            
            transition: transform 0.3s !important;
            outline: none !important;
        }}
        button[kind="secondary"]:hover {{ 
            transform: scale(1.05) !important; 
        }}
    </style>
    """, unsafe_allow_html=True)

    
    st.write("\n" * 4)  
    st.markdown(f"""
        <div style="display: flex; justify-content: center; align-items: center; margin-bottom: 30px;">
            <img src="{logo_b64}" style="max-width: 700px; height: auto;">
        </div>
    """, unsafe_allow_html=True)
    
    # Adicionamos type="primary" no Saiba Mais
    col1, col_centro, col3 = st.columns([2, 1, 2])
    with col_centro:
        if st.button("SAIBA MAIS", type="primary", use_container_width=True):
            st.session_state['pagina_atual'] = 'catalogo'
            st.rerun()

    # O botão Sobre Nós perdeu as colunas e ganha type="secondary". 
    # Ele pode ser solto no código, o CSS acima vai teletransportá-lo para o canto!
    if st.button("SOBRE NÓS", type="secondary"):
        st.session_state['pagina_atual'] = 'sobre'
        st.rerun()


# ==========================================
# TELA 2: SOBRE NÓS
# ==========================================
elif st.session_state['pagina_atual'] == 'sobre':
    
    col_logo, col_vazia, col_voltar = st.columns([1, 6, 1])
    with col_logo:
        st.markdown(f'<img src="{logo_b64}" style="max-height: 250px;">', unsafe_allow_html=True)
    with col_voltar:
        if st.button("⬅️ Voltar"):
            st.session_state['pagina_atual'] = 'home'
            st.rerun()

    st.write("\n" * 2)

    col_esq, col_meio, col_dir = st.columns([1, 1.5, 1])

    with col_esq:
        st.markdown("""
        <div style="background-color: #E2C792; border-radius: 15px; padding: 25px; text-align: center; color: #21130d; font-weight: bold; font-size: 24px; margin-bottom: 15px;">Missão</div>
        <div style="background-color: #7B4E31; border-radius: 15px; padding: 25px; text-align: center; color: white; font-weight: bold; font-size: 24px; margin-bottom: 15px;">Visão</div>
        <div style="background-color: #E2C792; border-radius: 15px; padding: 25px; text-align: center; color: #21130d; font-weight: bold; font-size: 24px;">Valores</div>
        """, unsafe_allow_html=True)

    with col_meio:
        st.markdown(f"""
        <div style="background-color: #7B4E31; border-radius: 15px; padding: 20px; text-align: center; height: 100%; min-height: 250px; display: flex; align-items: center; justify-content: center;">
            <img src="{foto_equipe_b64}" style="max-width: 90%; border-radius: 10px;" alt="Foto do Grupo">
        </div>
        """, unsafe_allow_html=True)

    with col_dir:
        st.markdown("""
        <div style="background-color: #E2C792; border-radius: 15px; padding: 30px; text-align: center; color: #21130d; font-weight: bold; height: 100%; min-height: 250px; display: flex; align-items: center; justify-content: center; font-size: 20px;">
            Descrição sobre<br>o grupo
        </div>
        """, unsafe_allow_html=True)


# ==========================================
# TELA 3: CATÁLOGO E PESQUISA
# ==========================================
elif st.session_state['pagina_atual'] == 'catalogo':
    
    st.markdown("""
    <style>
        .stTextInput > div > div { background-color: transparent !important; border: none !important; box-shadow: none !important; }
        .stTextInput > div > div > input { background-color: #E2C792 !important; color: black !important; border-radius: 30px !important; padding: 12px 20px !important; border: none !important; }
        .stTextInput > div > div > input::placeholder { color: #5c4033 !important; }
    </style>
    """, unsafe_allow_html=True)

    col_logo, col_vazia, col_voltar = st.columns([1, 6, 1])
    with col_logo:
        st.markdown(f'<img src="{logo_b64}" style="max-height: 250px;">', unsafe_allow_html=True)
    with col_voltar:
        if st.button("⬅️ Sair"):
            st.session_state['pagina_atual'] = 'home'
            st.rerun()

    st.write("\n")
    
    col_espaco1, col_busca, col_espaco2 = st.columns([1, 2, 1])
    with col_busca:
        busca = st.text_input("Buscar", placeholder="🔍 Pesquise aqui...", label_visibility="collapsed")
    
    st.write("\n" * 2)

    if busca:
        resultados = dados_alimentos[dados_alimentos["Alimento"].str.contains(busca, case=False)]
    else:
        resultados = dados_alimentos

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
            return f"data:image/png;base64,{encoded}"
    except FileNotFoundError:
        return "data:image/gif;base64,R0lGODlhAQABAAD/ACwAAAAAAQABAAACADs="

# Carregue as duas imagens agora (Ajuste os nomes para os seus arquivos reais)
logo_b64 = carregar_imagem_base64("logo_sem_fundo.png")
botao_saiba_mais_b64 = carregar_imagem_base64("botao_saiba_mais.png") # <--- NOVA IMAGEM AQUI
botao_sobre_nos_b64 = carregar_imagem_base64("botao_sobre_nos.png") # <--- NOVA IMAGEM AQUI

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
    
    st.markdown(f"""
    <style>
        /* --- 1. BOTÃO SAIBA MAIS (Primeiro bloco de colunas) --- */
        div[data-testid="stHorizontalBlock"]:nth-of-type(1) button {{
            background-image: url('{botao_saiba_mais_b64}') !important;
            background-size: contain !important;
            background-repeat: no-repeat !important;
            background-position: center !important;
            background-color: transparent !important;
            border: none !important;
            box-shadow: none !important;
            color: transparent !important; 
            height: 70px !important; /* Ajuste fino da altura aqui */
            width: 100% !important;
            transition: transform 0.3s !important;
            cursor: pointer !important;
        }}
        div[data-testid="stHorizontalBlock"]:nth-of-type(1) button:hover {{ transform: scale(1.05) !important; }}

        /* --- 2. BOTÃO SOBRE NÓS (Segundo bloco de colunas - Fixo) --- */
        /* Gruda o bloco inteiro no canto da tela */
        div[data-testid="stHorizontalBlock"]:nth-of-type(2) {{
            position: fixed !important;
            bottom: 30px !important;
            right: 30px !important;
            width: 180px !important; /* Controla a largura geral do botão lateral */
            z-index: 999 !important;
        }}
        
        div[data-testid="stHorizontalBlock"]:nth-of-type(2) button {{
            background-image: url('{botao_sobre_nos_b64}') !important;
            background-size: contain !important;
            background-repeat: no-repeat !important;
            background-position: center right !important;
            background-color: transparent !important;
            border: none !important;
            box-shadow: none !important;
            color: transparent !important; 
            height: 45px !important; /* Altura do botão Sobre Nós */
            width: 100% !important;
            transition: transform 0.3s !important;
            cursor: pointer !important;
        }}
        div[data-testid="stHorizontalBlock"]:nth-of-type(2) button:hover {{ transform: scale(1.05) !important; }}
    </style>
    """, unsafe_allow_html=True)

    st.write("\n" * 4) 
    st.markdown(f"""
        <div style="display: flex; justify-content: center; align-items: center; margin-bottom: 30px;">
            <img src="{logo_b64}" style="max-width: 700px; height: auto;">
        </div>
    """, unsafe_allow_html=True)
    
    # -----------------------------------------------------
    # BLOCO 1: Saiba Mais (As proporções 2, 1, 2 resolvem o tamanho)
    # -----------------------------------------------------
    col1, col_centro, col3 = st.columns([2, 1, 2])
    with col_centro:
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
