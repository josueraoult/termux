import getpass
from colorama import init, Fore, Style

# Initialisation de colorama
init(autoreset=True)

# Stockage des utilisateurs en mémoire (dictionnaire)
users = {}

# Inscription d'un nouvel utilisateur
def register_user():
    print(Fore.GREEN + "=== Inscription ===")
    username = input(Fore.CYAN + "Entrez votre nom d'utilisateur: ")
    password = getpass.getpass(Fore.CYAN + "Entrez votre mot de passe: ")
    
    if username in users:
        print(Fore.RED + "Erreur: Ce nom d'utilisateur est déjà pris.")
    else:
        users[username] = password
        print(Fore.GREEN + "Inscription réussie!")

# Connexion d'un utilisateur existant
def login_user():
    print(Fore.GREEN + "=== Connexion ===")
    username = input(Fore.CYAN + "Entrez votre nom d'utilisateur: ")
    password = getpass.getpass(Fore.CYAN + "Entrez votre mot de passe: ")
    
    if username in users and users[username] == password:
        print(Fore.GREEN + "Connexion réussie!")
    else:
        print(Fore.RED + "Erreur: Nom d'utilisateur ou mot de passe incorrect.")

# Menu principal
def main():
    while True:
        print(Fore.YELLOW + "\n=== Menu Principal ===")
        print(Fore.MAGENTA + "1. Inscription")
        print(Fore.MAGENTA + "2. Connexion")
        print(Fore.MAGENTA + "3. Quitter")
        choice = input(Fore.CYAN + "Choisissez une option: ")
        
        if choice == '1':
            register_user()
        elif choice == '2':
            login_user()
        elif choice == '3':
            print(Fore.YELLOW + "Au revoir!")
            break
        else:
            print(Fore.RED + "Option invalide. Veuillez réessayer.")

if __name__ == "__main__":
    main()
    
