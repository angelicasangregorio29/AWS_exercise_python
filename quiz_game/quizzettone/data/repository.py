import os
import json
import logging
from typing import List, Dict

logger = logging.getLogger(__name__)

def _resolve_path(path: str) -> str:
    """Rende il percorso relativo al package quizzettone."""
    base_dir = os.path.dirname(os.path.dirname(__file__))  # .../quizzettone
    return os.path.join(base_dir, path)

def carica_domande_txt(path: str = "domande.txt") -> List[Dict]:
    """Carica domande da file di testo (formato blocchi)."""
    full_path = _resolve_path(path)
    
    try:
        if not os.path.exists(full_path):
            logger.error(f"File non trovato: {full_path}")
            raise FileNotFoundError(f"File non trovato: {full_path}")
        
        if not os.path.isfile(full_path):
            logger.error(f"Il percorso non è un file: {full_path}")
            raise IOError(f"Il percorso non è un file: {full_path}")
        
        domande: List[Dict] = []
        with open(full_path, "r", encoding="utf-8") as f:
            buffer: List[str] = []
            for line_num, line in enumerate(f, 1):
                line = line.rstrip("\n")
                if line.strip() == "":
                    if buffer:
                        try:
                            domanda = _parse_block(buffer, line_num)
                            domande.append(domanda)
                        except ValueError as e:
                            logger.warning(f"Errore parsing blocco: {e}")
                            raise
                        buffer = []
                else:
                    buffer.append(line)
            if buffer:
                try:
                    domanda = _parse_block(buffer, line_num)
                    domande.append(domanda)
                except ValueError as e:
                    logger.warning(f"Errore parsing ultimo blocco: {e}")
                    raise
        
        if not domande:
            logger.warning(f"Nessuna domanda caricata da {full_path}")
            raise ValueError(f"File {full_path} non contiene domande valide")
        
        logger.info(f"Caricate {len(domande)} domande da {full_path}")
        return domande
        
    except FileNotFoundError as e:
        logger.error(f"FileNotFoundError: {e}")
        raise
    except IOError as e:
        logger.error(f"IOError durante lettura file: {e}")
        raise
    except Exception as e:
        logger.error(f"Errore inaspettato nel caricamento file: {e}")
        raise

def _parse_block(block: List[str], line_num: int = 0) -> Dict:
    """Parsa un blocco di domanda con validazione."""
    try:
        if len(block) < 6:
            raise ValueError(f"Blocco domanda incompleto (riga {line_num}): {len(block)} righe, attese 6")
        
        question = block[0][2:].strip() if len(block[0]) > 2 else ""
        if not question:
            raise ValueError(f"Domanda vuota (riga {line_num})")
        
        options = []
        for i in range(1, 5):
            if len(block[i]) <= 3:
                raise ValueError(f"Opzione {i} non valida (riga {line_num}): '{block[i]}'")
            options.append(block[i][3:].strip())
        
        if any(not opt for opt in options):
            raise ValueError(f"Opzioni vuote rilevate (riga {line_num})")
        
        try:
            correct = int(block[5].split(":")[1].strip())
        except (ValueError, IndexError) as e:
            raise ValueError(f"Numero risposta corretta non valido (riga {line_num}): {e}")
        
        if correct not in (1, 2, 3, 4):
            raise ValueError(f"Risposta corretta deve essere 1-4, trovato {correct} (riga {line_num})")
        
        return {"question": question, "options": options, "correct": correct}
        
    except ValueError as e:
        logger.error(f"Errore parsing blocco: {e}")
        raise

def carica_domande_json(path: str = "domande.json") -> List[Dict]:
    """Carica domande da file JSON (lista di dict)."""
    full_path = _resolve_path(path)
    
    try:
        if not os.path.exists(full_path):
            logger.error(f"File non trovato: {full_path}")
            raise FileNotFoundError(f"File non trovato: {full_path}")
        
        if not os.path.isfile(full_path):
            logger.error(f"Il percorso non è un file: {full_path}")
            raise IOError(f"Il percorso non è un file: {full_path}")
        
        with open(full_path, "r", encoding="utf-8") as f:
            try:
                domande = json.load(f)
            except json.JSONDecodeError as e:
                logger.error(f"Errore JSON non valido: {e}")
                raise ValueError(f"File JSON non valido: {e}")
        
        if not isinstance(domande, list):
            logger.error(f"File JSON non contiene una lista")
            raise ValueError("File JSON deve contenere una lista di domande")
        
        if not domande:
            logger.warning(f"File JSON vuoto: {full_path}")
            raise ValueError(f"File {full_path} non contiene domande")
        
        # Validazione domande
        for idx, d in enumerate(domande):
            try:
                if not isinstance(d, dict):
                    raise ValueError(f"Elemento {idx} non è un dict")
                if not all(k in d for k in ("question", "options", "correct")):
                    raise ValueError(f"Elemento {idx} manca campi obbligatori")
                if not isinstance(d.get("options"), list) or len(d["options"]) != 4:
                    raise ValueError(f"Elemento {idx}: 'options' deve essere lista di 4 elementi")
                if d["correct"] not in (1, 2, 3, 4):
                    raise ValueError(f"Elemento {idx}: 'correct' deve essere 1-4")
            except ValueError as e:
                logger.error(f"Domanda JSON non valida (idx {idx}): {e}")
                raise
        
        logger.info(f"Caricate {len(domande)} domande da {full_path}")
        return domande
        
    except FileNotFoundError as e:
        logger.error(f"FileNotFoundError: {e}")
        raise
    except IOError as e:
        logger.error(f"IOError durante lettura file: {e}")
        raise
    except Exception as e:
        logger.error(f"Errore inaspettato nel caricamento JSON: {e}")
        raise

def carica_domande(path: str) -> List[Dict]:
    """Carica domande scegliendo il formato in base all'estensione."""
    try:
        if not path:
            raise ValueError("Percorso file vuoto")
        
        if path.endswith(".txt"):
            return carica_domande_txt(path)
        elif path.endswith(".json"):
            return carica_domande_json(path)
        else:
            logger.error(f"Formato non supportato: {path}")
            raise ValueError("Formato non supportato. Usa .txt o .json")
    except Exception as e:
        logger.error(f"Errore nel caricamento domande: {e}")
        raise
