import os
from typing import List, Dict

def _resolve_path(path: str) -> str:
    """Rende il percorso relativo al package quizzettone."""
    base_dir = os.path.dirname(os.path.dirname(__file__))  # .../quizzettone
    return os.path.join(base_dir, path)

def carica_domande(path: str = "domande.txt") -> List[Dict]:
    """
    Carica le domande da un file di testo.
    Formato suggerito per ogni domanda (blocco di 6 righe):
      Q: Qual è la capitale della Francia?
      1) Parigi
      2) Londra
      3) Roma
      4) Madrid
      CORRECT: 1
    Blocchi separati da una riga vuota.
    """
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

        # ultimo blocco se il file non termina con newline
        if buffer:
            domanda = _parse_block(buffer)
            domande.append(domanda)

    return domande

def _parse_block(block: List[str]) -> Dict:
    """
    Converte un blocco di righe in un dizionario domanda.
    Richiede:
      Q: ...
      1) ...
      2) ...
      3) ...
      4) ...
      CORRECT: n
    """
    if len(block) < 6:
        raise ValueError(f"Blocco domanda incompleto: {block}")

    q_line = block[0]
    if not q_line.startswith("Q:"):
        raise ValueError(f"Prima riga non valida (deve iniziare con 'Q:'): {q_line}")

    question = q_line[2:].strip()
    options = [block[i][3:].strip() if block[i][:2].isdigit() else block[i].strip() for i in range(1, 5)]

    correct_line = block[5]
    if not correct_line.startswith("CORRECT:"):
        raise ValueError(f"Riga CORRECT non valida: {correct_line}")

    try:
        correct = int(correct_line.split(":", 1)[1].strip())
    except ValueError:
        raise ValueError(f"Indice CORRECT non numerico: {correct_line}")

    if correct not in {1, 2, 3, 4}:
        raise ValueError(f"Indice CORRECT fuori range (1-4): {correct}")

    return {
        "question": question,
        "options": options,     # lista di 4 stringhe
        "correct": correct      # int 1-4
    }