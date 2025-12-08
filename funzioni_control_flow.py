# Funzioni con return

def restituisce_numero_pari(numero):
    if numero % 2 == 0:
        return True
    else:
        return False

# Test
print("Test restituisce_numero_pari:")
print(restituisce_numero_pari(4))   # True
print(restituisce_numero_pari(7))   # False
print()


def calcola_sconto(prezzo, eta):
    if eta < 18:
        prezzo_finale = prezzo * 0.8   # sconto 20%
    elif eta >= 65:
        prezzo_finale = prezzo * 0.7   # sconto 30%
    else:
        prezzo_finale = prezzo         # nessuno sconto
    return prezzo_finale

# Test
print("Test calcola_sconto:")
print(calcola_sconto(100, 15))   # 80.0
print(calcola_sconto(100, 70))   # 70.0
print(calcola_sconto(100, 30))   # 100.0
print()


def valuta_temperatura(gradi):
    if gradi < 15:
        return "Freddo"
    elif 15 <= gradi <= 25:
        return "Mite"
    else:
        return "Caldo"

# Test
print("Test valuta_temperatura:")
print(valuta_temperatura(10))   # Freddo
print(valuta_temperatura(20))   # Mite
print(valuta_temperatura(30))   # Caldo
print()


# Funzioni con print (senza return)

def stampa_tabellina(numero):
    print(f"Tabellina del {numero}:")
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")
    print()

# Test
stampa_tabellina(5)


def disegna_rettangolo(larghezza, altezza):
    print(f"Rettangolo pieno {larghezza}x{altezza}:")
    for i in range(altezza):
        for j in range(larghezza):
            print("*", end="")
        print()
    print()

# Test
disegna_rettangolo(5, 3)


def disegna_rettangolo_bordo(larghezza, altezza):
    print(f"Rettangolo bordo {larghezza}x{altezza}:")
    for i in range(altezza):
        for j in range(larghezza):
            # Stampa asterisco solo sul bordo (prima/ultima riga o prima/ultima colonna)
            if i == 0 or i == altezza - 1 or j == 0 or j == larghezza - 1:
                print("*", end="")
            else:
                print(" ", end="")
        print()
    print()

# Test
disegna_rettangolo_bordo(10, 4)
disegna_rettangolo_bordo(5, 5)
disegna_rettangolo_bordo(3, 2)