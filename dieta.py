import random

# Banco de dados simples de alimentos
ALIMENTOS = {
    "Hipertrofia": [
        "Frango grelhado", "Arroz integral", "Batata doce", "Ovos", "Brócolis", "Peito de peru", "Quinoa", "Abacate", "Amêndoas", "Iogurte grego"
    ],
    "Emagrecimento": [
        "Salada de folhas verdes", "Peixe grelhado", "Abóbora", "Tomate", "Pepino", "Frango cozido", "Espinafre", "Cenoura", "Aveia", "Iogurte natural"
    ],
    "Resistência": [
        "Ovos cozidos", "Arroz integral", "Frango desfiado", "Peito de peru", "Abacate", "Alface", "Brócolis", "Batata doce", "Banana", "Maçã"
    ]
}

def gerar_dieta(objetivo):
    alimentos_base = ALIMENTOS.get(objetivo, [])
    dieta = {}
    
    for refeicao in ["Café da manhã", "Almoço", "Lanche da tarde", "Jantar"]:
        dieta[refeicao] = random.sample(alimentos_base, min(3, len(alimentos_base)))

    return dieta

def salvar_dieta(usuario_id, dieta_dict):
    import json
    from datetime import date
    from database import conectar
    
    conn = conectar()
    cursor = conn.cursor()
    dieta_json = json.dumps(dieta_dict)
    cursor.execute("INSERT INTO dietas (usuario_id, data, dieta) VALUES (?, ?, ?)", 
                   (usuario_id, str(date.today()), dieta_json))
    conn.commit()
    conn.close()

def obter_dietas(usuario_id):
    from database import conectar
    
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT data, dieta FROM dietas WHERE usuario_id = ? ORDER BY data DESC", (usuario_id,))
    dados = cursor.fetchall()
    conn.close()
    return dados
