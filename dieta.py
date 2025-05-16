import streamlit as st

def gerar_dieta():
    st.subheader("Plano Alimentar Personalizado")

    objetivo = st.session_state.usuario[7] if st.session_state.usuario else None

    if not objetivo:
        st.warning("Objetivo não definido. Atualize seu perfil.")
        return

    plano_alimentar = {
        "Hipertrofia": {
            "Café da manhã": [("Ovos mexidos", "3 unidades"), ("Aveia", "40g"), ("Banana", "1 unidade")],
            "Almoço": [("Arroz integral", "100g"), ("Frango grelhado", "150g"), ("Brócolis cozido", "50g")],
            "Lanche da tarde": [("Iogurte natural", "1 copo"), ("Granola", "30g")],
            "Jantar": [("Batata doce", "100g"), ("Carne moída magra", "150g"), ("Salada verde", "à vontade")]
        },
        "Emagrecimento": {
            "Café da manhã": [("Ovo cozido", "2 unidades"), ("Mamão", "1 fatia"), ("Chá verde", "1 xícara")],
            "Almoço": [("Quinoa", "70g"), ("Peito de frango", "120g"), ("Abobrinha grelhada", "50g")],
            "Lanche da tarde": [("Maçã", "1 unidade"), ("Castanhas", "5 unidades")],
            "Jantar": [("Sopa de legumes", "1 prato"), ("Frango desfiado", "80g")]
        },
        "Resistência": {
            "Café da manhã": [("Pão integral", "2 fatias"), ("Queijo branco", "1 fatia"), ("Suco natural", "1 copo")],
            "Almoço": [("Macarrão integral", "80g"), ("Carne vermelha magra", "150g"), ("Salada mista", "à vontade")],
            "Lanche da tarde": [("Barra de cereal", "1 unidade"), ("Banana", "1 unidade")],
            "Jantar": [("Arroz", "100g"), ("Omelete", "2 ovos"), ("Legumes cozidos", "50g")]
        }
    }

    refeicoes = plano_alimentar.get(objetivo)

    if not refeicoes:
        st.warning("Plano alimentar não disponível para esse objetivo.")
        return

    for nome_refeicao, itens in refeicoes.items():
        with st.expander(f"🍽️ {nome_refeicao}"):
            for alimento, quantidade in itens:
                st.markdown(f"- **{alimento}** – {quantidade}")

    # Estilo customizado com fundo preto
    st.markdown(
        """
        <style>
        .stApp {
            background-color: #000000;
            color: #FFFFFF;
        }
        .st-expander > summary {
            background-color: #111111;
            color: white;
            font-weight: bold;
        }
        </style>
        """,
        unsafe_allow_html=True
    )
