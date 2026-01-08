# Todo List CLI - Appunti

## Cosa vogliamo fare

- Un'app todo list da terminale, in Python
- Niente dipendenze esterne, solo libreria standard
- I dati li salviamo in un file JSON

## Concetti principali

- **Progetti** — contenitori di task (es: "Sito Web", "App Mobile")
- **Task** — le cose da fare, appartengono a un progetto
- **Tag** — etichette trasversali da attaccare ai task (es: #urgent, #bug, #idea)

## Cosa deve fare

### Progetti
- creare un progetto (nome + descrizione opzionale)
- vedere tutti i progetti
- cancellare un progetto (e i suoi task)

### Task
- aggiungere task a un progetto
- segnare come completato / riaprire
- assegnare uno o più tag
- vedere task di un progetto o tutti
- filtrare per tag
- cancellare task

### Tag
- creare tag (nome + colore opzionale)
- vedere tutti i tag
- cancellare tag (lo toglie dai task che ce l'hanno)

## Struttura dati

Progetti, task e tag hanno ciascuno un ID univoco (uuid).

Progetto ha: nome (univoco), descrizione, data creazione.

Task ha: titolo (univoco), completato sì/no, riferimento al progetto, lista di tag, date di creazione/completamento.

Tag ha: nome (univoco), colore.

## Note

- Se il file JSON non esiste, crearlo vuoto al primo avvio
- Output leggibile con emoji/simboli per stato task
- Messaggi chiari per errori (progetto non trovato, tag già esistente, ecc.)