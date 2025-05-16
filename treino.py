gerar_treino_personalizado(objetivo, frequencia):
    st.subheader("Plano de Treino Personalizado")

    if objetivo == "Hipertrofia":
        if frequencia == "1-2x":
            st.write("Treino A: Corpo inteiro (Alta intensidade)")
            st.write("- Agachamento livre")
            st.write("- Supino reto com barra")
            st.write("- Remada curvada")
            st.write("- Desenvolvimento militar")
        elif frequencia == "3-4x":
            st.write("Treino A: Peito e Tríceps")
            st.write("- Supino reto com barra")
            st.write("- Crucifixo com halteres")
            st.write("- Tríceps testa")
            st.write("Treino B: Costas e Bíceps")
            st.write("- Barra fixa")
            st.write("- Remada curvada")
            st.write("- Rosca direta")
        else:
            st.write("Divisão ABC:")
            st.write("Seg: Peito e Tríceps")
            st.write("Ter: Costas e Bíceps")
            st.write("Qua: Pernas")
            st.write("Qui: Ombros e abdômen")
            st.write("Sex: Corpo inteiro (leve)")

    elif objetivo == "Emagrecimento":
        st.write("Treino com foco em resistência e queima calórica")
        st.write("- Circuito de corpo inteiro")
        st.write("- Aeróbicos após treino de musculação")
        st.write("- Curtos descansos entre séries")

    elif objetivo == "Resistência":
        st.write("Treino com repetições altas e menor carga")
        st.write("- Séries de 15-20 repetições")
        st.write("- Exercícios compostos e funcionais")
        st.write("- Foco em técnica e forma")

    else:
        st.warning("Objetivo não reconhecido.")
