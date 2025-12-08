# ordinamento.py

# Creazione della lista prezzi
prezzi = [45.5, 12.0, 78.3, 23.1, 56.7]

# Creare una copia ordinata della lista
prezzi_ordinati = sorted(prezzi)

# Trovare il prezzo minimo e massimo
prezzo_min = min(prezzi)
prezzo_max = max(prezzi)

# Verificare se 23.1 è nella lista
presente = 23.1 in prezzi

# Contare quanti prezzi sono maggiori di 50
count_maggiori_50 = sum(1 for p in prezzi if p > 50)

# Stampare i risultati
print("Prezzi originali:", prezzi)
print("Prezzi ordinati:", prezzi_ordinati)
print("Minimo:", prezzo_min)
print("Massimo:", prezzo_max)
print("23.1 presente:", presente)
print("Prezzi > 50:", count_maggiori_50)