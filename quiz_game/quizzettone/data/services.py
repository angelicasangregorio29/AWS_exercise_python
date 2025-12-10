from typing import List, Dict, Optional
import logging

logger = logging.getLogger(__name__)

def valida_scelta(scelta: Optional[int]) -> bool:
    """Verifica se la scelta è un intero tra 1 e 4."""
    try:
        if scelta is None:
            logger.debug("Scelta è None")
            return False
        if not isinstance(scelta, int):
            logger.warning(f"Scelta non è un intero: {type(scelta)}")
            return False
        if scelta not in (1, 2, 3, 4):
            logger.warning(f"Scelta fuori intervallo: {scelta}")
            return False
        return True
    except Exception as e:
        logger.error(f"Errore nella validazione della scelta: {e}")
        return False

def calcola_punteggio(domande: List[Dict], risposte: List[Optional[int]]) -> int:
    """Restituisce il numero di risposte corrette con gestione errori."""
    try:
        if not domande:
            logger.warning("Lista domande vuota")
            return 0
        
        if not risposte:
            logger.warning("Lista risposte vuota")
            return 0
        
        if len(domande) != len(risposte):
            logger.warning(f"Mismatch: {len(domande)} domande, {len(risposte)} risposte")
        
        score = 0
        for i, domanda in enumerate(domande):
            try:
                if i >= len(risposte):
                    logger.debug(f"Risposta {i} mancante")
                    continue
                
                if risposte[i] is None:
                    logger.debug(f"Risposta {i} è None")
                    continue
                
                if "correct" not in domanda:
                    logger.error(f"Domanda {i} manca campo 'correct'")
                    continue
                
                if risposte[i] == domanda["correct"]:
                    score += 1
            except (KeyError, TypeError) as e:
                logger.error(f"Errore elaborazione domanda {i}: {e}")
                continue
        
        logger.info(f"Punteggio calcolato: {score}/{len(domande)}")
        return score
    except Exception as e:
        logger.error(f"Errore critico nel calcolo punteggio: {e}")
        return 0

def genera_feedback_scelta(scelta: int) -> str:
    """Feedback non legato alla correttezza, solo di stile."""
    try:
        if not isinstance(scelta, int):
            logger.warning(f"Scelta non è un intero: {type(scelta)}")
            return "Scelta non valida."
        
        feedback_map = {
            1: "Ottima scelta!",
            2: "Interessante!",
            3: "Solida scelta!",
            4: "Potente!"
        }
        
        if scelta not in feedback_map:
            logger.warning(f"Scelta fuori intervallo per feedback: {scelta}")
            return "Scelta non valida."
        
        return feedback_map[scelta]
    except Exception as e:
        logger.error(f"Errore nel feedback scelta: {e}")
        return "Errore nella generazione del feedback."

def genera_feedback_correttezza(scelta: int, correct: int) -> str:
    """Feedback sulla correttezza della risposta."""
    try:
        if not isinstance(scelta, int) or not isinstance(correct, int):
            logger.error(f"Parametri non interi: scelta={type(scelta)}, correct={type(correct)}")
            return "Errore nella valutazione."
        
        if scelta not in (1, 2, 3, 4) or correct not in (1, 2, 3, 4):
            logger.warning(f"Valori fuori intervallo: scelta={scelta}, correct={correct}")
            return "Dati non validi."
        
        if scelta == correct:
            return "Hai indovinato!"
        else:
            return f"Non hai indovinato. La risposta corretta era: {correct}"
    except Exception as e:
        logger.error(f"Errore nella generazione feedback correttezza: {e}")
        return "Errore nella valutazione."
