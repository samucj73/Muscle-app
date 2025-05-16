import streamlit as st

def gerar_dieta():
    st.markdown("<h2 style='text-align: center; color: white;'>🍽️ Plano Alimentar Personalizado</h2>", unsafe_allow_html=True)

    usuario = st.session_state.usuario
    if not usuario:
        st.warning("⚠️ Faça login para acessar a dieta.")
        return

    objetivo = usuario[7]  # índice do campo objetivo na tupla do banco
    st.markdown(f"<h4 style='text-align: center; color: gray;'>Objetivo: {objetivo}</h4>", unsafe_allow_html=True)
    st.markdown("<hr>", unsafe_allow_html=True)

    plano_alimentar = {
        "Hipertrofia": {
            "Café da manhã": [
                ("🍳 Ovos mexidos", "3 unidades"),
                ("🍞 Pão integral", "2 fatias"),
                ("🥛 Leite com aveia", "1 copo")
            ],
            "Almoço": [
                ("🍗 Frango grelhado", "150g"),
                ("🍚 Arroz integral", "1 xícara"),
                ("🥗 Salada verde", "à vontade"),
                ("🥔 Batata-doce", "1 unidade média")
            ],
            "Jantar": [
                ("🐟 Peixe assado", "150g"),
                ("🍝 Macarrão integral", "1 prato"),
                ("🥬 Brócolis cozido", "1 porção")
            ],
            "Lanches": [
                ("🍌 Banana com pasta de amendoim", "1 unidade"),
                ("🥜 Mix de castanhas", "30g")
            ]
        },

        "Emagrecimento": {
            "Café da manhã": [
                ("🍎 Maçã", "1 unidade"),
                ("🍳 Omelete de claras", "3 claras"),
                ("☕ Café preto sem açúcar", "1 xícara")
            ],
            "Almoço": [
                ("🥩 Carne magra grelhada", "100g"),
                ("🥦 Legumes no vapor", "1 porção"),
                ("🥗 Salada verde", "à vontade")
            ],
            "Jantar": [
                ("🍲 Sopa de legumes", "1 prato"),
                ("🍳 Omelete com vegetais", "1 porção")
            ],
            "Lanches": [
                ("🥜 Castanhas", "10 unidades"),
                ("🥛 Iogurte desnatado", "1 copo")
            ]
        },

        "Resistência": {
            "Café da manhã": [
                ("🍞 Torradas integrais", "2 unidades"),
                ("🍯 Mel", "1 colher"),
                ("🍌 Banana", "1 unidade"),
                ("🥛 Leite desnatado", "1 copo")
            ],
            "Almoço": [
                ("🥩 Bife grelhado", "120g"),
                ("🍚 Arroz branco", "1 xícara"),
                ("🥗 Salada com azeite", "à vontade")
            ],
            "Jantar": [
                ("🍝 Macarrão com frango desfiado", "1 prato"),
                ("🥬 Espinafre refogado", "1 porção")
            ],
            "Lanches": [
                ("🍪 Barra de proteína", "1 unidade"),
                ("🍓 Morangos", "1 xícara")
            ]
        }
    }

    refeicoes = st.tabs(["Café da manhã", "Almoço", "Jantar", "Lanches"])

    for i, nome_refeicao in enumerate(["Café da manhã", "Almoço", "Jantar", "Lanches"]):
        with refeicoes[i]:
            st.markdown(f"<h3 style='color: white;'>{nome_refeicao}</h3>", unsafe_allow_html=True)
            for alimento, quantidade in plano_alimentar[objetivo][nome_refeicao]:
                st.markdown(f"""
                <div style="background-color: #222; padding: 10px; border-radius: 8px; margin-bottom: 10px;">
                    <strong style="color: white;">{alimento}</strong><br>
                    <span style="color: gray;">Quantidade:</span> <span style="color: white;">{quantidade}</span>
                </div>
                """, unsafe_allow_html=True)
