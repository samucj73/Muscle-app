import streamlit as st

def gerar_treino(objetivo=None, frequencia=None):
    st.subheader("Plano de Treino Personalizado")

    if not objetivo or not frequencia:
        st.warning("Objetivo ou frequência não definidos.")
        return

    # Parâmetros por objetivo
    if objetivo == "Hipertrofia":
        series = "3-4 séries"
        reps = "8-12 repetições"
    elif objetivo == "Emagrecimento":
        series = "3-4 séries"
        reps = "15-20 repetições"
    elif objetivo == "Resistência":
        series = "2-3 séries"
        reps = "20+ repetições"
    else:
        st.warning("Objetivo não reconhecido.")
        return

    # Planos de treino por frequência
    if frequencia == "1-2x":
        st.markdown("**Treino Corpo Inteiro**")
        st.markdown(f"- Agachamento livre ({series} de {reps})")
        st.markdown(f"- Supino reto com barra ({series} de {reps})")
        st.markdown(f"- Remada curvada ({series} de {reps})")
        st.markdown(f"- Desenvolvimento militar ({series} de {reps})")
        st.markdown(f"- Elevação lateral ({series} de {reps})")
        st.markdown(f"- Prancha abdominal ({series} de 30-60 segundos)")

    elif frequencia == "3-4x":
        st.markdown("**Treino A - Peito e Tríceps**")
        st.markdown(f"- Supino reto com barra ({series} de {reps})")
        st.markdown(f"- Supino inclinado com halteres ({series} de {reps})")
        st.markdown(f"- Crucifixo com halteres ({series} de {reps})")
        st.markdown(f"- Tríceps testa ({series} de {reps})")
        st.markdown(f"- Tríceps pulley ({series} de {reps})")

        st.markdown("**Treino B - Costas e Bíceps**")
        st.markdown(f"- Barra fixa ({series} de {reps})")
        st.markdown(f"- Remada curvada com barra ({series} de {reps})")
        st.markdown(f"- Pulldown frontal ({series} de {reps})")
        st.markdown(f"- Rosca direta com barra ({series} de {reps})")
        st.markdown(f"- Rosca alternada com halteres ({series} de {reps})")

        st.markdown("**Treino C - Pernas e Abdômen**")
        st.markdown(f"- Agachamento livre ({series} de {reps})")
        st.markdown(f"- Leg press ({series} de {reps})")
        st.markdown(f"- Cadeira extensora ({series} de {reps})")
        st.markdown(f"- Stiff com halteres ({series} de {reps})")
        st.markdown(f"- Elevação de pernas ({series} de {reps})")

    elif frequencia == "5-6x":
        st.markdown("**Segunda - Peito e Tríceps**")
        st.markdown(f"- Supino reto com barra ({series} de {reps})")
        st.markdown(f"- Supino inclinado com halteres ({series} de {reps})")
        st.markdown(f"- Crucifixo inclinado ({series} de {reps})")
        st.markdown(f"- Tríceps coice ({series} de {reps})")
        st.markdown(f"- Tríceps na corda ({series} de {reps})")

        st.markdown("**Terça - Costas e Bíceps**")
        st.markdown(f"- Puxada frontal ({series} de {reps})")
        st.markdown(f"- Remada curvada ({series} de {reps})")
        st.markdown(f"- Remada unilateral ({series} de {reps})")
        st.markdown(f"- Rosca direta ({series} de {reps})")
        st.markdown(f"- Rosca martelo ({series} de {reps})")

        st.markdown("**Quarta - Pernas**")
        st.markdown(f"- Agachamento livre ({series} de {reps})")
        st.markdown(f"- Leg press ({series} de {reps})")
        st.markdown(f"- Cadeira flexora ({series} de {reps})")
        st.markdown(f"- Stiff ({series} de {reps})")
        st.markdown(f"- Panturrilha no leg press ({series} de {reps})")

        st.markdown("**Quinta - Ombros e Abdômen**")
        st.markdown(f"- Desenvolvimento militar ({series} de {reps})")
        st.markdown(f"- Elevação lateral ({series} de {reps})")
        st.markdown(f"- Elevação frontal ({series} de {reps})")
        st.markdown(f"- Encolhimento para trapézio ({series} de {reps})")
        st.markdown(f"- Abdominal infra ({series} de {reps})")

        st.markdown("**Sexta - Corpo inteiro (leve)**")
        st.markdown(f"- Circuito leve com foco em resistência")
        st.markdown(f"- Exercícios compostos com pouco descanso")

    else:
        st.warning("Frequência de treino não reconhecida.")
