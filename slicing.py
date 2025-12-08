# slicing.py

# Creazione della lista temperature
temperature = [15, 18, 22, 25, 28, 30, 27, 24, 20]

# Stampare la prima temperatura (indice 0)
print("Prima temperatura:", temperature[0])

# Stampare l'ultima temperatura (indice -1)
print("Ultima temperatura:", temperature[-1])

# Stampare le temperature dalla posizione 2 alla 5 (esclusa)
print("Temperature [2:5]:", temperature[2:5])

# Stampare tutte le temperature con step 2 (saltando una ogni due)
print("Ogni due:", temperature[::2])