# Supermercato Robotizzato 2050
lista_spesa = {}  # {prodotto: prezzo}
carrello = {}     # {prodotto: quantita}

def mostra_menu():
    print("\n=== SUPERMERCATO ROBOT 2050 ===")
    print("1. Aggiungi alla Lista Spesa")
    print("2. Rimuovi dalla Lista Spesa")
    print("3. Aggiungi al Carrello (solo autorizzati)")
    print("4. Rimuovi dal Carrello")
    print("5. Mostra Lista Spesa")
    print("6. Mostra Carrello e Totale")
    print("7. Checkout e Esci")

def totale_carrello():
    totale = 0
    for prod, qta in carrello.items():
        if prod in lista_spesa:
            totale += qta * lista_spesa[prod]
    return totale

while True:
    mostra_menu()
    scelta = input("Scegli (1-7): ").strip()
    
    if scelta == '1':
        prod = input("Prodotto: ").strip().lower()
        prezzo = float(input("Prezzo unitario: "))
        lista_spesa[prod] = prezzo
        print(f"{prod} aggiunto alla Lista Spesa.")
    
    elif scelta == '2':
        if lista_spesa:
            print("Lista Spesa:", list(lista_spesa.keys()))
            prod = input("Rimuovi: ").strip().lower()
            if prod in lista_spesa:
                del lista_spesa[prod]
                print("Rimosso.")
            else:
                print("Non trovato.")
        else:
            print("Lista vuota.")
    
    elif scelta == '3':
        prod = input("Prodotto per Carrello: ").strip().lower()
        if prod not in lista_spesa:
            print("❌ ERRORE ROBOT: Prodotto non autorizzato dalla Lista Spesa!")
        else:
            qta = int(input("Quantità: "))
            carrello[prod] = carrello.get(prod, 0) + qta
            print(f"{qta} x {prod} aggiunto al Carrello.")
    
    elif scelta == '4':
        if carrello:
            print("Carrello:", list(carrello.keys()))
            prod = input("Rimuovi: ").strip().lower()
            if prod in carrello:
                del carrello[prod]
                print("Rimosso.")
            else:
                print("Non trovato.")
        else:
            print("Carrello vuoto.")
    
    elif scelta == '5':
        print("Lista Spesa:", lista_spesa if lista_spesa else "Vuota")
    
    elif scelta == '6':
        print("Carrello:", carrello if carrello else "Vuoto")
        print(f"Totale: €{totale_carrello():.2f}")
    
    elif scelta == '7':
        print("\n=== SCONTRINO FINALE ===")
        print("Carrello:", carrello)
        print(f"TOTALE: €{totale_carrello():.2f}")
        print("Grazie per lo shopping robotico!")
        break  # Termina
    
    else:
        print("Scelta non valida.")
