import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import base64

# --- Configuração da aba no navegador ---
st.set_page_config(page_title="Fake Wonka", page_icon="🍫", layout="wide", initial_sidebar_state="collapsed")

# --- Carregar o banco de dados ---
@st.cache_data
def carregar_dados():
    return pd.read_excel("banco_alimentos.xlsx")

dados_alimentos = carregar_dados()

def carregar_imagem_base64(caminho):
    try:
        with open(caminho, "rb") as image_file:
            encoded = base64.b64encode(image_file.read()).decode()
            return f"data:image/png;base64,{encoded}"
    except FileNotFoundError:
        # Retorna um pixel transparente se a imagem do produto não for encontrada
        return "data:image/gif;base64,R0lGODlhAQABAAD/ACwAAAAAAQABAAACADs="

# --- Carregamento das imagens ---
logo_b64 = carregar_imagem_base64("logo_sem_fundo.png")
botao_saiba_mais_b64 = carregar_imagem_base64("botao_saiba_mais.png")
botao_sobre_nos_b64 = carregar_imagem_base64("botao_sobre_nos.png")
foto_equipe_b64 = carregar_imagem_base64("foto_equipe.png")
botao_home_b64 = carregar_imagem_base64("botao_home.png")
botao_voltar_b64 = carregar_imagem_base64("botao_voltar.png")
botao_pesquisa_b64 = carregar_imagem_base64("botao_pesquisa.png")
botao_ver_produto_b64 = carregar_imagem_base64("botao_ver_produto.png") 

# --- Gerenciamento de estado ---
if 'pagina_atual' not in st.session_state:
    st.session_state['pagina_atual'] = 'home'
    
if 'alimento_selecionado' not in st.session_state:
    st.session_state['alimento_selecionado'] = None

