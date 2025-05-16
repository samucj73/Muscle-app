import streamlit as st
from usuario import cadastrar_usuario, autenticar_usuario, atualizar_perfil, obter_perfil
from database import criar_tabelas
from treino import gerar_treino
from dieta import gerar_dieta
from progresso import registrar_progresso, exibir_progresso

# Inicializa banco
criar_tabelas()

st.set_page_config(page_title="Muscle Natural App", layout="wide")

# CSS personalizado para modo escuro e centralização
st.markdown("""
    <style>
        body {
            background-color: #121212;
            color: white;
        }
        h1 {
            text-align: center;
            color: white;
        }
    </style>
""", unsafe_allow_html=True)

# Estado de sessão
if 'usuario' not in st.session_state:
    st.session_state.usuario = None

# Título principal
st.markdown("<h1>Muscle Natural App</h1>", unsafe_allow_html=True)

# Abas do menu
abas = st.tabs(["Login/Cadastro", "Perfil", "Treino", "Dieta", "Progresso"])

# --- Aba 0: Login/Cadastro ---
with abas[0]:
    st.subheader("Acesse sua conta")

    if st.session_state.usuario:
        st.success("Você está logado!")
        if st.button("Sair"):
            st.session_state.usuario = None
            st.success("Logout realizado com sucesso.")
            st.experimental_rerun()
    else:
        escolha = st.radio("Selecione:", ["Login", "Cadastro"], horizontal=True)

        if escolha == "Login":
            email = st.text_input("Email", key="email_login")
            senha = st.text_input("Senha", type="password", key="senha_login")
            if st.button("Entrar"):
                usuario = autenticar_usuario(email, senha)
                if usuario:
                    st.session_state.usuario = usuario
                    st.success("Login realizado com sucesso!")
                    st.experimental_rerun()
                else:
                    st.error("Credenciais inválidas.")
        else:
            nome = st.text_input("Nome", key="nome_cad")
            email = st.text_input("Email", key="email_cad")
            senha = st.text_input("Senha", type="password", key="senha_cad")
            if st.button("Cadastrar"):
                if cadastrar_usuario(nome, email, senha):
                    st.success("Cadastro realizado com sucesso! Faça login.")
                else:
                    st.error("Email já cadastrado.")

# --- Aba 1: Perfil ---
with abas[1]:
    if st.session_state.usuario:
        st.subheader("Seu Perfil")
        usuario_id = st.session_state.usuario[0]
        perfil = obter_profil(usuario_id)
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
    else:
        st.warning("Você precisa estar logado para acessar o perfil.")

# --- Aba 2: Treino ---
with abas[2]:
    if st.session_state.usuario:
        st.subheader("Seu Plano de Treino")
        usuario_id = st.session_state.usuario[0]
        perfil = obter_profil(usuario_id)
        objetivo, frequencia = perfil[6], perfil[7]
        gerar_treino(objetivo, frequencia)
    else:
        st.warning("Você precisa estar logado para acessar o treino.")

# --- Aba 3: Dieta ---
with abas[3]:
    if st.session_state.usuario:
        st.subheader("Plano Alimentar")
        usuario_id = st.session_state.usuario[0]
        perfil = obter_profil(usuario_id)
        objetivo = perfil[6]
        gerar_dieta(objetivo)
    else:
        st.warning("Você precisa estar logado para acessar a dieta.")

# --- Aba 4: Progresso ---
with abas[4]:
    if st.session_state.usuario:
        st.subheader("Acompanhamento de Progresso")
        registrar_progresso()
        exibir_progresso()
    else:
        st.warning("Você precisa estar logado para acessar o progresso.")

# Rodapé
st.markdown("""
    <hr>
    <div style='text-align: center; font-size: 14px; color: white;'>
        <strong>SAMUCJ TECHNOLOGY</strong>
    </div>
""", unsafe_allow_html=True)
