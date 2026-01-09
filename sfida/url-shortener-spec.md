# URL Shortener CLI - Appunti

## Cosa vogliamo fare

- Un'app da terminale per accorciare URL, in Python
- Usiamo l'API gratuita di is.gd (no autenticazione richiesta)
- I dati li salviamo in `db.json` nella stessa cartella dello script
- Opzionale: usiamo Gemini per generare descrizioni dei link

## API da usare

- **is.gd** — servizio di URL shortening gratuito, no API key
  - Endpoint: `https://is.gd/create.php?format=json&url=URL_DA_ACCORCIARE`
  - Risposta: `{"shorturl": "https://is.gd/abc123"}`
- **Gemini** — per generare titoli/descrizioni automatiche dei link (opzionale)
- **GitHub Gist** — per backup cloud della lista link (opzionale)

## Concetti principali

- **Link** — un URL originale con il suo corrispondente URL accorciato
- **Alias** — nome personalizzato opzionale per ricordare un link (es: "portfolio", "cv")
- **Categoria** — gruppo opzionale per organizzare i link (es: "lavoro", "social", "tools")

## Cosa deve fare

### Link
- accorciare un URL nuovo
- accorciare con alias personalizzato
- vedere tutti i link salvati
- cercare link per alias o URL originale
- copiare un link corto (stamparlo per copia manuale)
- cancellare un link dallo storico

### Categorie (opzionale)
- creare una categoria
- assegnare categoria a un link
- filtrare link per categoria
- vedere tutte le categorie

### Statistiche
- contare totale link creati
- mostrare ultimi N link creati
- link più recente

## Struttura dati

```json
{
  "links": [
    {
      "id": "uuid",
      "original_url": "https://www.example.com/very/long/url",
      "short_url": "https://is.gd/abc123",
      "alias": "portfolio",
      "category": "lavoro",
      "description": "Il mio sito portfolio",
      "created_at": "2025-01-09T10:30:00"
    }
  ],
  "categories": ["lavoro", "social", "tools"]
}
```

## Note

- Se `db.json` non esiste, crearlo vuoto al primo avvio
- Validare che l'URL sia un URL valido prima di chiamare l'API
- Gestire errori di rete (API non raggiungibile)
- Gestire errori dell'API (URL non valido, etc.)
- Output leggibile con emoji (✂️ per short, 🔗 per link, etc.)
- Messaggi chiari per errori (URL non valido, link non trovato, etc.)