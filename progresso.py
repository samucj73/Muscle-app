from datetime import date
from database import conectar

def registrar_progresso(usuario_id, peso, cintura, quadril, peito):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO progresso (usuario_id, data, peso, cintura, quadril, peito)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (usuario_id, str(date.today()), peso, cintura, quadril, peito))
    conn.commit()
    conn.close()

def obter_progresso(usuario_id):
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
    return dados
