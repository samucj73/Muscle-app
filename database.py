def criar_tabelas():
    conn = sqlite3.connect("app.db")
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
