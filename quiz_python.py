# === QUIZ PYTHON ===
print("=== QUIZ PYTHON ===")
print("Domanda: Qual è il tuo linguaggio di programmazione preferito?\n")

print("1. Python")
print("2. JavaScript")
print("3. Java")
print("4. C++\n")

try:
    scelta = int(input("Inserisci la tua scelta (1-4): "))
    print("\n--- RISPOSTA ---")
    if scelta == 1:
        print("Hai scelto: Python")
        print("Ottima scelta! Perché lo useremo per i prossimi quattro mesi!!")
    elif scelta == 2:
        print("Hai scelto: JavaScript")
        print("Interessante! Ma mi vuoi male!")
    elif scelta == 3:
        print("Hai scelto: Java")
        print("Solida scelta! Ok, però si potrebbe fare meglio! Tipo Python!")
    elif scelta == 4:
        print("Hai scelto: C++")
        print("Potente! C++ è ottimo per le performance, ma lasciamolo ai nerd!")
    else:
        print("Errore: devi scegliere un numero tra 1 e 4!")
except ValueError:
    print("\n--- RISPOSTA ---")
    print("Errore: devi inserire un numero valido!")