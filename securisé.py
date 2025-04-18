import hashlib

# Enregistrement des utilisateurs
users = {}
for _ in range(3):
    name = input("Nom d'utilisateur : ")
    password = input("Mot de passe : ")
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    users[name] = hashed_password

# Connexion
name = input("\nConnexion\nNom d'utilisateur : ")
password = input("Mot de passe : ")
hashed_input = hashlib.sha256(password.encode()).hexdigest()

# Vérification
if name in users and users[name] == hashed_input:
    print("✅ Bienvenue", name)
else:
    print("❌ Identifiants incorrects")
