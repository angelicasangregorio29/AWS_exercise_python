from text_analyzer import conta_caratteri, frequenza_caratteri, leggi_file

if __name__ == "__main__":
    percorso = input("Inserisci il percorso del file di testo: ")
    testo = leggi_file(percorso)

    if testo:
        totale = conta_caratteri(testo)
        print(f"Numero totale di caratteri: {totale}")

        freq = frequenza_caratteri(testo)
        print("Caratteri con frequenza > 5:")
        for char, count in freq.items():
            if count > 5:
                print(f"'{char}': {count}")