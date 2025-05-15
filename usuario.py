import sqlite3
import hashlib
from database import conectar

def hash_senha(senha):
    return hashlib.sha256(senha.encode()).hexdigest()

def cadastrar_usuario(nome, email, senha):
    conn = conectar()
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO usuarios (nome, email, senha) VALUES (?, ?, ?)",
                       (nome, email, hash_senha(senha)))
        conn.commit()
        return True
    except sqlite3.IntegrityError:
        return False
    finally:
        conn.close()

def autenticar_usuario(email, senha):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM usuarios WHERE email = ? AND senha = ?", (email, hash_senha(senha)))
    usuario = cursor.fetchone()
    conn.close()
    return usuario

def atualizar_perfil(usuario_id, idade, sexo, peso, altura, objetivo, frequencia_treino):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("""
    UPDATE usuarios SET idade = ?, sexo = ?, peso = ?, altura = ?, objetivo = ?, frequencia_treino = ?
    WHERE id = ?
    """, (idade, sexo, peso, altura, objetivo, frequencia_treino, usuario_id))
    conn.commit()
    conn.close()

def obter_perfil(usuario_id):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT nome, email, idade, sexo, peso, altura, objetivo, frequencia_treino FROM usuarios WHERE id = ?", (usuario_id,))
    dados = cursor.fetchone()
    conn.close()
    return dados
