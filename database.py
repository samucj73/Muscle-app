import sqlite3

def conectar():
    """
    Conecta ao banco de dados SQLite. Cria o banco se não existir.
    """
    conn = sqlite3.connect("app.db")
    return conn

def criar_tabelas():
    """
    Cria as tabelas necessárias para o funcionamento do app.
    """
    conn = conectar()
    cursor = conn.cursor()

    # Tabela de usuários
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS usuarios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        email TEXT UNIQUE NOT NULL,
        senha TEXT NOT NULL,
        idade INTEGER,
        sexo TEXT,
        peso REAL,
        altura REAL,
        objetivo TEXT,
        frequencia_treino TEXT
    )""")
    
    # Tabela de treinos
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS treinos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        usuario_id INTEGER,
        data TEXT,
        treino TEXT,
        FOREIGN KEY(usuario_id) REFERENCES usuarios(id)
    )""")
    
    # Tabela de dietas
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS dietas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        usuario_id INTEGER,
        data TEXT,
        dieta TEXT,
        FOREIGN KEY(usuario_id) REFERENCES usuarios(id)
    )""")
    
    # Tabela de progresso
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS progresso (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        usuario_id INTEGER,
        data TEXT,
        peso REAL,
        cintura REAL,
        quadril REAL,
        peito REAL,
        FOREIGN KEY(usuario_id) REFERENCES usuarios(id)
    )""")

    conn.commit()
    conn.close()

def criar_usuario(nome, email, senha, idade, sexo, peso, altura, objetivo, frequencia_treino):
    """
    Cria um novo usuário no banco de dados.
    """
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("""
    INSERT INTO usuarios (nome, email, senha, idade, sexo, peso, altura, objetivo, frequencia_treino)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (nome, email, senha, idade, sexo, peso, altura, objetivo, frequencia_treino))
    conn.commit()
    conn.close()

def obter_usuario_por_email(email):
    """
    Obtém um usuário pelo email.
    """
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("""
    SELECT * FROM usuarios WHERE email = ?
    """, (email,))
    usuario = cursor.fetchone()
    conn.close()
    return usuario
