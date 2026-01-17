# URL Shortener CLI (DB locale)

Tool **da terminale** in Python per accorciare URL tramite l’API di **is.gd** e salvare tutto in un piccolo database locale (`db.json`).  
Include: lista link, ricerca, eliminazione, categorie e statistiche.

---

## Funzionalità

- ✂️ **Accorcia URL** (con o senza alias personalizzato)
- 💾 **Salvataggio persistente** in `db.json`
- 📋 **Lista link** in tabella
- 🔍 **Ricerca** per alias o URL originale
- 🗑️ **Eliminazione** tramite alias o short URL
- 📂 **Gestione categorie** (lista / aggiunta)
- 📊 **Statistiche** (totale + ultimo creato)

---

## Requisiti

- Python **3.9+** (consigliato)
- Dipendenza: `requests`

Installazione:

```bash
pip install requests
```

---

## Avvio

Esegui lo script:

```bash
python shortner_url.py
```

Si aprirà un menu interattivo:

- 1 ✂️ Accorcia URL  
- 2 📋 Lista Link  
- 3 🔍 Cerca Link  
- 4 🗑️ Elimina Link  
- 5 📂 Categorie  
- 6 📊 Statistiche  
- 0 🚪 Esci  

> Nota: questa versione funziona **solo** in modalità interattiva (niente argomenti da riga di comando).

---

## Struttura progetto

Esempio:

```
project/
│─ main.py
│─ db.json        # creato automaticamente se non esiste
│─ README.md
```

Il database viene salvato nella stessa cartella dello script:
- `db.json` contiene `links` e `categories`
- se `db.json` non esiste o è corrotto, lo script crea una struttura vuota di default

Esempio di `db.json`:

```json
{
  "links": [],
  "categories": ["lavoro", "social", "tools"]
}
```

---

## Dati salvati per ogni link

Quando crei un link, viene aggiunto un record con questi campi:

- `id`: UUID univoco
- `original_url`: URL lungo originale
- `short_url`: URL accorciato restituito da is.gd
- `alias`: alias scelto oppure quello generato (ultima parte dello short URL)
- `category`: categoria associata
- `created_at`: data/ora in formato ISO (es. `2026-01-09T12:34:56.123456`)

---

## Alias personalizzati (come funzionano)

Se scegli un alias personalizzato:

- deve essere **alfanumerico** (consigliato)
- consigliati **4–10 caratteri**
- può fallire se:
  - è già stato usato su is.gd
  - non rispetta le regole del servizio

Se l’API restituisce un errore specifico per alias, il programma stampa:

- `❌ Alias '<alias>' non disponibile o non valido.`

Esempi consigliati:
- `lab2026`
- `spot467`
- `tools258`

---

## Note sul comportamento

- Se inserisci un URL senza `http://` o `https://`, lo script aggiunge automaticamente `https://`
- Nella **lista link**, l’URL originale viene troncato a schermo se troppo lungo (solo per visualizzazione)
- Le categorie vengono salvate e restano disponibili nei successivi avvii

---

## Dipendenze e rete

Questo progetto usa l’API pubblica di **is.gd**:
- serve connessione a Internet
- in caso di problemi di rete, verrà mostrato un errore del tipo: `❌ Errore di connessione: ...`

---