import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import base64

# --- CONFIGURAÇÃO INICIAL ---
st.set_page_config(page_title="Fake Wonka", page_icon="🍫", layout="wide", initial_sidebar_state="collapsed")

# --- BASE DE DADOS SIMULADA ---
dados_alimentos = pd.DataFrame({
    "Alimento": ["Chocolate ao Leite", "Salsicha", "Suco de Caixinha", "Biscoito Recheado"],
    "Resumo": ["Atenção: Possíveis traços de metais pesados.", "Atenção: Risco de Listeria no lote atual.", "Atenção: Alto índice de micotoxinas.", "Atenção: Excesso de corantes artificiais banidos."],
    "Risco_Pct": [85, 92, 45, 78],
    "Calorias": ["535 kcal", "300 kcal", "45 kcal", "480 kcal"],
    "Carboidratos": ["59g", "2g", "11g", "68g"],
    "Proteinas": ["7g", "12g", "0g", "5g"]
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
botao_home_b64 = carregar_imagem_base64("botao_home.png")
botao_voltar_b64 = carregar_imagem_base64("botao_voltar.png")
botao_pesquisa_b64 = carregar_imagem_base64("botao_pesquisa.png") 

# --- GERENCIADOR DE ESTADO ---
if 'pagina_atual' not in st.session_state:
    st.session_state['pagina_atual'] = 'home'
    
if 'alimento_selecionado' not in st.session_state:
    st.session_state['alimento_selecionado'] = None

# ==========================================
# CSS GLOBAL E BARRA DE PESQUISA (Blindada)
# ==========================================
st.markdown(f"""
<style>
    .stApp {{ background-color: #301f1b; color: #F8F3E6; }}
    [data-testid="collapsedControl"] {{ display: none; }}
    header {{ visibility: hidden; }}
            
    div[data-baseweb="input"], div[data-baseweb="base-input"] {{ background-color: transparent !important; border: none !important; }}
    .stTextInput input {{ 
        background-color: #E2C792 !important; 
        color: black !important; 
        border-radius: 30px !important; 
        padding: 12px 20px 12px 55px !important; 
        border: none !important; 
        box-shadow: none !important; 
        background-image: url('{botao_pesquisa_b64}') !important;
        background-repeat: no-repeat !important;
        background-position: 15px center !important;
        background-size: 25px !important; 
    }}
    .stTextInput input::placeholder {{ color: #5c4033 !important; }}
</style>
""", unsafe_allow_html=True)


# ==========================================
# TELA 1: HOME
# ==========================================
if st.session_state['pagina_atual'] == 'home':
    st.markdown(f"""
    <style>
        /* Primary = Saiba Mais */
        button[kind="primary"], button[kind="primary"]:hover, button[kind="primary"]:active, button[kind="primary"]:focus, button[kind="primary"]:disabled {{
            background: transparent url('{botao_saiba_mais_b64}') center / contain no-repeat !important; border: none !important; box-shadow: none !important;
            height: 70px !important; width: 100% !important; transition: transform 0.3s !important; outline: none !important; opacity: 1 !important;
        }}
        button[kind="primary"] * {{ display: none !important; }}
        button[kind="primary"]:hover {{ transform: scale(1.05) !important; }}

        /* Secondary = Sobre Nós */
        button[kind="secondary"], button[kind="secondary"]:hover, button[kind="secondary"]:active, button[kind="secondary"]:focus, button[kind="secondary"]:disabled {{
            background: transparent url('{botao_sobre_nos_b64}') right center / contain no-repeat !important; border: none !important; box-shadow: none !important;
            height: 45px !important; width: 180px !important; position: fixed !important; bottom: 30px !important; right: 30px !important; z-index: 999 !important; transition: transform 0.3s !important; outline: none !important; opacity: 1 !important;
        }}
        button[kind="secondary"] * {{ display: none !important; }}
        button[kind="secondary"]:hover {{ transform: scale(1.05) !important; }}
    </style>
    """, unsafe_allow_html=True)

    st.write("\n" * 4)  
    st.markdown(f"""<div style="display: flex; justify-content: center; align-items: center; margin-bottom: 30px;">
        <img src="{logo_b64}" style="max-width: 700px; height: auto;"></div>""", unsafe_allow_html=True)
    
    col1, col_centro, col3 = st.columns([2, 1, 2])
    with col_centro:
        if st.button(" ", type="primary", use_container_width=True):
            st.session_state['pagina_atual'] = 'catalogo'
            st.rerun()

    if st.button(" ", type="secondary"):
        st.session_state['pagina_atual'] = 'sobre'
        st.rerun()


# ==========================================
# TELA 2: SOBRE NÓS
# ==========================================
elif st.session_state['pagina_atual'] == 'sobre':
    
    # CSS: O Secondary desta página é o Botão Home
    st.markdown(f"""
    <style>
        button[kind="secondary"], button[kind="secondary"]:hover, button[kind="secondary"]:active, button[kind="secondary"]:focus, button[kind="secondary"]:disabled {{
            background: transparent url('{botao_home_b64}') center / contain no-repeat !important;
            border: none !important; box-shadow: none !important; height: 60px !important; width: 60px !important; border-radius: 50% !important; color: transparent !important; transition: transform 0.2s !important; opacity: 1 !important; outline: none !important; 
            display: block !important; margin-left: auto !important; /* Empurra para a direita */
        }}
        button[kind="secondary"] * {{ display: none !important; }}
        button[kind="secondary"]:hover {{ transform: scale(1.1) !important; }}
    </style>
    """, unsafe_allow_html=True)

    col_logo, col_vazia, col_voltar = st.columns([1, 6, 1])
    with col_logo:
        st.markdown(f'<img src="{logo_b64}" style="max-height: 250px;">', unsafe_allow_html=True)
    with col_voltar:
        # Repare no type="secondary"
        if st.button(" ", key="btn_sobre_home", type="secondary"):
            st.session_state['pagina_atual'] = 'home'
            st.rerun()

    st.write("\n" * 2)
    col_esq, col_meio, col_dir = st.columns([1, 1.5, 1])

    with col_esq:
        st.markdown("""<div style="background-color: #E2C792; border-radius: 15px; padding: 25px; text-align: center; color: #21130d; font-weight: bold; font-size: 24px; margin-bottom: 15px;">Missão</div>
        <div style="background-color: #7B4E31; border-radius: 15px; padding: 25px; text-align: center; color: white; font-weight: bold; font-size: 24px; margin-bottom: 15px;">Visão</div>
        <div style="background-color: #E2C792; border-radius: 15px; padding: 25px; text-align: center; color: #21130d; font-weight: bold; font-size: 24px;">Valores</div>""", unsafe_allow_html=True)

    with col_meio:
        st.markdown(f"""<div style="background-color: #7B4E31; border-radius: 15px; padding: 20px; text-align: center; height: 100%; min-height: 250px; display: flex; align-items: center; justify-content: center;">
            <img src="{foto_equipe_b64}" style="max-width: 90%; border-radius: 10px;" alt="Foto do Grupo"></div>""", unsafe_allow_html=True)

    with col_dir:
        st.markdown("""<div style="background-color: #E2C792; border-radius: 15px; padding: 30px; text-align: center; color: #21130d; font-weight: bold; height: 100%; min-height: 250px; display: flex; align-items: center; justify-content: center; font-size: 20px;">
            Descrição sobre<br>o grupo</div>""", unsafe_allow_html=True)


# ==========================================
# TELA 3: CATÁLOGO E PESQUISA
# ==========================================
elif st.session_state['pagina_atual'] == 'catalogo':
    
    # CSS: Secondary = Botão Voltar (Seta), Primary = Botões do Catálogo
    st.markdown(f"""
    <style>
        /* O Botão do Topo */
        button[kind="secondary"], button[kind="secondary"]:hover, button[kind="secondary"]:active, button[kind="secondary"]:focus, button[kind="secondary"]:disabled {{
            background: transparent url('{botao_home_b64}') center / contain no-repeat !important;
            border: none !important; box-shadow: none !important; height: 60px !important; width: 60px !important; border-radius: 50% !important; color: transparent !important; transition: transform 0.2s !important; opacity: 1 !important; outline: none !important; 
            display: block !important; margin-left: auto !important;
        }}
        button[kind="secondary"] * {{ display: none !important; }}
        button[kind="secondary"]:hover {{ transform: scale(1.1) !important; }}
        
        /* Os Botões dos Alimentos (Não escondemos o texto neste!) */
        button[kind="primary"], button[kind="primary"]:active, button[kind="primary"]:focus, button[kind="primary"]:disabled {{ 
            background-color: #C69C26 !important; color: #21130d !important; font-weight: bold !important; border-radius: 15px !important; border: none !important; width: 100% !important; opacity: 1 !important; outline: none !important; 
        }}
        button[kind="primary"]:hover {{ background-color: #E2C792 !important; color: black !important; }}
    </style>
    """, unsafe_allow_html=True)

    col_logo, col_vazia, col_voltar = st.columns([1, 6, 1])
    with col_logo:
        st.markdown(f'<img src="{logo_b64}" style="max-height: 250px;">', unsafe_allow_html=True)
    with col_voltar:
        # Repare no type="secondary"
        if st.button(" ", key="btn_cat_voltar", type="secondary"):
            st.session_state['pagina_atual'] = 'home'
            st.rerun()

    st.write("\n")
    col_espaco1, col_busca, col_espaco2 = st.columns([1, 2, 1])
    with col_busca:
        busca = st.text_input("Buscar", placeholder="Pesquise aqui...", label_visibility="collapsed")
    
    st.write("\n" * 2)

    resultados = dados_alimentos[dados_alimentos["Alimento"].str.contains(busca, case=False)] if busca else dados_alimentos

    if not resultados.empty:
        for index, row in resultados.iterrows():
            card_html = f"""
            <div style="display: flex; gap: 15px; margin-bottom: 5px; align-items: stretch; justify-content: center;">
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
            
            col_esp, col_btn = st.columns([0.25, 0.6])
            with col_btn:
                # Botão Primary ganha a formatação dourada que fizemos no CSS desta página
                if st.button(f"🔍 Abrir Dossiê de Análise", key=f"btn_{index}", type="primary"):
                    st.session_state['alimento_selecionado'] = row
                    st.session_state['pagina_atual'] = 'descricao'
                    st.rerun()
            st.write("---") 
    else:
        st.markdown("<p style='text-align: center; color: #E2C792;'>Nenhum alimento encontrado.</p>", unsafe_allow_html=True)


# ==========================================
# TELA 4: DESCRIÇÃO DO PRODUTO 
# ==========================================
elif st.session_state['pagina_atual'] == 'descricao':
    
    # CSS: O Secondary desta página é o Botão de Pesquisa (Lupa)
    st.markdown(f"""
    <style>
        button[kind="secondary"], button[kind="secondary"]:hover, button[kind="secondary"]:active, button[kind="secondary"]:focus, button[kind="secondary"]:disabled {{
            background: transparent url('{botao_pesquisa_b64}') center / contain no-repeat !important;
            border: none !important; box-shadow: none !important; height: 60px !important; width: 60px !important; border-radius: 50% !important; color: transparent !important; transition: transform 0.2s !important; opacity: 1 !important; outline: none !important; 
            display: block !important; margin-left: auto !important;
        }}
        button[kind="secondary"] * {{ display: none !important; }}
        button[kind="secondary"]:hover {{ transform: scale(1.1) !important; }}
    </style>
    """, unsafe_allow_html=True)

    alimento = st.session_state['alimento_selecionado']

    col_logo, col_vazia, col_voltar = st.columns([1, 6, 1])
    with col_logo:
        st.markdown(f'<img src="{logo_b64}" style="max-height: 250px;">', unsafe_allow_html=True)
    with col_voltar:
        # Repare no type="secondary"
        if st.button(" ", key="btn_desc_pesquisa", type="secondary"):
            st.session_state['pagina_atual'] = 'catalogo'
            st.rerun()

    st.write("\n")
    st.markdown(f"<h2 style='text-align: center; color: #E2C792;'>Análise: {alimento['Alimento']}</h2>", unsafe_allow_html=True)

    pct_risco = alimento['Risco_Pct']
    fig = go.Figure(go.Pie(
        values=[pct_risco, 100 - pct_risco],
        labels=["Índice de Risco", "Segurança"],
        hole=0.75, 
        marker_colors=["#C00000", "#4A2F24"], 
        textinfo='none', 
        hoverinfo='label+percent'
    ))
    
    fig.update_layout(
        showlegend=False, paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)',
        margin=dict(t=0, b=0, l=0, r=0), height=300,
        annotations=[dict(text=f"{pct_risco}%", x=0.5, y=0.5, font_size=50, font_color="#E2C792", showarrow=False, font_family="serif")]
    )
    st.plotly_chart(fig, use_container_width=True)

    st.write("\n")
    col_info, col_nutri = st.columns([1, 1])

    with col_info:
        st.markdown(f"""
        <div style="background-color: #7B4E31; border-radius: 15px; padding: 30px; height: 100%; min-height: 280px; color: white;">
            <h4 style="color: #E2C792; margin-top: 0;">Informações do Produto</h4>
            <p style="font-size: 16px;">{alimento['Resumo']}</p>
            <p><strong>Nível de Alerta:</strong> Crítico devido ao modelo de produção industrial padrão.</p>
        </div>
        """, unsafe_allow_html=True)

    with col_nutri:
        st.markdown(f"""
        <div style="background-color: #E2C792; border-radius: 15px; padding: 25px; color: black; font-family: Arial, sans-serif; height: 100%; min-height: 280px;">
            <h4 style="margin: 0; text-align: center; border-bottom: 2px solid black; padding-bottom: 5px;">INFORMAÇÃO NUTRICIONAL</h4>
            <p style="margin: 5px 0; font-size: 14px;">Porção de 100g</p>
            <table style="width: 100%; border-collapse: collapse; font-size: 14px; margin-top: 10px;">
                <tr style="border-bottom: 1px solid #7B4E31;">
                    <td style="padding: 5px 0;"><strong>Valor Energético</strong></td>
                    <td style="text-align: right;">{alimento['Calorias']}</td>
                </tr>
                <tr style="border-bottom: 1px solid #7B4E31;">
                    <td style="padding: 5px 0;"><strong>Carboidratos</strong></td>
                    <td style="text-align: right;">{alimento['Carboidratos']}</td>
                </tr>
                <tr style="border-bottom: 1px solid #7B4E31;">
                    <td style="padding: 5px 0;"><strong>Proteínas</strong></td>
                    <td style="text-align: right;">{alimento['Proteinas']}</td>
                </tr>
            </table>
        </div>
        """, unsafe_allow_html=True)
