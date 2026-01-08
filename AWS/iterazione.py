# iterazione.py

utenti = {
    "alice": "admin",
    "bob": "user",
    "charlie": "guest"
}

# Iterazione su chiavi e valori
for username, ruolo in utenti.items():
    print(f"Username: {username}, Ruolo: {ruolo}")

# Verifica se "bob" è presente
print("bob presente:", "bob" in utenti)

# Stampare tutte le chiavi
print("Usernames:", utenti.keys())

# Stampare tutti i valori
print("Ruoli:", utenti.values())