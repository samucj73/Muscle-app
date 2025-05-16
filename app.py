import streamlit as st
from usuario import cadastrar_usuario, autenticar_usuario, atualizar_perfil, obter_perfil
from database import criar_tabelas
from treino import gerar_treino
from dieta import gerar_dieta
from progresso import registrar_progresso, exibir_progresso

# Inicializa banco
criar_tabelas()

# Configurações visuais e CSS
st.set_page_config(page_title="Muscle Natural App", layout="wide")

# Tema escuro customizado (se quiser, mantém seu CSS aqui)
st.markdown(
    """
    <style>
    /* Corpo com fundo escuro */
    body, .css-18e3th9 {
        background-color: #121212;
        color: white;
    }
    /* Centraliza o título */
    h1 {
        text-align: center;
        color: white;
    }
    /* Outros ajustes visuais */
    </style>
    """,
    unsafe_allow_html=True
)

if 'usuario' not in st.session_state:
    st.session_state.usuario = None

if 'modo_login' not in st.session_state:
    st.session_state.modo_login = True

# Título principal
st.markdown(
    "<h1>Muscle Natural App</h1>",
    unsafe_allow_html=True
)

# Menu horizontal fixo abaixo do título
if st.session_state.usuario:
    menu_opcoes = ["Perfil", "Treino", "Dieta", "Progresso", "Sair"]
else:
    menu_opcoes = ["Login", "Cadastro"]

menu_escolha = st.radio(
    "Navegação",
    menu_opcoes,
    index=0,
    horizontal=True,
    label_visibility="visible"
)

# --- Página Login / Cadastro ---
if menu_escolha == "Login" and not st.session_state.usuario:
    if st.session_state.modo_login:
        st.subheader("Login")
        email = st.text_input("Email", key="email_login")
        senha = st.text_input("Senha", type="password", key="senha_login")
        col1, col2 = st.columns(2)
        with col1:
            if st.button("Entrar"):
                usuario = autenticar_usuario(email, senha)
                if usuario:
                    st.session_state.usuario = usuario
                    st.success("Login realizado com sucesso!")
                    st.experimental_rerun()
                else:
                    st.error("Credenciais inválidas.")
        with col2:
            if st.button("Cadastrar"):
                st.session_state.modo_login = False
                st.experimental_rerun()
    else:
        st.subheader("Cadastro")
        nome = st.text_input("Nome", key="nome_cad")
        email = st.text_input("Email", key="email_cad")
        senha = st.text_input("Senha", type="password", key="senha_cad")
        col1, col2 = st.columns(2)
        with col1:
            if st.button("Cadastrar"):
                if cadastrar_usuario(nome, email, senha):
                    st.success("Cadastro realizado. Faça login.")
                    st.session_state.modo_login = True
                    st.experimental_rerun()
                else:
                    st.error("Email já cadastrado.")
        with col2:
            if st.button("Voltar para Login"):
                st.session_state.modo_login = True
                st.experimental_rerun()

elif menu_escolha == "Cadastro" and not st.session_state.usuario:
    st.subheader("Cadastro")
    nome = st.text_input("Nome")
    email = st.text_input("Email")
    senha = st.text_input("Senha", type="password")
    if st.button("Cadastrar"):
        if cadastrar_usuario(nome, email, senha):
            st.success("Cadastro realizado. Faça login.")
        else:
            st.error("Email já cadastrado.")

# --- Página Perfil ---
elif menu_escolha == "Perfil" and st.session_state.usuario:
    usuario_id = st.session_state.usuario[0]
    perfil = obter_perfil(usuario_id)
    nome, email, idade, sexo, peso, altura, objetivo, freq = perfil
    st.subheader("Seu Perfil")
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

# --- Página Sair ---
elif menu_escolha == "Sair":
    st.session_state.usuario = None
    st.success("Você saiu da sua conta.")
    st.experimental_rerun()

# --- Página Treino ---
elif menu_escolha == "Treino" and st.session_state.usuario:
    usuario_id = st.session_state.usuario[0]
    perfil = obter_perfil(usuario_id)
    objetivo, frequencia = perfil[6], perfil[7]
    gerar_treino(objetivo, frequencia)

# --- Página Dieta ---
elif menu_escolha == "Dieta" and st.session_state.usuario:
    usuario_id = st.session_state.usuario[0]
    perfil = obter_perfil(usuario_id)
    objetivo = perfil[6]
    gerar_dieta(objetivo)

# --- Página Progresso ---
elif menu_escolha == "Progresso" and st.session_state.usuario:
    registrar_progresso()
    exibir_progresso()

# --- Caso tente acessar página sem login ---
elif menu_escolha in ["Treino", "Dieta", "Progresso", "Perfil", "Sair"] and not st.session_state.usuario:
    st.warning("Faça login para acessar essa aba.")

# Rodapé
st.markdown(
    """
    <hr style="margin-top: 50px; border: 1px solid #555;">
    <div style='text-align: center; font-size: 14px; color: white;'>
        <strong>SAMUCJ TECHNOLOGY</strong>
    </div>
    """,
    unsafe_allow_html=True
)
