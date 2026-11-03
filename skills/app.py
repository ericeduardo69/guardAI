import sqlite3


def init_db():
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username TEXT, password TEXT)')
    
    cursor.execute("INSERT OR IGNORE INTO users (id, username, password) VALUES (1, 'admin', 'admin123')")
    conn.commit()
    conn.close()


def login(username, password):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    
    query = "SELECT * FROM users WHERE username = ? AND password = ?"
    print(f"\n[DEBUG] Query preparada para execução.")
    
    try:
        cursor.execute(query, (username, password))
        user = cursor.fetchone()
    except Exception as e:
        print(f"Erro: {e}")
        user = None
        
    conn.close()
    return user

if __name__ == '__main__':
    init_db()
    print("--- Sistema de Login (Seguro) ---")
    u = input("Utilizador: ")
    p = input("Palavra-passe: ")
    
    result = login(u, p)
    if result:
        print(f"[SUCESSO] Login efetuado com sucesso! Bem-vindo, {result[1]}")
    else:
        print("[ERRO] Credenciais inválidas.")
