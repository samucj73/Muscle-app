from datetime import date
from database import conectar
import streamlit as st
import pandas as pd

# Função de backend para salvar progresso
def salvar_progresso(usuario_id, peso, cintura, quadril, peito):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO progresso (usuario_id, data, peso, cintura, quadril, peito)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (usuario_id, str(date.today()), peso, cintura, quadril, peito))
    conn.commit()
    conn.close()

# Função de backend para obter progresso
def obter_progresso(usuario_id):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT data, peso, cintura, quadril, peito
        FROM progresso
        WHERE usuario_id = ?
        ORDER BY data DESC
    """, (usuario_id,))
    dados = cursor.fetchall()
    conn.close()
    return dados

# ✅ Interface para registrar progresso (usada no app.py)
def registrar_progresso():
    st.subheader("Registrar Progresso Corporal")

    usuario_id = st.session_state.usuario[0]
    peso = st.number_input("Peso (kg)", min_value=0.0, format="%.2f")
    cintura = st.number_input("Cintura (cm)", min_value=0.0, format="%.2f")
    quadril = st.number_input("Quadril (cm)", min_value=0.0, format="%.2f")
    peito = st.number_input("Peitoral (cm)", min_value=0.0, format="%.2f")

    if st.button("Salvar Progresso"):
        salvar_progresso(usuario_id, peso, cintura, quadril, peito)
        st.success("Progresso registrado com sucesso!")

# ✅ Interface para exibir progresso
def exibir_progresso():
    st.subheader("Histórico de Progresso Corporal")
    usuario_id = st.session_state.usuario[0]
    dados = obter_progresso(usuario_id)

    if dados:
        df = pd.DataFrame(dados, columns=["Data", "Peso", "Cintura", "Quadril", "Peito"])
        st.dataframe(df)
    else:
        st.info("Nenhum progresso registrado ainda.")
