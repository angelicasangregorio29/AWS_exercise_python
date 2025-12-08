# main.py

from quizzettone.ui.console import mostra_domanda, mostra_feedback
from quizzettone.data.repository import carica_domande
from quizzettone.data.services import valida_scelta

def main():
    domande = carica_domande("domande.txt")
    for i, domanda in enumerate(domande):
        mostra_domanda(i, domanda)
        scelta = int(input("Inserisci la tua scelta (1-4): "))
        if valida_scelta(scelta):
            mostra_feedback(scelta)
        else:
            print("Errore: scelta non valida!")

if __name__ == "__main__":
    main()