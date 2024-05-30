import sqlite3
import getpass

# Initialiser et configurer la base de données
def init_db():
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

# Inscription d'un nouvel utilisateur
def register_user():
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    
    username = input("Entrez votre nom d'utilisateur: ")
    password = getpass.getpass("Entrez votre mot de passe: ")
    
    try:
        cursor.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, password))
        conn.commit()
        print("Inscription réussie!")
    except sqlite3.IntegrityError:
        print("Erreur: Ce nom d'utilisateur est déjà pris.")
    
    conn.close()

# Connexion d'un utilisateur existant
def login_user():
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    
    username = input("Entrez votre nom d'utilisateur: ")
    password = getpass.getpass("Entrez votre mot de passe: ")
    
    cursor.execute('SELECT * FROM users WHERE username = ? AND password = ?', (username, password))
    user = cursor.fetchone()
    
    if user:
        print("Connexion réussie!")
    else:
        print("Erreur: Nom d'utilisateur ou mot de passe incorrect.")
    
    conn.close()

# Menu principal
def main():
    init_db()
    
    while True:
        print("\n1. Inscription")
        print("2. Connexion")
        print("3. Quitter")
        choice = input("Choisissez une option: ")
        
        if choice == '1':
            register_user()
        elif choice == '2':
            login_user()
        elif choice == '3':
            print("Au revoir!")
            break
        else:
            print("Option invalide. Veuillez réessayer.")

if __name__ == "__main__":
    main()
    
