import sys
import logging
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

# Configura logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(sys.stdout),
        logging.FileHandler('quiz.log')
    ]
)
logger = logging.getLogger(__name__)

def main():
    """Main function per il quiz con gestione eccezioni robusta."""
    try:
        logger.info(">>> Avvio del quiz...\n")
        print(">>> Avvio del quiz...\n")

        # Puoi scegliere il file da caricare: "domande.txt" oppure "domande.json"
        try:
            domande = carica_domande("domande.json")
        except FileNotFoundError as e:
            logger.error(f"File domande non trovato: {e}")
            print(">>> ERRORE: File domande non trovato. Assicurati che 'domande.json' esista.")
            return
        except ValueError as e:
            logger.error(f"File domande non valido: {e}")
            print(f">>> ERRORE: {e}")
            return
        except Exception as e:
            logger.error(f"Errore inaspettato nel caricamento domande: {e}")
            print(">>> ERRORE: Impossibile caricare le domande. Controlla il file.")
            return
        
        if not domande:
            logger.error("Nessuna domanda caricata")
            print(">>> ERRORE: Nessuna domanda caricata")
            return
        
        totale = len(domande)
        logger.info(f"Caricate {totale} domande con successo")
        
        risposte = [None] * totale  # lista che memorizza le risposte dell'utente

        counter = 0
        while 0 <= counter < totale:
            try:
                logger.debug(f"Domanda attuale: {counter + 1}/{totale}")
                print(f"[DEBUG] Counter attuale: {counter}")
                
                domanda = domande[counter]

                mostra_domanda(counter, domanda, totale)
                scelta = raccogli_risposta()

                if scelta is None:
                    # Errore critico o interruzione
                    logger.warning("Input non valido, passando alla prossima")
                    counter += 1
                    continue

                if valida_scelta(scelta):
                    risposte[counter] = scelta  # sovrascrive sempre la risposta corrente
                    logger.info(f"Risposta registrata per domanda {counter + 1}: {scelta}")
                    mostra_feedback_scelta(scelta)
                    mostra_feedback_correttezza(scelta, domanda.get("correct"))
                else:
                    logger.warning(f"Scelta non valida: {scelta}")
                    print(">>> Scelta non valida. Riprova oppure naviga.")

                azione = chiedi_navigazione(totale)

                if azione == "P":
                    if counter > 0:
                        counter -= 1
                        logger.debug(f"Navigazione: torna alla domanda {counter + 1}")
                        print(">>> Torniamo alla domanda precedente...")
                    else:
                        logger.debug("Tentativo di tornare indietro da prima domanda")
                        print(">>> Sei già alla prima domanda, non puoi tornare indietro!")
                elif azione == "S":
                    counter += 1
                    logger.debug(f"Navigazione: prossima domanda {counter + 1}")
                    print(">>> Passiamo alla domanda successiva...")
                elif azione.isdigit():
                    numero = int(azione)
                    if 1 <= numero <= totale:
                        counter = numero - 1
                        logger.debug(f"Navigazione: salto alla domanda {numero}")
                        print(f">>> Salto alla domanda {numero}...")
                    else:
                        logger.warning(f"Numero domanda non valido: {numero}")
                        print(">>> Numero non valido! Rimaniamo sulla stessa domanda.")
                else:
                    counter += 1
                    logger.debug(f"Input navigazione sconosciuto: {azione}, prossima domanda")
                    print(">>> Passiamo alla domanda successiva...")

            except KeyboardInterrupt:
                logger.warning("Quiz interrotto dall'utente (Ctrl+C)")
                print("\n>>> Quiz interrotto dall'utente")
                return
            except Exception as e:
                logger.error(f"Errore nella elaborazione domanda {counter}: {e}")
                print(f">>> ERRORE: Problema nell'elaborazione. {e}")
                counter += 1
                continue

        # Calcolo e visualizzazione risultati
        try:
            punteggio = calcola_punteggio(domande, risposte)
            mostra_risultati_finali(risposte, punteggio, totale)
            logger.info(f"Quiz completato con successo: {punteggio}/{totale}")
        except Exception as e:
            logger.error(f"Errore nel calcolo risultati: {e}")
            print(">>> ERRORE: Impossibile calcolare i risultati finali")
            return

        print("\n>>> Fine del quiz. Grazie per aver partecipato!")
        logger.info("Quiz terminato normalmente")

    except KeyboardInterrupt:
        logger.warning("Interruzione forzata (Ctrl+C)")
        print("\n>>> Quiz interrotto.")
    except Exception as e:
        logger.critical(f"Errore critico nel main: {e}", exc_info=True)
        print(f">>> ERRORE CRITICO: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
