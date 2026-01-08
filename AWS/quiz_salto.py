# === QUIZ MULTI-DOMANDA CON NAVIGAZIONE AVANZATA (SALTO) ===

lista_domande = [
    "Qual è la capitale della Francia?",
    "Qual è il linguaggio di programmazione più usato nel web?",
    "Chi ha scritto 'La Divina Commedia'?",
    "Qual è il colore della bandiera italiana?",
    "In che anno è iniziata la Seconda Guerra Mondiale?"
]

lista_opzioni = [
    ["1. Parigi", "2. Londra", "3. Roma", "4. Madrid"],
    ["1. Python", "2. JavaScript", "3. C++", "4. Java"],
    ["1. Dante Alighieri", "2. Alessandro Manzoni", "3. Giovanni Boccaccio", "4. Italo Calvino"],
    ["1. Rosso, Bianco, Verde", "2. Blu, Bianco, Rosso", "3. Giallo, Nero, Verde", "4. Bianco, Nero, Rosso"],
    ["1. 1914", "2. 1939", "3. 1945", "4. 1929"]
]

lista_domande_length = len(lista_domande)
risultato_finale = []  # lista che memorizza le risposte dell'utente

def mostra_domanda(counter_domanda_corrente):
    """Mostra la domanda corrente con il numero di progresso"""
    print(f"\nDomanda {counter_domanda_corrente + 1} di {lista_domande_length}")
    print("------------------------------")
    print(lista_domande[counter_domanda_corrente])
    for opzione in lista_opzioni[counter_domanda_corrente]:
        print(opzione)

def raccogli_risposta():
    """Raccoglie la risposta dell'utente"""
    try:
        scelta = int(input("Inserisci la tua scelta (1-4): "))
        return scelta
    except ValueError:
        return None

def valida_scelta(scelta):
    """Verifica se la scelta è valida"""
    return scelta in [1, 2, 3, 4]

def mostra_feedback(scelta):
    """Mostra feedback semplice"""
    print("\n--- RISPOSTA ---")
    if scelta == 1:
        print(">>> Ottima scelta!")
    elif scelta == 2:
        print(">>> Interessante!")
    elif scelta == 3:
        print(">>> Solida scelta!")
    elif scelta == 4:
        print(">>> Potente!")
    else:
        print(">>> Errore: devi scegliere un numero tra 1 e 4!")

# === PROGRAMMA PRINCIPALE ===
print(">>> Avvio del quiz...\n")

counter_domanda_corrente = 0

while counter_domanda_corrente < lista_domande_length:
    print(f"[DEBUG] Counter attuale: {counter_domanda_corrente}")
    
    mostra_domanda(counter_domanda_corrente)
    scelta = raccogli_risposta()
    
    if scelta is not None and valida_scelta(scelta):
        mostra_feedback(scelta)
        
        # --- Gestione della memoria ---
        if len(risultato_finale) > counter_domanda_corrente:
            print(f"[DEBUG] Sovrascrivo la risposta alla domanda {counter_domanda_corrente + 1}")
            risultato_finale[counter_domanda_corrente] = scelta
        else:
            print(f"[DEBUG] Aggiungo nuova risposta alla domanda {counter_domanda_corrente + 1}")
            risultato_finale.append(scelta)
    else:
        print(">>> Input non valido.")

    # Navigazione avanzata con salto
    azione = input("\nVuoi andare alla domanda Precedente (P), Successiva (S) o saltare a una domanda specifica (numero)? ").upper()
    
    if azione == "P":
        if counter_domanda_corrente > 0:
            counter_domanda_corrente -= 1
            print(">>> Torniamo alla domanda precedente...")
        else:
            print(">>> Sei già alla prima domanda, non puoi tornare indietro!")
            counter_domanda_corrente += 1
    elif azione.isdigit():
        numero = int(azione)
        if 1 <= numero <= lista_domande_length:
            counter_domanda_corrente = numero - 1
            print(f">>> Salto alla domanda {numero}...")
        else:
            print(">>> Numero non valido! Rimaniamo sulla stessa domanda.")
    else:
        counter_domanda_corrente += 1
        print(">>> Passiamo alla domanda successiva...")

print("\n>>> Fine del quiz. Grazie per aver partecipato!")
print(">>> Risultati finali:", risultato_finale)