import streamlit as st

def gerar_treino(objetivo=None, frequencia=None):
    st.markdown("<h2 style='text-align: center; color: white;'>🏋️ Plano de Treino Personalizado</h2>", unsafe_allow_html=True)

    if not objetivo or not frequencia:
        st.warning("⚠️ Objetivo ou frequência não definidos.")
        return

    st.markdown("<hr>", unsafe_allow_html=True)

    grupos_musculares = {
        "Peito": [
            ("🏋️ Supino reto com barra", "3-4 séries", "8-12 reps", "Banco, barra"),
            ("🏋️ Supino inclinado com halteres", "3 séries", "10-12 reps", "Banco inclinado, halteres"),
            ("🏋️ Crucifixo reto com halteres", "3 séries", "12-15 reps", "Banco, halteres"),
            ("🏋️ Crossover na polia", "3 séries", "12 reps", "Polia"),
            ("🏋️ Flexão de braço", "4 séries", "Máx reps", "Corpo livre")
        ],
        "Costas": [
            ("🏋️ Barra fixa", "4 séries", "Máx reps", "Barra fixa"),
            ("🏋️ Puxada frente na polia", "3 séries", "10 reps", "Polia alta"),
            ("🏋️ Remada curvada", "3 séries", "8-10 reps", "Barra ou halteres"),
            ("🏋️ Remada unilateral", "3 séries", "10 reps", "Halter"),
            ("🏋️ Pullover", "3 séries", "12 reps", "Halter ou máquina")
        ],
        "Pernas": [
            ("🏋️ Agachamento livre", "4 séries", "8-12 reps", "Barra"),
            ("🏋️ Leg press", "4 séries", "10-12 reps", "Máquina"),
            ("🏋️ Cadeira extensora", "3 séries", "12 reps", "Máquina"),
            ("🏋️ Flexora deitada", "3 séries", "12 reps", "Máquina"),
            ("🏋️ Panturrilha em pé", "4 séries", "15 reps", "Máquina ou peso livre")
        ],
        "Ombros": [
            ("🏋️ Desenvolvimento com halteres", "3 séries", "10 reps", "Halteres"),
            ("🏋️ Elevação lateral", "3 séries", "12 reps", "Halteres"),
            ("🏋️ Elevação frontal", "3 séries", "12 reps", "Halteres"),
            ("🏋️ Remada alta", "3 séries", "10-12 reps", "Barra"),
            ("🏋️ Encolhimento de ombros", "4 séries", "12 reps", "Halteres ou barra")
        ],
        "Braços": [
            ("🏋️ Rosca direta", "3 séries", "10 reps", "Barra"),
            ("🏋️ Rosca alternada", "3 séries", "12 reps", "Halteres"),
            ("🏋️ Tríceps testa", "3 séries", "10 reps", "Barra"),
            ("🏋️ Tríceps pulley", "3 séries", "12 reps", "Polia"),
            ("🏋️ Rosca martelo", "3 séries", "12 reps", "Halteres")
        ],
        "Abdômen": [
            ("🏋️ Abdominal infra", "4 séries", "15 reps", "Peso corporal"),
            ("🏋️ Abdominal supra", "4 séries", "20 reps", "Peso corporal"),
            ("🏋️ Prancha", "3 séries", "30-60s", "Corpo livre"),
            ("🏋️ Abdominal com polia", "3 séries", "15 reps", "Polia alta"),
            ("🏋️ Bicicleta no solo", "3 séries", "20 reps", "Peso corporal")
        ]
    }

    # Ajusta as repetições de acordo com o objetivo
    if objetivo == "Emagrecimento":
        ajuste_reps = lambda r: "15-20 reps"
    elif objetivo == "Resistência":
        ajuste_reps = lambda r: "18-25 reps"
    else:  # Hipertrofia padrão
        ajuste_reps = lambda r: r

    abas = st.tabs(list(grupos_musculares.keys()))

    for i, grupo in enumerate(grupos_musculares):
        with abas[i]:
            st.markdown(f"<h3 style='color: white;'>{grupo}</h3>", unsafe_allow_html=True)
            for nome, series, reps, equipamento in grupos_musculares[grupo]:
                st.markdown(f"""
                <div style="background-color: #222; padding: 10px; border-radius: 8px; margin-bottom: 10px;">
                    <strong style="color: white;">{nome}</strong><br>
                    <span style="color: gray;">Séries:</span> <span style="color: white;">{series}</span><br>
                    <span style="color: gray;">Repetições:</span> <span style="color: white;">{ajuste_reps(reps)}</span><br>
                    <span style="color: gray;">Equipamento:</span> <span style="color: white;">{equipamento}</span>
                </div>
                """, unsafe_allow_html=True)
