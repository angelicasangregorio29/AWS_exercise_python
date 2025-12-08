# Esercizio 3.1: Lista di Dizionari

# Creiamo la lista di prodotti (ognuno è un dizionario)
prodotti = [
    {"nome": "Laptop", "prezzo": 899.99, "quantita": 5},
    {"nome": "Mouse", "prezzo": 25.50, "quantita": 50},
    {"nome": "Tastiera", "prezzo": 75.00, "quantita": 30},
    {"nome": "Monitor", "prezzo": 299.99, "quantita": 15}
]

# Stampiamo solo i prodotti con prezzo > 100
print("Prodotti > 100€:")
for prodotto in prodotti:
    if prodotto["prezzo"] > 100:
        print(f"- {prodotto['nome']}: €{prodotto['prezzo']}")

# Calcoliamo il valore totale dell'inventario
valore_totale = 0
for prodotto in prodotti:
    valore_totale += prodotto["prezzo"] * prodotto["quantita"]

print(f"\nValore totale inventario: €{valore_totale:.2f}")