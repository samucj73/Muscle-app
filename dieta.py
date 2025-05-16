import streamlit as st
from usuario import obter_perfil

def gerar_dieta():
    st.markdown(
        "<h2 style='text-align: center; color: white;'>Plano Alimentar Personalizado</h2><hr>",
        unsafe_allow_html=True
    )

    if not st.session_state.usuario:
        st.warning("Faça login para acessar o plano alimentar.")
        return

    usuario_id = st.session_state.usuario[0]
    perfil = obter_perfil(usuario_id)
    objetivo = perfil[6] if perfil else None

    if not objetivo:
        st.warning("Objetivo não definido. Atualize seu perfil.")
        return

    objetivo = objetivo.capitalize()

    plano_alimentar = {
        "Hipertrofia": {
            "Café da manhã": [("Ovos mexidos", "3 unidades"), ("Aveia com banana", "1 porção"), ("Leite integral", "1 copo")],
            "Almoço": [("Arroz integral", "3 colheres de sopa"), ("Feijão", "1 concha"), ("Frango grelhado", "150g"), ("Salada de folhas", "à vontade")],
            "Lanche da tarde": [("Iogurte natural", "1 pote"), ("Granola", "2 colheres de sopa")],
            "Jantar": [("Batata doce", "2 unidades médias"), ("Ovos cozidos", "3 unidades"), ("Brócolis cozido", "à vontade")],
        },
        "Emagrecimento": {
            "Café da manhã": [("Claras de ovo", "4 unidades"), ("Mamão", "1 fatia"), ("Chá verde", "1 xícara")],
            "Almoço": [("Arroz integral", "2 colheres"), ("Frango grelhado", "100g"), ("Salada crua", "à vontade")],
            "Lanche da tarde": [("Maçã", "1 unidade"), ("Castanhas", "5 unidades")],
            "Jantar": [("Sopa de legumes", "1 prato fundo"), ("Peito de frango desfiado", "50g")],
        },
        "Resistência": {
            "Café da manhã": [("Pão integral", "2 fatias"), ("Ovos mexidos", "2 unidades"), ("Suco de laranja", "1 copo")],
            "Almoço": [("Macarrão integral", "1 prato médio"), ("Carne moída", "100g"), ("Cenoura ralada", "à vontade")],
            "Lanche da tarde": [("Vitamina de frutas com leite", "1 copo"), ("Amendoim", "1 colher de sopa")],
            "Jantar": [("Quinoa", "2 colheres de sopa"), ("Filé de peixe", "100g"), ("Salada de legumes", "à vontade")],
        }
    }

    if objetivo not in plano_alimentar:
        st.error("Plano alimentar não disponível para o objetivo selecionado.")
        return

    for nome_refeicao, itens in plano_alimentar[objetivo].items():
        st.markdown(f"<h4 style='color:#00ffcc;'>{nome_refeicao}</h4>", unsafe_allow_html=True)
        for alimento, quantidade in itens:
            st.markdown(f"- **{alimento}**: {quantidade}")
        st.markdown("---")
