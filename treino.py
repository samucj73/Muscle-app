import random
from database import conectar

# Banco básico de exercícios (sem uso de anabolizantes, apenas peso corporal, halteres e barras simples)
EXERCICIOS = {
    "Hipertrofia": [
        "Agachamento com halteres", "Flexão de braços", "Remada curvada", "Desenvolvimento com halteres", 
        "Afundo", "Puxada na barra", "Elevação lateral", "Rosca direta", "Tríceps banco", "Stiff com halteres"
    ],
    "Emagrecimento": [
        "Burpee", "Corrida no lugar", "Agachamento com salto", "Mountain climber", 
        "Pular corda", "Polichinelo", "Flexão dinâmica", "Abdominal bicicleta"
    ],
    "Resistência": [
        "Corrida leve", "Circuito funcional", "Subida de escada", "Prancha", 
        "Agachamento isométrico", "Flexão isométrica", "Abdominal prancha lateral", "Polichinelo"
    ]
}

def gerar_treino(objetivo, frequencia):
    treino_base = EXERCICIOS.get(objetivo, [])
    dias = {"1-2x": 2, "3-4x": 4, "5-6x": 6}[frequencia]

    plano = {}
    for dia in range(1, dias + 1):
        plano[f"Dia {dia}"] = random.sample(treino_base, min(5, len(treino_base)))

    return plano

def salvar_treino(usuario_id, treino_dict):
    conn = conectar()
    cursor = conn.cursor()
    import json
    from datetime import date

    treino_json = json.dumps(treino_dict)
    cursor.execute("INSERT INTO treinos (usuario_id, data, treino) VALUES (?, ?, ?)", 
                   (usuario_id, str(date.today()), treino_json))
    conn.commit()
    conn.close()

def obter_treinos(usuario_id):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT data, treino FROM treinos WHERE usuario_id = ? ORDER BY data DESC", (usuario_id,))
    dados = cursor.fetchall()
    conn.close()
    return dados
