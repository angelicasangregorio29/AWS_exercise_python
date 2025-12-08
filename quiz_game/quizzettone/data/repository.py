import os
import json
from typing import List, Dict

def _resolve_path(path: str) -> str:
    """Rende il percorso relativo al package quizzettone."""
    base_dir = os.path.dirname(os.path.dirname(__file__))  # .../quizzettone
    return os.path.join(base_dir, path)

def carica_domande_txt(path: str = "domande.txt") -> List[Dict]:
    """Carica domande da file di testo (formato blocchi)."""
    full_path = _resolve_path(path)
    if not os.path.exists(full_path):
        raise FileNotFoundError(f"File non trovato: {full_path}")

    domande: List[Dict] = []
    with open(full_path, "r", encoding="utf-8") as f:
        buffer: List[str] = []
        for line in f:
            line = line.rstrip("\n")
            if line.strip() == "":
                if buffer:
                    domanda = _parse_block(buffer)
                    domande.append(domanda)
                    buffer = []
            else:
                buffer.append(line)
        if buffer:
            domanda = _parse_block(buffer)
            domande.append(domanda)
    return domande

def _parse_block(block: List[str]) -> Dict:
    if len(block) < 6:
        raise ValueError(f"Blocco domanda incompleto: {block}")
    question = block[0][2:].strip()  # riga "Q: ..."
    options = [block[i][3:].strip() for i in range(1, 5)]
    correct = int(block[5].split(":")[1].strip())
    return {"question": question, "options": options, "correct": correct}

def carica_domande_json(path: str = "domande.json") -> List[Dict]:
    """Carica domande da file JSON (lista di dict)."""
    full_path = _resolve_path(path)
    if not os.path.exists(full_path):
        raise FileNotFoundError(f"File non trovato: {full_path}")

    with open(full_path, "r", encoding="utf-8") as f:
        domande = json.load(f)

    # Validazione minima
    for d in domande:
        if not all(k in d for k in ("question", "options", "correct")):
            raise ValueError(f"Domanda JSON non valida: {d}")
    return domande

def carica_domande(path: str) -> List[Dict]:
    """Carica domande scegliendo il formato in base all'estensione."""
    if path.endswith(".txt"):
        return carica_domande_txt(path)
    elif path.endswith(".json"):
        return carica_domande_json(path)
    else:
        raise ValueError("Formato non supportato. Usa .txt o .json")