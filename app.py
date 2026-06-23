import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import base64
import textwrap

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
botao_acessar_catalogo_b64 = carregar_imagem_base64("botao_acessar_catalogo.png")

# --- Gerenciamento de estado ---
if 'pagina_atual' not in st.session_state:
    st.session_state['pagina_atual'] = 'home'
    
if 'alimento_selecionado' not in st.session_state:
    st.session_state['alimento_selecionado'] = None

# NOVO ESTADO: Memória para a tela Sobre Nós
if 'aba_sobre' not in st.session_state:
    st.session_state['aba_sobre'] = 'missao'

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
    
    /* Scrollbar customizada global para caixas de texto */
    div[style*="overflow-y: auto"]::-webkit-scrollbar {{ width: 10px; }}
    div[style*="overflow-y: auto"]::-webkit-scrollbar-track {{ background: #d1b57c; border-radius: 10px; }}
    div[style*="overflow-y: auto"]::-webkit-scrollbar-thumb {{ background: #7B4E31; border-radius: 10px; }}
    div[style*="overflow-y: auto"]::-webkit-scrollbar-thumb:hover {{ background: #5c4033; }}
</style>
""", unsafe_allow_html=True)


# ==========================================
# TELA 1: HOME
# ==========================================
if st.session_state['pagina_atual'] == 'home':
    st.markdown(f"""
    <style>
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
            st.session_state['pagina_atual'] = 'desclaimer' 
            st.rerun()

    if st.button(" ", type="secondary"):
        st.session_state['pagina_atual'] = 'sobre'
        st.rerun()

# ==========================================
# TELA DESCLAIMER: CONEXÃO COM INT ADM
# ==========================================
elif st.session_state['pagina_atual'] == 'desclaimer':
    
    st.markdown(f"""
    <style>
        button[kind="secondary"], button[kind="secondary"]:hover, button[kind="secondary"]:active, button[kind="secondary"]:focus, button[kind="secondary"]:disabled {{
            background: transparent url('{botao_voltar_b64}') center / contain no-repeat !important;
            border: none !important; box-shadow: none !important; height: 60px !important; width: 60px !important; border-radius: 50% !important; color: transparent !important; transition: transform 0.2s !important; opacity: 1 !important; outline: none !important; 
            display: block !important; margin-left: auto !important;
        }}
        button[kind="secondary"] * {{ display: none !important; }}
        button[kind="secondary"]:hover {{ transform: scale(1.1) !important; }}
        
        button[kind="primary"], button[kind="primary"]:hover, button[kind="primary"]:active, button[kind="primary"]:focus, button[kind="primary"]:disabled {{ 
            background-color: transparent !important;
            background-image: url('{botao_acessar_catalogo_b64}') !important;
            background-size: contain !important;
            background-repeat: no-repeat !important;
            background-position: center !important;
            border: none !important; box-shadow: none !important; 
            width: 100% !important; height: 70px !important; opacity: 1 !important; outline: none !important; 
            display: block !important; margin: 0 auto !important; color: transparent !important;
        }}
        button[kind="primary"] * {{ display: none !important; }}
        button[kind="primary"]::before, button[kind="primary"]::after {{ display: none !important; background: transparent !important; }}
        button[kind="primary"]:hover {{ transform: scale(1.02) !important; }}
    </style>
    """, unsafe_allow_html=True)


    col_vazia1, col_logo, col_voltar = st.columns([1, 6, 1])
    with col_logo:
        st.markdown(f'<div style="text-align: center;"><img src="{logo_b64}" style="max-height: 120px;"></div>', unsafe_allow_html=True)
    with col_voltar:
        if st.button(" ", key="btn_manifesto_voltar", type="secondary"):
            st.session_state['pagina_atual'] = 'home'
            st.rerun()

    st.write("\n")

    # texto do Desclaimer
    texto_admin = f"""
    <div style="background-color: #E2C792; border-radius: 15px; padding: 40px; color: #21130d; height: 400px; overflow-y: auto; box-shadow: inset 0 0 15px rgba(0,0,0,0.3); text-align: justify; font-family: Arial, sans-serif; line-height: 1.6; margin-bottom: 30px;">
        
        <h2 style="text-align: center; border-bottom: 2px solid #7B4E31; padding-bottom: 10px; margin-top: 0;">O que é esse projeto</h2>
        
        <p> O nosso projeto deu-se inicio quando notamos que as empresas começaram a dotar certos meios de burlar o sistema alimentar utilizando metodos administrativos como:</p>

        <p><strong>A Cultura Organizacional do Lucro:</strong> Em um ambiente empresarial onde as margens de lucro ditam as regras, a indústria alimentícia adotou conceitos da Teoria Clássica e do Fordismo para otimizar suas linhas de produção. O resultado? A substituição de comida real por fórmulas químicas ultraprocessadas, focadas em baratear o custo e estender a vida útil nas prateleiras.</p>
        
        <p><strong>Marketing e Análise Comportamental:</strong> Utilizando princípios da Abordagem Comportamental, as empresas desenham embalagens e campanhas publicitárias que criam gatilhos psicológicos no consumidor. Eles mascaram produtos nocivos à saúde sob a roupagem de "produtos enriquecidos com vitaminas" ou "opções práticas para o dia a dia", manipulando a percepção de valor.</p>
        
        <p><strong>Teoria Contingencial e o Ambiente Externo:</strong> Como essas indústrias sobrevivem às novas leis da Anvisa sobre rotulagem? Através da adaptação contingencial. Elas alteram superficialmente suas fórmulas apenas o suficiente para evitar os selos pretos de alerta de alto teor de sódio ou açúcares, sem mudar a essência ultra processada do produto.</p>
        
        <p>O nosso catálogo a seguir é uma ferramenta de auditoria. Vamos expor, produto por produto, o que os relatórios e táticas de gestão dessas empresas não querem que você veja, ultilizando um metodo proprio de calculo de risco com a seguinte formula:</p>

        <p><strong>O indicie se baseia nos seguintes critérios:</strong> </p>

        <p><strong>1. Pontos de Nutrientes Críticos (Até 100 pontos)</strong> Olhamos para o rótulo do produto e calculamos o quanto os nutrientes daquela porção consomem da meta diária recomendada pela OMS (Organização Mundial da Saúde):</p>

        <li>Sódio (Vale até 40 pontos): Meta da OMS é < 2000mg/dia.</li>
        
        <li>Gordura Saturada (Vale até 40 pontos): Meta da OMS é < 22g/dia.</li>

        <li>Açúcares Adicionados (Vale até 20 pontos): Meta da OMS é < 50g/dia.</li>
        

        <p><strong>2. O Multiplicador Ultraprocessado (x1,5)</strong> Se o alimento for um ultraprocessado comercial (Classificação NOVA 4), nós pegamos os pontos do passo anterior e multiplicamos por 1,5. Isso serve para o algoritmo penalizar a engenharia química do produto e a velocidade com que o corpo absorve essa gordura e açúcar.</p>

        <p><strong>3. O Pedágio de Aditivos (+15 pontos fixos)</strong> Se na lista de ingredientes houver conservantes pesados, corantes ou realçadores de sabor (como os nitritos dos embutidos ou o glutamato do Doritos), o sistema soma +15 pontos de risco diretos no resultado final.</p>

        <p><strong>Formula:</strong> Índice de Risco (%) = [(Pontos de Sódio + Pontos de Gordura + Pontos de Açúcar) x 1,5] + 15</p>

        <p><strong>Sendo:</strong></p>

        <li>Pontos de Sódio: (Quantidade de Sódio na embalagem / 2000) x 40.</li>

        <li>Pontos de Gordura Saturada: (Quantidade de Gordura na embalagem / 22) x 40. </li>

        <li>Pontos de Açúcar Adicionado: (Quantidade de Açúcar na embalagem / 50) x 20.</li>

    </div>
    """
    
    
    col_espaco_esq, col_caixa, col_espaco_dir = st.columns([1, 3, 1])
    with col_caixa:
        st.markdown(texto_admin.replace('\n', ''), unsafe_allow_html=True)
        
        if st.button(" ", key="btn_acessar_catalogo", type="primary", use_container_width=True):
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
        
        /* CSS da "Caixa" dos Botões Laterais Beges */
        button[kind="tertiary"], button[kind="tertiary"]:hover, button[kind="tertiary"]:active, button[kind="tertiary"]:focus {{
            background-color: #E2C792 !important;
            border-radius: 15px !important;
            border: 2px solid transparent !important;
            height: 115px !important; /* Altura ajustada para simetria */
            width: 100% !important;
            transition: transform 0.2s !important;
            margin-bottom: 20px !important;
            box-shadow: 0px 4px 6px rgba(0,0,0,0.15) !important;
        }}
        
        /* O SEGREDO: CSS mirando diretamente no TEXTO do botão para forçar o tamanho */
        button[kind="tertiary"] p {{
            font-family: 'Georgia', serif !important; 
            font-weight: bold !important;
            font-size: 26px !important; /* <-- AQUI VOCÊ CONTROLA O TAMANHO REAL DA LETRA */
            color: #21130d !important;
            margin: 0 !important;
            white-space: normal !important;
        }}
        
        button[kind="tertiary"]:hover {{
            transform: scale(1.03) !important;
            border: 2px solid #7B4E31 !important;
        }}
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

    # Textos do card central apra cada secao
    textos_sobre = {
        'missao': """
        <h2 style="text-align: center; border-bottom: 2px solid #E2C792; padding-bottom: 24px; margin-top: 0; font-family: 'Georgia', serif;">Nossa Missão</h2>
        <p style="font-size: 18px;">Desenvolver as tarefas e o projeto final de equipe de forma estruturada, aplicando conhecimentos analíticos e técnicos, destacando-se pela organização e praticidade na resolução de problemas, para atender às exigências da professora e gerar aprendizado prático de IADM.</p>
        """,
        
        'visao': """
        <h2 style="text-align: center; border-bottom: 2px solid #E2C792; padding-bottom: 24px; margin-top: 0; font-family: 'Georgia', serif;">Nossa Visão</h2>
        <p style="font-size: 18px;">Ser reconhecida pelo corpo docente e pelos pares como uma equipe de excelência técnica e gestão eficiente, alcançando a nota máxima no Projeto Final e gerando um portfólio prático até o fim do semestre.</p>
        """,
        
        'valores': """
        <h2 style="text-align: center; border-bottom: 2px solid #E2C792; padding-bottom: 24px; margin-top: 0; font-family: 'Georgia', serif;">Nossos Valores</h2>
        <ul style="font-size: 18px; line-height: 1.8;">
            <li><strong>Pragmatismo:</strong> Foco na resolução de problemas e trabalho de qualidade.</li>
            <li><strong>Comprometimento com prazos:</strong> Respeito com os marcos do projeto.</li>
            <li><strong>Comunicação direta e transparente:</strong> Feedbacks técnicos, baseados em dados e fatos.</li>
            <li><strong>Qualidade técnica:</strong> Decisões baseadas em praticidade e fundamentos teóricos.</li>
        </ul>
        """,
        
        'grupo': f"""
        <h2 style="text-align: center; border-bottom: 2px solid #E2C792; padding-bottom: 10px; margin-top: 0; font-family: 'Georgia', serif;">O Grupo</h2>
        <div style="text-align: center; margin-bottom: 15px;">
            <img src="{foto_equipe_b64}" style="max-height: 160px; border-radius: 10px;">
        </div>
        <p style="font-size: 18px;"> Nosso grupo nasceu com o intuito de conscientizar a população sobre os problemas modernos da industrialização alimentícia. O grupo é composto de apenas 4 alunos de Introducao a Administração, e usamos o que aprendemos em aula para criar todo o projeto “Fake Wonka” com esse intuito. O grupo apesar de pequeno é bastante diverso , criativo, organizado e aplicado.</p>
        <p> O grupo então é composto por: </p>
        <li> Danielle Cristine Tavera </li>
        <li> Misael Gomes Da Silva </li>
        <li> Ronald Rodrigues Barbosa </li>
        <li> Washington Marinho dos Santos </li>
        """,
        
        'professora': """
        <h2 style="text-align: center; border-bottom: 2px solid #E2C792; padding-bottom: 10px; margin-top: 0; font-family: 'Georgia', serif;">A Professora</h2>
        <p style="font-size: 18px;">Agradecemos a nossa professora pelos ensinamentos admistrativos que usamos para fazer esse projeto fluir, além de abrir nossos olhos para a realidade da administração do dia a dia e como funciona as organizacões.</p> 
        <p>Um agradecimento especial a monitoria que sempre se mostrou disposta a ajudar e tirar nossas dúvidas durante o curso.</p>
        """,

        'materia': """
        <h2 style="text-align: center; border-bottom: 2px solid #E2C792; padding-bottom: 10px; margin-top: 0; font-family: 'Georgia', serif;">A Matéria</h2>
        <p style="font-size: 18px;">A disciplina de Introdução à Administração estabelece o arcabouço teórico-conceitual necessário para a gestão de organizações, abordando a administração como um processo sistêmico composto pelas funções de planejamento, organização, direção e controle. O estudo fundamenta-se na evolução do pensamento administrativo, analisando como as organizações transitaram de estruturas rígidas para modelos ágeis e adaptáveis.</p>
        <p style="font-size: 18px;">Nos ajudou a consolidar nossa compreensão dos pilares organizacionais, e o desenvolvimento do nosso projeto de site permitiu elevar essa análise a um novo patamar, aprimorando nossa visão crítica sobre as dinâmicas complexas do mercado industrial e administrativo.</p>
        """
    }

    col_vazia_esq, col_esq, col_meio, col_dir, col_vazia_dir = st.columns([0.5, 1.2, 2.2, 1.2, 0.5])
    
    with col_esq:
        if st.button("Missão", type="tertiary", use_container_width=True):
            st.session_state['aba_sobre'] = 'missao'
            st.rerun()
            
        if st.button("Visão", type="tertiary", use_container_width=True):
            st.session_state['aba_sobre'] = 'visao'
            st.rerun()

        if st.button("Valores", type="tertiary", use_container_width=True):
            st.session_state['aba_sobre'] = 'valores'
            st.rerun()

    with col_meio:
        texto_selecionado = textos_sobre[st.session_state['aba_sobre']]
        
        # Card central com as informacoes do cards laterais
        html_caixa = f"""
        <div style="background-color: #7B4E31; border-radius: 15px; padding: 40px; color: white; height: 416px; overflow-y: auto; box-shadow: inset 0 0 15px rgba(0,0,0,0.3); font-family: Arial, sans-serif; line-height: 1.6;">
            {texto_selecionado}
        </div>
        """
        st.markdown(textwrap.dedent(html_caixa), unsafe_allow_html=True)

    with col_dir:
        if st.button("O Grupo", type="tertiary", use_container_width=True):
            st.session_state['aba_sobre'] = 'grupo'
            st.rerun()
            
        if st.button("A Professora", type="tertiary", use_container_width=True):
            st.session_state['aba_sobre'] = 'professora'
            st.rerun()

        if st.button("A Matéria", type="tertiary", use_container_width=True):
            st.session_state['aba_sobre'] = 'materia'
            st.rerun()


# ==========================================
# TELA 3: CATÁLOGO E PESQUISA
# ==========================================
elif st.session_state['pagina_atual'] == 'catalogo':
    
    st.markdown(f"""
    <style>
        /* O Botão do Topo (Voltar) */
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
        
        /* O Novo Botão de Ver Produto (Retangular e Blindado) */
        button[kind="primary"], button[kind="primary"]:hover, button[kind="primary"]:active, button[kind="primary"]:focus, button[kind="primary"]:disabled {{ 
            background-color: transparent !important;
            background-image: url('{botao_ver_produto_b64}') !important;
            background-size: contain !important;
            background-repeat: no-repeat !important;
            background-position: center !important;
            border: none !important; box-shadow: none !important; 
            height: 50px !important; 
            width: 100% !important; 
            color: transparent !important; transition: transform 0.2s !important; opacity: 1 !important; outline: none !important; 
            display: block !important; margin: 0 auto !important;
        }}
        button[kind="primary"] * {{ display: none !important; color: transparent !important; background: transparent !important; }}
        button[kind="primary"]::before, button[kind="primary"]::after {{ display: none !important; background: transparent !important; }}
        button[kind="primary"]:hover {{ transform: scale(1.02) !important; }}
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
    
    # Barra de pesquisa 
    col_pesq_esq, col_busca, col_pesq_dir = st.columns([1, 2.5, 1])
    with col_busca:
        busca = st.text_input("Buscar", placeholder="Pesquise aqui...", label_visibility="collapsed")
    
    st.write("\n" * 2)

    resultados = dados_alimentos[dados_alimentos["Alimento"].str.contains(busca, case=False, na=False)] if busca else dados_alimentos

    if not resultados.empty:
        for index, row in resultados.iterrows():
            foto_produto_b64 = carregar_imagem_base64(str(row['Caminho_Imagem']))
            
            # Espaçamento para alinhar o catalogo
            col_vazia_esq, col_img, col_info, col_vazia_dir = st.columns([1, 1, 2.5, 1])
            
            with col_img:
                st.markdown(f"""
                <div style="background-color: #E2C792; border-radius: 15px; width: 160px; height: 160px; display: flex; align-items: center; justify-content: center; padding: 10px; margin: 0 auto;">
                    <img src="{foto_produto_b64}" style="max-height: 140px; max-width: 100%; border-radius: 10px; object-fit: contain;">
                </div>
                """, unsafe_allow_html=True)
                
            with col_info:
                st.markdown(f"""
                <div style="background-color: #7B4E31; border-radius: 15px; padding: 15px 20px; color: white; min-height: 95px; height: auto; margin-bottom: 15px; display: flex; flex-direction: column; justify-content: center;">
                    <h4 style="margin: 0; color: #E2C792;">{row['Alimento']}</h4>
                    <p style="margin: 5px 0 0 0; font-size: 14px; line-height: 1.4;">{row['Descricao']}</p>
                </div>
                """, unsafe_allow_html=True)
                
                if st.button(" ", key=f"btn_{index}", type="primary", use_container_width=True):
                    st.session_state['alimento_selecionado'] = row
                    st.session_state['pagina_atual'] = 'descricao'
                    st.rerun()
            
            # linha divisoria
            st.markdown("<hr style='margin: 20px auto; width: 70%; border-color: #7B4E31; opacity: 0.25;'>", unsafe_allow_html=True)
            
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

    pct_risco = float(alimento.get('Nivel_Risco_Pct', 0))
    if pct_risco <= 1 and pct_risco > 0: 
        pct_risco = pct_risco * 100
    
    foto_produto_b64 = carregar_imagem_base64(str(alimento['Caminho_Imagem']))
        
    fig = go.Figure(go.Pie(
        values=[pct_risco, 100 - pct_risco],
        labels=["Índice de Risco", "Segurança"],
        hole=0.75, 
        marker_colors=["#8b0232", "#ae5a66"], 
        textinfo='none', 
        hoverinfo='label+percent'
    ))
    
    fig.update_layout(
        showlegend=False, paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)',
        margin=dict(t=10, b=10, l=10, r=10), height=300
    )
    
    fig.add_layout_image(
        dict(
            source=foto_produto_b64,
            xref="paper", yref="paper",
            x=0.5, y=0.5,
            sizex=0.6, sizey=0.6, 
            xanchor="center", yanchor="middle"
        )
    )
    
    st.plotly_chart(fig, use_container_width=True)

    st.markdown(f"""
        <div style='text-align: center; margin-top: -30px; margin-bottom: 30px;'>
            <span style='color: white; font-size: 20px; font-weight: bold;'>Índice de Risco: </span>
            <span style='color: #E2C792; font-size: 30px; font-weight: bold;'>{int(pct_risco)}%</span>
        </div>
    """, unsafe_allow_html=True)

    st.write("\n")
    col_info, col_nutri = st.columns([1, 1])

    def valor_nutri(coluna):
        val = alimento.get(coluna)
        return val if pd.notna(val) else "Informação não disponível"

    with col_info:
        zona_risco = valor_nutri('Zona_de_Risco')
        justificativa = valor_nutri('Justificativa_Risco')
        
        html_info = f"""<div style="background-color: #7B4E31; border-radius: 15px; padding: 30px; height: 100%; min-height: 380px; color: white;">
<h4 style="color: #E2C792; margin-top: 0;">Informações do Produto</h4>
<p style="font-size: 16px;">{valor_nutri('Descricao')}</p>
<br>
<h4 style="color: #C00000; margin-top: 0;">⚠️ Laudo de Alerta Industrial</h4>
<p style="font-size: 15px; line-height: 1.4;">{valor_nutri('Alerta_Riscos')}</p>
<br>
<h4 style="color: #E2C792; margin-top: 0;">🧮 Cálculo do Índice</h4>
<p style="font-size: 15px; line-height: 1.4;"><strong>{zona_risco}</strong><br>{justificativa}</p>
</div>"""
        st.markdown(textwrap.dedent(html_info), unsafe_allow_html=True)

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
                
                linhas_html += f'<tr style="border-bottom: 1px solid #7B4E31;"><td style="padding: 4px 0 4px {recuo}px; font-weight: {peso_fonte}; color: {cor_fonte};">{nome_exibicao}</td><td style="text-align: right;">{valor}</td></tr>'

        porcao_texto = alimento.get('Porcao') if pd.notna(alimento.get('Porcao')) else "Porção não informada"

        html_tabela = f'<div style="background-color: #E2C792; border-radius: 15px; padding: 25px; color: black; font-family: Arial, sans-serif; height: 100%; min-height: 380px; box-shadow: inset 0 0 10px rgba(0,0,0,0.1);"><h4 style="margin: 0; text-align: center; border-bottom: 2px solid black; padding-bottom: 5px;">INFORMAÇÃO NUTRICIONAL</h4><p style="margin: 5px 0; font-size: 14px; text-align: center; font-weight: bold;">{porcao_texto}</p><table style="width: 100%; border-collapse: collapse; font-size: 13px; margin-top: 10px;">{linhas_html}</table></div>'
        
        st.markdown(textwrap.dedent(html_tabela), unsafe_allow_html=True)
