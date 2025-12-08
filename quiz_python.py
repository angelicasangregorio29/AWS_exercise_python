# === QUIZ PYTHON CON FUNZIONI ===

def mostra_domanda():
    """Stampa la domanda e le opzioni"""
    print("=== QUIZ PYTHON ===")
    print("Domanda: Qual è il tuo linguaggio di programmazione preferito?\n")
    print("1. Python")
    print("2. JavaScript")
    print("3. Java")
    print("4. C++\n")

def raccogli_risposta():
    """Chiede input all'utente e restituisce un numero"""
    print(">>> Sto raccogliendo la risposta dall'utente...")
    try:
        scelta = int(input("Inserisci la tua scelta (1-4): "))
        print(f">>> Hai inserito: {scelta}")
        return scelta
    except ValueError:
        print(">>> Errore: input non numerico!")
        return None

def valida_scelta(scelta):
    """Verifica se la scelta è valida (1-4)"""
    print(">>> Sto validando la scelta...")
    if scelta in [1, 2, 3, 4]:
        print(">>> Scelta valida!")
        return True
    else:
        print(">>> Scelta NON valida!")
        return False

def genera_feedback(scelta):
    """Genera un messaggio personalizzato in base alla scelta"""
    print(">>> Sto generando il feedback...")
    if scelta == 1:
        return "Hai scelto: Python\nOttima scelta! Perché lo useremo per i prossimi quattro mesi!!"
    elif scelta == 2:
        return "Hai scelto: JavaScript\nInteressante! Ma mi vuoi male!"
    elif scelta == 3:
        return "Hai scelto: Java\nSolida scelta! Ok, però si potrebbe fare meglio! Tipo Python!"
    elif scelta == 4:
        return "Hai scelto: C++\nPotente! C++ è ottimo per le performance, ma lasciamolo ai nerd!"
    else:
        return "Errore: devi scegliere un numero tra 1 e 4!"

def mostra_feedback(messaggio):
    """Stampa il feedback formattato"""
    print("\n--- RISPOSTA ---")
    print(messaggio)

# === PROGRAMMA PRINCIPALE ===
print(">>> Avvio del programma principale...")
mostra_domanda()
scelta = raccogli_risposta()

if scelta is not None and valida_scelta(scelta):
    messaggio = genera_feedback(scelta)
else:
    messaggio = "Errore: devi scegliere un numero tra 1 e 4!"

mostra_feedback(messaggio)
print(">>> Fine del programma.")