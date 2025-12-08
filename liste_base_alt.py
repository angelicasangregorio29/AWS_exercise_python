# liste_base_alt.py

# Creazione della lista iniziale
server = ["web01", "db01", "cache01"]

# Aggiungere "backup01" alla fine con concatenazione
server = server + ["backup01"]

# Inserire "proxy01" all'inizio con slicing
server = ["proxy01"] + server

# Rimuovere "cache01" con list comprehension
server = [s for s in server if s != "cache01"]

# Stampare la lista finale
print(server)

# Stampare la lunghezza della lista
print("Numero server:", len(server))