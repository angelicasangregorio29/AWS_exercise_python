# Esercizio 2.3: Conteggio Occorrenze

# Creiamo la lista dei voti
voti = ["A", "B", "A", "C", "B", "A", "D", "B", "C", "A"]

# Creiamo un dizionario vuoto
conteggio = {}

# Iteriamo sulla lista voti
for voto in voti:
    # Usando get per gestire chiavi mancanti
    conteggio[voto] = conteggio.get(voto, 0) + 1

# Stampiamo il risultato finale
print("Conteggio voti:", conteggio)