# ==========================================
# CSS GLOBAL E BARRA DE PESQUISA
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
            background-color: transparent !important;
            background-image: url('{botao_saiba_mais_b64}') !important;
            background-size: contain !important;
            background-repeat: no-repeat !important;
            background-position: center !important;
            border: none !important; box-shadow: none !important;
            height: 70px !important; width: 100% !important; transition: transform 0.3s !important; outline: none !important; opacity: 1 !important;
        }}
        button[kind="primary"] * {{ display: none !important; }}
        button[kind="primary"]:hover {{ transform: scale(1.05) !important; }}

        /* Secondary = Sobre Nós */
        button[kind="secondary"], button[kind="secondary"]:hover, button[kind="secondary"]:active, button[kind="secondary"]:focus, button[kind="secondary"]:disabled {{
            background-color: transparent !important;
            background-image: url('{botao_sobre_nos_b64}') !important;
            background-size: contain !important;
            background-repeat: no-repeat !important;
            background-position: right center !important;
            border: none !important; box-shadow: none !important;
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
            # AGORA ELE VAI PARA A PÁGINA INTERMEDIÁRIA
            st.session_state['pagina_atual'] = 'manifesto' 
            st.rerun()


    if st.button(" ", type="secondary"):
        st.session_state['pagina_atual'] = 'sobre'
        st.rerun()

# ==========================================
# TELA INTERMEDIÁRIA: ADMINISTRAÇÃO E INDÚSTRIA
# ==========================================
elif st.session_state['pagina_atual'] == 'manifesto':
    
    st.markdown(f"""
    <style>
        /* Botão Secundário para o botão de Voltar (Seta) */
        button[kind="secondary"], button[kind="secondary"]:hover, button[kind="secondary"]:active, button[kind="secondary"]:focus, button[kind="secondary"]:disabled {{
            background: transparent url('{botao_voltar_b64}') center / contain no-repeat !important;
            border: none !important; box-shadow: none !important; height: 60px !important; width: 60px !important; border-radius: 50% !important; color: transparent !important; transition: transform 0.2s !important; opacity: 1 !important; outline: none !important; 
            display: block !important; margin-left: auto !important;
        }}
        button[kind="secondary"] * {{ display: none !important; }}
        button[kind="secondary"]:hover {{ transform: scale(1.1) !important; }}
        
        /* Botão Primário para avançar ao Catálogo */
        button[kind="primary"], button[kind="primary"]:active, button[kind="primary"]:focus, button[kind="primary"]:disabled {{ 
            background-color: #C69C26 !important; color: #21130d !important; font-weight: bold !important; font-size: 18px !important; border-radius: 15px !important; border: none !important; width: 100% !important; height: 60px !important; opacity: 1 !important; outline: none !important; 
        }}
        button[kind="primary"]:hover {{ background-color: #E2C792 !important; color: black !important; transform: scale(1.02) !important; transition: transform 0.2s !important;}}
    </style>
    """, unsafe_allow_html=True)


    col_vazia1, col_logo, col_voltar = st.columns([1, 6, 1])
    with col_logo:
        # A logo menor centralizada
        st.markdown(f'<div style="text-align: center;"><img src="{logo_b64}" style="max-height: 120px;"></div>', unsafe_allow_html=True)
    with col_voltar:
        if st.button(" ", key="btn_manifesto_voltar", type="secondary"):
            st.session_state['pagina_atual'] = 'home'
            st.rerun()

    st.write("\n")


    texto_admin = f"""
    <div style="background-color: #E2C792; border-radius: 15px; padding: 40px; color: #21130d; height: 450px; overflow-y: auto; box-shadow: inset 0 0 15px rgba(0,0,0,0.3); text-align: justify; font-family: Arial, sans-serif; line-height: 1.6; margin-bottom: 30px;">
        
        <h2 style="text-align: center; border-bottom: 2px solid #7B4E31; padding-bottom: 10px; margin-top: 0;">A Ilusão Industrial e a Gestão</h2>
        
        <p><strong>A Cultura Organizacional do Lucro:</strong> Em um ambiente empresarial onde as margens de lucro ditam as regras, a indústria alimentícia adotou conceitos da Teoria Clássica e do Fordismo para otimizar suas linhas de produção. O resultado? A substituição de comida real por fórmulas químicas ultraprocessadas, focadas em baratear o custo e estender a vida útil nas prateleiras.</p>
        
        <p><strong>Marketing e Análise Comportamental:</strong> Utilizando princípios da Abordagem Comportamental, as empresas desenham embalagens e campanhas publicitárias que criam gatilhos psicológicos no consumidor. Eles mascaram produtos nocivos à saúde sob a roupagem de "produtos enriquecidos com vitaminas" ou "opções práticas para o dia a dia", manipulando a percepção de valor.</p>
        
        <p><strong>Teoria Contingencial e o Ambiente Externo:</strong> Como essas indústrias sobrevivem às novas leis da Anvisa sobre rotulagem? Através da adaptação contingencial. Elas alteram superficialmente suas fórmulas apenas o suficiente para evitar os selos pretos de alerta de alto teor de sódio ou açúcares, sem mudar a essência ultraprocessada do produto.</p>
        
        <p>O nosso catálogo a seguir é uma ferramenta de auditoria. Vamos expor, produto por produto, o que os relatórios e táticas de gestão dessas empresas não querem que você veja.</p>
        
        <br><br><p style="opacity: 0.5; text-align: center;">[Role para baixo para continuar lendo...]</p><br><br>
        <p>Ao analisar a administração moderna, percebemos que a ética e a responsabilidade social corporativa (RSC) muitas vezes ficam em segundo plano. A gestão estratégica dessas marcas prioriza o acionista em detrimento do consumidor. Este projeto visa aplicar o senso crítico da administração para desmontar essa cadeia de manipulação alimentar.</p>

    </div>
    
    <style>
        /* Estilizando a barra de rolagem nativa para combinar com o site */
        div[style*="overflow-y: auto"]::-webkit-scrollbar {{
            width: 10px;
        }}
        div[style*="overflow-y: auto"]::-webkit-scrollbar-track {{
            background: #d1b57c; 
            border-radius: 10px;
        }}
        div[style*="overflow-y: auto"]::-webkit-scrollbar-thumb {{
            background: #7B4E31; 
            border-radius: 10px;
        }}
        div[style*="overflow-y: auto"]::-webkit-scrollbar-thumb:hover {{
            background: #5c4033; 
        }}
    </style>
    """
    
    col_espaco_esq, col_caixa, col_espaco_dir = st.columns([1, 4, 1])
    with col_caixa:
        # Renderiza a caixa com scroll numa linha só de HTML
        st.markdown(texto_admin.replace('\n', ''), unsafe_allow_html=True)
        
        # Botão para ir para o catálogo final
        if st.button("Acessar o Catálogo de Produtos ➡️", type="primary", use_container_width=True):
            st.session_state['pagina_atual'] = 'catalogo'
            st.rerun()




# ==========================================
# TELA 2: SOBRE NÓS
# ==========================================
elif st.session_state['pagina_atual'] == 'sobre':
    
    st.markdown(f"""
    <style>
        button[kind="secondary"], button[kind="secondary"]:hover, button[kind="secondary"]:active, button[kind="secondary"]:focus, button[kind="secondary"]:disabled {{
            background-color: transparent !important;
            background-image: url('{botao_home_b64}') !important;
            background-size: contain !important;
            background-repeat: no-repeat !important;
            background-position: center !important;
            border: none !important; box-shadow: none !important; height: 60px !important; width: 60px !important; border-radius: 50% !important; color: transparent !important; transition: transform 0.2s !important; opacity: 1 !important; outline: none !important; 
            display: block !important; margin-left: auto !important;
        }}
        button[kind="secondary"] * {{ display: none !important; }}
        button[kind="secondary"]:hover {{ transform: scale(1.1) !important; }}
    </style>
    """, unsafe_allow_html=True)

    col_logo, col_vazia, col_voltar = st.columns([1, 6, 1])
    with col_logo:
        st.markdown(f'<img src="{logo_b64}" style="max-height: 250px;">', unsafe_allow_html=True)
    with col_voltar:
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
    
    st.markdown(f"""
    <style>
        /* O Botão do Topo (Voltar) */
        button[kind="secondary"], button[kind="secondary"]:hover, button[kind="secondary"]:active, button[kind="secondary"]:focus, button[kind="secondary"]:disabled {{
            background-color: transparent !important;
            background-image: url('{botao_voltar_b64}') !important;
            background-size: contain !important;
            background-repeat: no-repeat !important;
            background-position: center !important;
            border: none !important; box-shadow: none !important; height: 60px !important; width: 60px !important; border-radius: 50% !important; color: transparent !important; transition: transform 0.2s !important; opacity: 1 !important; outline: none !important; 
            display: block !important; margin-left: auto !important;
        }}
        button[kind="secondary"] * {{ display: none !important; }}
        button[kind="secondary"]:hover {{ transform: scale(1.1) !important; }}
        
        /* O Novo Botão de Ver Produto (Retangular) */
        button[kind="primary"], button[kind="primary"]:active, button[kind="primary"]:focus, button[kind="primary"]:disabled {{ 
            background-color: transparent !important;
            background-image: url('{botao_ver_produto_b64}') !important;
            background-size: contain !important;
            background-repeat: no-repeat !important;
            background-position: center !important;
            border: none !important; box-shadow: none !important; 
            height: 50px !important; 
            width: 100% !important; /* Estica para preencher a coluna inteira */
            color: transparent !important; transition: transform 0.2s !important; opacity: 1 !important; outline: none !important; 
            display: block !important; margin: 0 auto !important;
        }}
        button[kind="primary"]:hover {{ transform: scale(1.05) !important; }}
    </style>
    """, unsafe_allow_html=True)

    col_logo, col_vazia, col_voltar = st.columns([1, 6, 1])
    with col_logo:
        st.markdown(f'<img src="{logo_b64}" style="max-height: 250px;">', unsafe_allow_html=True)
    with col_voltar:
        if st.button(" ", key="btn_cat_voltar", type="secondary"):
            st.session_state['pagina_atual'] = 'home'
            st.rerun()

    st.write("\n")
    col_espaco1, col_busca, col_espaco2 = st.columns([1, 2, 1])
    with col_busca:
        busca = st.text_input("Buscar", placeholder="Pesquise aqui...", label_visibility="collapsed")
    
    st.write("\n" * 2)

    # Filtro de maiusculas ou minusculas
    resultados = dados_alimentos[dados_alimentos["Alimento"].str.contains(busca, case=False, na=False)] if busca else dados_alimentos

    if not resultados.empty:
        for index, row in resultados.iterrows():
            # Converte a imagem do produto para exibir no card
            foto_produto_b64 = carregar_imagem_base64(str(row['Caminho_Imagem']))
            
            card_html = f"""
            <div style="display: flex; gap: 15px; margin-bottom: 5px; align-items: stretch; justify-content: center;">
                <div style="background-color: #E2C792; border-radius: 15px; width: 25%; padding: 10px; text-align: center; color: #21130d; display: flex; align-items: center; justify-content: center; min-height: 120px;">
                    <img src="{foto_produto_b64}" style="max-height: 100px; max-width: 100%; border-radius: 10px; object-fit: contain;">
                </div>
                <div style="background-color: #7B4E31; border-radius: 15px; width: 60%; padding: 20px; color: white; display: flex; flex-direction: column; justify-content: center;">
                    <h4 style="margin: 0; color: #E2C792;">{row['Alimento']}</h4>
                    <p style="margin: 5px 0 0 0; font-size: 14px;">{row['Descricao']}</p>
                </div>
            </div>
            """
            st.markdown(card_html, unsafe_allow_html=True)
            
            col_esp, col_btn = st.columns([0.25, 0.6])
            with col_btn:
                
                if st.button(" ", key=f"btn_{index}", type="primary", use_container_width=True):
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
        if st.button(" ", key="btn_desc_pesquisa", type="secondary"):
            st.session_state['pagina_atual'] = 'catalogo'
            st.rerun()

    st.write("\n")
    st.markdown(f"<h2 style='text-align: center; color: #E2C792;'>Análise: {alimento['Alimento']}</h2>", unsafe_allow_html=True)

    # Grafico de Rosca
    pct_risco = float(alimento['Nivel_Risco_Pct'])
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
        annotations=[dict(text=f"{int(pct_risco)}%", x=0.5, y=0.5, font_size=50, font_color="#E2C792", showarrow=False, font_family="serif")]
    )
    st.plotly_chart(fig, use_container_width=True)

    st.write("\n")
    col_info, col_nutri = st.columns([1, 1])

    def valor_nutri(coluna):
        val = alimento.get(coluna)
        return val if pd.notna(val) else "Informação não disponível"

    with col_info:
        
        html_info = f"""<div style="background-color: #7B4E31; border-radius: 15px; padding: 30px; height: 100%; min-height: 380px; color: white;">
<h4 style="color: #E2C792; margin-top: 0;">Informações do Produto</h4>
<p style="font-size: 16px;">{valor_nutri('Descricao')}</p>
<br>
<h4 style="color: #C00000; margin-top: 0;">⚠️ Laudo de Alerta Industrial</h4>
<p style="font-size: 15px; line-height: 1.4;">{valor_nutri('Alerta_Riscos')}</p>
</div>"""
        st.markdown(html_info, unsafe_allow_html=True)

    with col_nutri:
        mapa_nutrientes = [
            ('Valor_Energético', 'Valor Energético', True, 0),
            ('Carboidratos', 'Carboidratos', True, 0),
            ('Açúcares_Totais', 'Açúcares Totais', False, 15),
            ('Açúcares_Adicionados', 'Açúcares Adicionados', False, 15),
            ('Proteínas', 'Proteínas', True, 0),
            ('Gorduras_Totais', 'Gorduras Totais', True, 0),
            ('Gorduras Saturadas', 'Gorduras Saturadas', False, 15),
            ('Gorduras_Trans', 'Gorduras Trans', False, 15),
            ('Fibra Alimentar', 'Fibra Alimentar', True, 0),
            ('Sódio', 'Sódio', True, 0),
            ('Cálcio', 'Cálcio', False, 0),
            ('Ferro', 'Ferro', False, 0),
            ('Vitamina A', 'Vitamina A', False, 0),
            ('Vitamina C', 'Vitamina C', False, 0),
            ('Ácido Fólico', 'Ácido Fólico', False, 0)
        ]

        linhas_html = ""
        for col_excel, nome_exibicao, is_bold, recuo in mapa_nutrientes:
            if col_excel in alimento and pd.notna(alimento[col_excel]):
                valor = str(alimento[col_excel]).strip()
                peso_fonte = "bold" if is_bold else "normal"
                cor_fonte = "#21130d" if is_bold else "#4A2F24"
                
                # Geração da linha da tabela nutricional
                linhas_html += f'<tr style="border-bottom: 1px solid #7B4E31;"><td style="padding: 4px 0 4px {recuo}px; font-weight: {peso_fonte}; color: {cor_fonte};">{nome_exibicao}</td><td style="text-align: right;">{valor}</td></tr>'

        porcao_texto = alimento.get('Porcao') if pd.notna(alimento.get('Porcao')) else "Porção não informada"

        # Tabela completa montada em bloco linear
        html_tabela = f'<div style="background-color: #E2C792; border-radius: 15px; padding: 25px; color: black; font-family: Arial, sans-serif; height: 100%; min-height: 380px; box-shadow: inset 0 0 10px rgba(0,0,0,0.1);"><h4 style="margin: 0; text-align: center; border-bottom: 2px solid black; padding-bottom: 5px;">INFORMAÇÃO NUTRICIONAL</h4><p style="margin: 5px 0; font-size: 14px; text-align: center; font-weight: bold;">{porcao_texto}</p><table style="width: 100%; border-collapse: collapse; font-size: 13px; margin-top: 10px;">{linhas_html}</table></div>'
        
        st.markdown(html_tabela, unsafe_allow_html=True)
