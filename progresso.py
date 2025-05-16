import streamlit as st
from datetime import date
from database import conectar

def registrar_progresso():
    st.markdown("<h2 style='text-align: center; color: white;'>📈 Registrar Progresso</h2>", unsafe_allow_html=True)

    usuario_id = st.session_state.usuario[0]

    with st.form("form_progresso"):
        col1, col2 = st.columns(2)
        with col1:
            peso = st.number_input("Peso (kg)", min_value=0.0, step=0.1)
            cintura = st.number_input("Cintura (cm)", min_value=0.0, step=0.1)
        with col2:
            quadril = st.number_input("Quadril (cm)", min_value=0.0, step=0.1)
            peito = st.number_input("Peitoral (cm)", min_value=0.0, step=0.1)

        submit = st.form_submit_button("Registrar")
        if submit:
            conn = conectar()
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO progresso (usuario_id, data, peso, cintura, quadril, peito)
                VALUES (?, ?, ?, ?, ?, ?)
            """, (usuario_id, str(date.today()), peso, cintura, quadril, peito))
            conn.commit()
            conn.close()
            st.success("✅ Progresso registrado com sucesso!")

def exibir_progresso():
    st.markdown("<h2 style='text-align: center; color: white;'>📊 Histórico de Progresso</h2>", unsafe_allow_html=True)

    usuario_id = st.session_state.usuario[0]
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

    if dados:
        for registro in dados:
            data, peso, cintura, quadril, peito = registro
            st.markdown(f"""
                <div style="background-color: #222; padding: 15px; border-radius: 10px; margin-bottom: 10px;">
                    <strong style="color: white;">📅 Data:</strong> <span style="color: gray;">{data}</span><br>
                    <strong style="color: white;">⚖️ Peso:</strong> {peso} kg<br>
                    <strong style="color: white;">📏 Cintura:</strong> {cintura} cm<br>
                    <strong style="color: white;">🍑 Quadril:</strong> {quadril} cm<br>
                    <strong style="color: white;">💪 Peitoral:</strong> {peito} cm
                </div>
            """, unsafe_allow_html=True)
    else:
        st.info("Nenhum progresso registrado ainda.")
