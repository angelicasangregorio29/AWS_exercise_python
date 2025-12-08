from typing import List, Dict, Optional

def valida_scelta(scelta: Optional[int]) -> bool:
    """Verifica se la scelta è un intero tra 1 e 4."""
    return isinstance(scelta, int) and scelta in (1, 2, 3, 4)

def calcola_punteggio(domande: List[Dict], risposte: List[Optional[int]]) -> int:
    """Restituisce il numero di risposte corrette."""
    score = 0
    for i, domanda in enumerate(domande):
        if i < len(risposte) and risposte[i] is not None:
            if risposte[i] == domanda["correct"]:
                score += 1
    return score

def genera_feedback_scelta(scelta: int) -> str:
    """Feedback non legato alla correttezza, solo di stile."""
    if scelta == 1:
        return "Ottima scelta!"
    elif scelta == 2:
        return "Interessante!"
    elif scelta == 3:
        return "Solida scelta!"
    elif scelta == 4:
        return "Potente!"
    return "Scelta non valida."

def genera_feedback_correttezza(scelta: int, correct: int) -> str:
    """Feedback sulla correttezza della risposta."""
    return "Hai indovinato!" if scelta == correct else "Non hai indovinato."