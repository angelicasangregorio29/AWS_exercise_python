import sys
import logging
from pathlib import Path
import argparse

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

def main(format_pref: str = "auto", all_txt: bool = False, dir_path: str | None = None):
    """Main function per il quiz con gestione eccezioni robusta."""
    try:
        logger.info(">>> Avvio del quiz...\n")
        print(">>> Avvio del quiz...\n")

        # Gestione formato: 'txt', 'json', 'auto'
        domande = []
        try:
            if format_pref == "txt":
                if all_txt:
                    # Carica tutte le domande da tutti i .txt nella directory specificata o nel package
                    from .data.repository import carica_domande_from_dir
                    domande = carica_domande_from_dir(dir_path or "")
                else:
                    # se è stata passata una directory, usiamo il file domande.txt dentro quella directory
                    if dir_path:
                        import os as _os
                        domande = carica_domande(_os.path.join(dir_path, "domande.txt"))
                    else:
                        domande = carica_domande("domande.txt")
                logger.info("Caricate domande in modalità TXT")
            elif format_pref == "json":
                if dir_path:
                    import os as _os
                    domande = carica_domande(_os.path.join(dir_path, "domande.json"))
                else:
                    domande = carica_domande("domande.json")
                logger.info("Caricate domande in modalità JSON")
            else:  # auto
                if all_txt:
                    from .data.repository import carica_domande_from_dir
                    try:
                        domande = carica_domande_from_dir(dir_path or "")
                        logger.info("Caricate domande da tutti i .txt (auto+all)")
                    except Exception:
                        logger.info("Nessun .txt valido; provo domande.json")
                        if dir_path:
                            import os as _os
                            domande = carica_domande(_os.path.join(dir_path, "domande.json"))
                        else:
                            domande = carica_domande("domande.json")
                else:
                    # preferenza: domande.txt -> domande.json
                    try:
                        if dir_path:
                            import os as _os
                            domande = carica_domande(_os.path.join(dir_path, "domande.txt"))
                        else:
                            domande = carica_domande("domande.txt")
                        logger.info("Caricate domande da domande.txt")
                    except Exception:
                        logger.info("domande.txt non utilizzabile; provo domande.json")
                        if dir_path:
                            import os as _os
                            domande = carica_domande(_os.path.join(dir_path, "domande.json"))
                        else:
                            domande = carica_domande("domande.json")
        except FileNotFoundError as e:
            logger.error(f"Nessun file domande trovato: {e}")
            print(">>> ERRORE: Nessun file domande valido trovato.")
            return
        except ValueError as e:
            logger.error(f"File domande non valido: {e}")
            print(f">>> ERRORE: {e}")
            return
        except Exception as e:
            logger.error(f"Errore inaspettato nel caricamento domande: {e}")
            print(">>> ERRORE: Impossibile caricare le domande. Controlla i file.")
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
    parser = argparse.ArgumentParser(description="Avvia il quizzettone")
    parser.add_argument("--format", choices=("txt", "json", "auto"), default="auto",
                        help="Seleziona formato domande: 'txt', 'json' o 'auto' (default)")
    parser.add_argument("--all-txt", action="store_true",
                        help="Se True, carica tutte le domande da tutti i file .txt nella cartella del package")
    parser.add_argument("--dir", dest="dir", default=None,
                        help="Directory da cui caricare i file domande (default: package quizzettone)")
    args = parser.parse_args()
    main(format_pref=args.format, all_txt=args.all_txt, dir_path=args.dir)
