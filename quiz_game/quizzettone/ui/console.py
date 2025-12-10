from typing import Dict, List, Optional
import logging
from ..data.services import (
    valida_scelta,
    genera_feedback_scelta,
    genera_feedback_correttezza,
)

logger = logging.getLogger(__name__)

def mostra_domanda(index: int, domanda: Dict, totale: int) -> None:
    """Stampa la domanda con progresso e opzioni con gestione errori."""
    try:
        if not isinstance(index, int) or index < 0:
            logger.error(f"Indice domanda non valido: {index}")
            raise ValueError(f"Indice non valido: {index}")
        
        if not isinstance(totale, int) or totale <= 0:
            logger.error(f"Totale domande non valido: {totale}")
            raise ValueError(f"Totale non valido: {totale}")
        
        if not isinstance(domanda, dict):
            logger.error(f"Domanda non è un dict: {type(domanda)}")
            raise TypeError("Domanda deve essere un dizionario")
        
        if "question" not in domanda or "options" not in domanda:
            logger.error(f"Domanda manca campi obbligatori: {domanda.keys()}")
            raise ValueError("Domanda manca campi 'question' o 'options'")
        
        print(f"\nDomanda {index + 1} di {totale}")
        print("------------------------------")
        print(domanda["question"])
        
        options = domanda["options"]
        if not isinstance(options, list) or len(options) != 4:
            logger.error(f"Opzioni non valide: {options}")
            raise ValueError("Opzioni deve essere una lista di 4 elementi")
        
        for i, opt in enumerate(options, start=1):
            if not isinstance(opt, str):
                logger.warning(f"Opzione {i} non è una stringa: {type(opt)}")
                print(f"{i}. [ERRORE: opzione non valida]")
            else:
                print(f"{i}. {opt}")
    except (ValueError, TypeError, KeyError) as e:
        logger.error(f"Errore nella visualizzazione domanda: {e}")
        print(">>> ERRORE: impossibile visualizzare la domanda")

def raccogli_risposta() -> Optional[int]:
    """Chiede la risposta e tenta di convertirla in intero con gestione errori robusta."""
    max_tentativi = 3
    tentativi = 0
    
    while tentativi < max_tentativi:
        try:
            scelta = input("Inserisci la tua scelta (1-4): ").strip()
            
            if not scelta:
                logger.debug("Input vuoto ricevuto")
                print(">>> Errore: inserisci un numero.")
                tentativi += 1
                continue
            
            try:
                scelta_int = int(scelta)
            except ValueError:
                logger.warning(f"Input non numerico: '{scelta}'")
                print(">>> Errore: inserisci un numero valido (1-4).")
                tentativi += 1
                continue
            
            if scelta_int < 1 or scelta_int > 4:
                logger.warning(f"Scelta fuori intervallo: {scelta_int}")
                print(">>> Errore: il numero deve essere tra 1 e 4.")
                tentativi += 1
                continue
            
            logger.debug(f"Input valido ricevuto: {scelta_int}")
            return scelta_int
            
        except KeyboardInterrupt:
            logger.info("Interruzione da tastiera ricevuta")
            print("\n>>> Quiz interrotto dall'utente")
            return None
        except EOFError:
            logger.warning("EOF ricevuto (fine input)")
            return None
        except Exception as e:
            logger.error(f"Errore inaspettato nella lettura input: {e}")
            tentativi += 1
            print(">>> Errore imprevisto. Riprova.")
    
    logger.warning("Massimo numero di tentativi raggiunto")
    print(">>> Massimo numero di tentativi raggiunto")
    return None

def mostra_feedback_scelta(scelta: int) -> None:
    """Feedback di stile sulla scelta."""
    try:
        if scelta is None:
            logger.debug("Scelta None, saltando feedback")
            return
        
        print("\n--- FEEDBACK SCELTA ---")
        feedback = genera_feedback_scelta(scelta)
        print(feedback)
    except Exception as e:
        logger.error(f"Errore nel feedback scelta: {e}")
        print(">>> Errore nel feedback")

def mostra_feedback_correttezza(scelta: int, correct: int) -> None:
    """Feedback sulla correttezza della risposta."""
    try:
        if scelta is None or correct is None:
            logger.debug("Scelta o correct None, saltando feedback correttezza")
            return
        
        print("\n--- ESITO ---")
        feedback = genera_feedback_correttezza(scelta, correct)
        print(feedback)
    except Exception as e:
        logger.error(f"Errore nel feedback correttezza: {e}")
        print(">>> Errore nella valutazione")

def chiedi_navigazione(totale: int) -> str:
    """
    Chiede all'utente come muoversi:
      P = precedente
      S = successiva
      numero (1..totale) = salto diretto
    Restituisce la stringa originale per la gestione nel main.
    """
    try:
        if not isinstance(totale, int) or totale <= 0:
            logger.error(f"Totale non valido: {totale}")
            raise ValueError(f"Totale non valido: {totale}")
        
        while True:
            try:
                azione = input("\nNavigazione — Precedente (P), Successiva (S), oppure numero [1..{}]: ".format(totale)).strip().upper()
                
                if not azione:
                    logger.debug("Input navigazione vuoto, default a successiva")
                    return "S"
                
                logger.debug(f"Navigazione input: {azione}")
                return azione
                
            except KeyboardInterrupt:
                logger.info("Interruzione da tastiera nella navigazione")
                return "S"
            except EOFError:
                logger.warning("EOF nella navigazione")
                return "S"
    except Exception as e:
        logger.error(f"Errore nella navigazione: {e}")
        return "S"

def mostra_risultati_finali(risposte: List[Optional[int]], punteggio: int, totale: int) -> None:
    """Stampa il riepilogo finale con validazione."""
    try:
        if not isinstance(risposte, list):
            logger.error(f"Risposte non è una lista: {type(risposte)}")
            raise TypeError("Risposte deve essere una lista")
        
        if not isinstance(punteggio, int) or punteggio < 0:
            logger.error(f"Punteggio non valido: {punteggio}")
            raise ValueError(f"Punteggio non valido: {punteggio}")
        
        if not isinstance(totale, int) or totale <= 0:
            logger.error(f"Totale non valido: {totale}")
            raise ValueError(f"Totale non valido: {totale}")
        
        percentuale = (punteggio / totale * 100) if totale > 0 else 0
        
        print("\n=== RISULTATI FINALI ===")
        print(f"Risposte date: {risposte}")
        print(f"Punteggio: {punteggio}/{totale}")
        print(f"Percentuale: {percentuale:.1f}%")
        
        if percentuale >= 80:
            print(">>> Eccellente! Ottimo lavoro!")
        elif percentuale >= 60:
            print(">>> Buono! Continua così!")
        elif percentuale >= 40:
            print(">>> Discreto. Puoi fare meglio!")
        else:
            print(">>> Insufficiente. Rivedi gli argomenti!")
        
        logger.info(f"Quiz completato: {punteggio}/{totale} ({percentuale:.1f}%)")
    except (TypeError, ValueError) as e:
        logger.error(f"Errore nella visualizzazione risultati: {e}")
        print(">>> ERRORE: impossibile visualizzare i risultati finali")
