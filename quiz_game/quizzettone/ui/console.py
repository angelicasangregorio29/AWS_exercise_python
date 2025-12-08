from typing import Dict, List, Optional
from ..data.services import (
    valida_scelta,
    genera_feedback_scelta,
    genera_feedback_correttezza,
)

def mostra_domanda(index: int, domanda: Dict, totale: int) -> None:
    """Stampa la domanda con progresso e opzioni."""
    print(f"\nDomanda {index + 1} di {totale}")
    print("------------------------------")
    print(domanda["question"])
    for i, opt in enumerate(domanda["options"], start=1):
        print(f"{i}. {opt}")

def raccogli_risposta() -> Optional[int]:
    """Chiede la risposta e tenta di convertirla in intero."""
    try:
        scelta = int(input("Inserisci la tua scelta (1-4): ").strip())
        print(f"[DEBUG] Input utente: {scelta}")
        return scelta
    except ValueError:
        print(">>> Errore: inserisci un numero.")
        return None

def mostra_feedback_scelta(scelta: int) -> None:
    """Feedback di stile sulla scelta."""
    print("\n--- FEEDBACK SCELTA ---")
    print(genera_feedback_scelta(scelta))

def mostra_feedback_correttezza(scelta: int, correct: int) -> None:
    """Feedback sulla correttezza della risposta."""
    print("\n--- ESITO ---")
    print(genera_feedback_correttezza(scelta, correct))

def chiedi_navigazione(totale: int) -> str:
    """
    Chiede all'utente come muoversi:
      P = precedente
      S = successiva
      numero (1..totale) = salto diretto
    Restituisce la stringa originale per la gestione nel main.
    """
    azione = input("\nNavigazione — Precedente (P), Successiva (S), oppure numero [1..{}]: ".format(totale)).strip().upper()
    print(f"[DEBUG] Navigazione input: {azione}")
    return azione

def mostra_risultati_finali(risposte: List[Optional[int]], punteggio: int, totale: int) -> None:
    """Stampa il riepilogo finale."""
    print("\n=== RISULTATI FINALI ===")
    print(f"Risposte: {risposte}")
    print(f"Punteggio: {punteggio}/{totale}")