def conta_caratteri(testo: str) -> int:
    """Restituisce il numero totale di caratteri (spazi inclusi)."""
    return len(testo)


def frequenza_caratteri(testo: str) -> dict[str, int]:
    """Restituisce un dizionario con la frequenza di ogni carattere."""
    freq = {}
    for char in testo:
        freq[char] = freq.get(char, 0) + 1
    return freq


def leggi_file(percorso: str) -> str:
    """Legge un file e restituisce il contenuto come stringa."""
    try:
        with open(percorso, 'r', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        print(f"Errore: il file '{percorso}' non esiste.")
        return ""