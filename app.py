import streamlit as st
from usuario import cadastrar_usuario, autenticar_usuario, atualizar_perfil, obter_perfil
from database import criar_tabelas
from treino import gerar_treino
from dieta import gerar_dieta
from progresso import registrar_progresso, exibir_progresso

# Inicializa banco
criar_tabelas()

# Tema escuro com CSS customizado
st.markdown("""
    <style>
        body {
            background-color: #000000;
            color: #FFFFFF;
        }
        .css-1v0mbdj.edgvbvh3 {
            background-color: #111111;
        }
        .stTextInput > div > div > input, .stNumberInput input, .stSelectbox div div {
            background-color: #222;
            color: white;
        }
        .stButton>button {
            background-color: #444;
            color: white;
            border: 1px solid white;
        }
        .stButton>button:hover {
            background-color: #666;
        }
        .stRadio > div {
            background-color: #111;
            color: white;
        }
        .stSelectbox div {
            color: white;
        }
    </style>
""", unsafe_allow_html=True)

# Sessão de autenticação
if 'usuario' not in st.session_state:
    st.session_state.usuario = None

# TÍTULO CENTRALIZADO
st.markdown(
    "<h1 style='text-align: center; color: white;'>Muscle Natural App</h1>",
    unsafe_allow_html=True
)

# Menu lateral
menu = ["Login", "Cadastro"] if not st.session_state.usuario else ["Perfil", "Treino", "Dieta", "Progresso", "Sair"]
escolha = st.sidebar.selectbox("Menu", menu)

# LOGIN e CADASTRO juntos para o layout do botão lado a lado
if escolha == "Login" and not st.session_state.usuario:
    st.subheader("Login e Cadastro")

    col1, col2 = st.columns([1, 1])

    with col1:
        st.markdown("### Login")
        email_login = st.text_input("Email (login)", key="email_login")
        senha_login = st.text_input("Senha (login)", type="password", key="senha_login")
        if st.button("Entrar"):
            usuario = autenticar_usuario(email_login, senha_login)
            if usuario:
                st.session_state.usuario = usuario
                st.success("Login realizado com sucesso!")
                st.experimental_rerun()
            else:
                st.error("Credenciais inválidas.")

    with col2:
        st.markdown("### Cadastro")
        nome_cad = st.text_input("Nome (cadastro)", key="nome_cad")
        email_cad = st.text_input("Email (cadastro)", key="email_cad")
        senha_cad = st.text_input("Senha (cadastro)", type="password", key="senha_cad")
        if st.button("Cadastrar"):
            if cadastrar_usuario(nome_cad, email_cad, senha_cad):
                st.success("Cadastro realizado. Faça login.")
                # Opcional: limpar os campos após cadastro
                st.experimental_rerun()
            else:
                st.error("Email já cadastrado.")

# CADASTRO separado — opcional, você pode remover essa aba se usar o formulário acima
elif escolha == "Cadastro" and not st.session_state.usuario:
    st.subheader("Cadastro")
    nome = st.text_input("Nome")
    email = st.text_input("Email")
    senha = st.text_input("Senha", type="password")
    if st.button("Cadastrar"):
        if cadastrar_usuario(nome, email, senha):
            st.success("Cadastro realizado. Faça login.")
        else:
            st.error("Email já cadastrado.")

# PERFIL
elif escolha == "Perfil" and st.session_state.usuario:
    st.subheader("Seu Perfil")
    usuario_id = st.session_state.usuario[0]
    perfil = obter_perfil(usuario_id)

    nome, email, idade, sexo, peso, altura, objetivo, freq = perfil
    st.text(f"Nome: {nome} | Email: {email}")

    idade = st.number_input("Idade", value=idade or 0)
    sexo = st.selectbox("Sexo", ["Masculino", "Feminino"], index=0 if sexo == "Masculino" else 1)
    peso = st.number_input("Peso (kg)", value=peso or 0.0)
    altura = st.number_input("Altura (cm)", value=altura or 0.0)
    objetivo = st.selectbox("Objetivo", ["Hipertrofia", "Emagrecimento", "Resistência"], index=["Hipertrofia", "Emagrecimento", "Resistência"].index(objetivo or "Hipertrofia"))
    freq = st.selectbox("Frequência de treino", ["1-2x", "3-4x", "5-6x"], index=["1-2x", "3-4x", "5-6x"].index(freq or "3-4x"))

    if st.button("Atualizar Perfil"):
        atualizar_perfil(usuario_id, idade, sexo, peso, altura, objetivo, freq)
        st.success("Perfil atualizado com sucesso!")

# SAIR
elif escolha == "Sair":
    st.session_state.usuario = None
    st.success("Você saiu da sua conta.")
    st.experimental_rerun()

# TREINO
elif escolha == "Treino" and st.session_state.usuario:
    usuario_id = st.session_state.usuario[0]
    perfil = obter_perfil(usuario_id)
    objetivo, frequencia = perfil[6], perfil[7]
    gerar_treino(objetivo, frequencia)

# DIETA
elif escolha == "Dieta" and st.session_state.usuario:
    usuario_id = st.session_state.usuario[0]
    perfil = obter_perfil(usuario_id)
    objetivo = perfil[6]
    gerar_dieta(objetivo)

# PROGRESSO
elif escolha == "Progresso" and st.session_state.usuario:
    registrar_progresso()
    exibir_progresso()

# LEMBRETE SE NÃO ESTIVER LOGADO
elif escolha in ["Treino", "Dieta", "Progresso"] and not st.session_state.usuario:
    st.warning("Faça login para acessar essa aba.")

# RODAPÉ CENTRALIZADO
st.markdown(
    """
    <hr style="margin-top: 50px; border: 1px solid #555;">
    <div style='text-align: center; font-size: 14px; color: white;'>
        <strong>SAMUCJ TECHNOLOGY</strong>
    </div>
    """,
    unsafe_allow_html=True
)
