import streamlit as st
from usuario import obter_perfil

def calcular_tmb(peso, altura, idade, sexo):
    if sexo == "Masculino":
        return 10 * peso + 6.25 * altura - 5 * idade + 5
    else:
        return 10 * peso + 6.25 * altura - 5 * idade - 161

def calcular_get(tmb, freq):
    fator = {
        "1-2x": 1.375,
        "3-4x": 1.55,
        "5-6x": 1.725
    }
    return tmb * fator.get(freq, 1.55)

def gerar_dieta():
    st.subheader("Plano Alimentar Personalizado")

    usuario = st.session_state.usuario
    if not usuario:
        st.warning("Faça login para acessar a dieta.")
        return

    perfil = obter_perfil(usuario[0])
    nome, email, idade, sexo, peso, altura, objetivo, freq = perfil

    if not all([idade, sexo, peso, altura, objetivo, freq]):
        st.warning("Complete seu perfil na aba 'Perfil' para gerar a dieta.")
        return

    tmb = calcular_tmb(peso, altura, idade, sexo)
    get = calcular_get(tmb, freq)

    if objetivo == "Hipertrofia":
        calorias = get + 300
        proteinas = peso * 2.2
        carbs = peso * 4
        gorduras = peso * 1
    elif objetivo == "Emagrecimento":
        calorias = get - 400
        proteinas = peso * 2
        carbs = peso * 2.5
        gorduras = peso * 0.8
    else:  # Resistência
        calorias = get
        proteinas = peso * 1.6
        carbs = peso * 5
        gorduras = peso * 1

    st.success(f"Calorias diárias: {int(calorias)} kcal")
    st.info(f"Proteínas: {int(proteinas)}g | Carboidratos: {int(carbs)}g | Gorduras: {int(gorduras)}g")

    st.markdown("---")
    st.markdown("### Exemplo de Refeições:")

    st.markdown(f"""
    **Café da Manhã**: Ovos mexidos, pão integral, fruta, café preto  
    **Lanche da Manhã**: Iogurte + aveia + banana  
    **Almoço**: Arroz, feijão, frango grelhado, salada  
    **Lanche da Tarde**: Sanduíche natural ou shake de whey  
    **Jantar**: Omelete com legumes e batata doce  
    **Ceia**: Iogurte ou castanhas com proteína
    """)
