import sys
from pathlib import Path

# Allow running this file both as a package module and as a standalone script.
# When executed directly (`python quiz_game/quizzettone/main.py`), Python sets
# `__package__` to None and relative imports fail. We add the package root to
# `sys.path` and provide an import fallback to make imports robust.
if __package__ is None and __name__ == "__main__":
    pkg_root = Path(__file__).resolve().parents[1]  # .../quiz_game
    sys.path.insert(0, str(pkg_root))

try:
    from .data.repository import carica_domande
    from .data.services import valida_scelta, calcola_punteggio
    from .ui.console import (
        mostra_domanda,
        raccogli_risposta,
        mostra_feedback_scelta,
        mostra_feedback_correttezza,
        chiedi_navigazione,
        mostra_risultati_finali,
    )
except Exception:
    # Fallback for environments where package-relative imports still fail.
    from quizzettone.data.repository import carica_domande
    from quizzettone.data.services import valida_scelta, calcola_punteggio
    from quizzettone.ui.console import (
        mostra_domanda,
        raccogli_risposta,
        mostra_feedback_scelta,
        mostra_feedback_correttezza,
        chiedi_navigazione,
        mostra_risultati_finali,
    )

def main():
    print(">>> Avvio del quiz...\n")

    # Puoi scegliere il file da caricare: "domande.txt" oppure "domande.json"
    domande = carica_domande("domande.json")
    totale = len(domande)
    risposte = [None] * totale  # lista che memorizza le risposte dell'utente

    counter = 0
    while 0 <= counter < totale:
        print(f"[DEBUG] Counter attuale: {counter}")
        domanda = domande[counter]

        mostra_domanda(counter, domanda, totale)
        scelta = raccogli_risposta()

        if valida_scelta(scelta):
            risposte[counter] = scelta  # sovrascrive sempre la risposta corrente
            mostra_feedback_scelta(scelta)
            mostra_feedback_correttezza(scelta, domanda["correct"])
        else:
            print(">>> Scelta non valida. Riprova oppure naviga.")

        azione = chiedi_navigazione(totale)

        if azione == "P":
            if counter > 0:
                counter -= 1
                print(">>> Torniamo alla domanda precedente...")
            else:
                print(">>> Sei già alla prima domanda, non puoi tornare indietro!")
        elif azione == "S":
            counter += 1
            print(">>> Passiamo alla domanda successiva...")
        elif azione.isdigit():
            numero = int(azione)
            if 1 <= numero <= totale:
                counter = numero - 1
                print(f">>> Salto alla domanda {numero}...")
            else:
                print(">>> Numero non valido! Rimaniamo sulla stessa domanda.")
        else:
            counter += 1
            print(">>> Passiamo alla domanda successiva...")

    punteggio = calcola_punteggio(domande, risposte)
    mostra_risultati_finali(risposte, punteggio, totale)
    print("\n>>> Fine del quiz. Grazie per aver partecipato!")

if __name__ == "__main__":
    main()