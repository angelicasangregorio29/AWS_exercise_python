1. Obiettivo del Progetto

Creare uno script Python automatizzato per monitorare i follower di GitHub su base giornaliera.

Funzionalità principale: Confrontare la lista attuale con quella del giorno precedente.

Output desiderato: Identificare chi ha iniziato a seguirti (Nuovi Follower) e chi ha smesso (Unfollow).

2. Analisi Tecnica della Pagina

A. Struttura degli URL e Paginazione

La lista dei follower non è caricata in un'unica pagina, ma è distribuita su più pagine.

Pattern URL Base: https://github.com/username?tab=followers

Pattern Paginazione: https://github.com/username?page=X&tab=followers (dove X è il numero della pagina).

B. Elementi HTML da Intercettare (Parsing)

Per estrarre i dati è necessario identificare specifici tag HTML nel DOM:

Il Bottone "Next" (Navigazione): Serve per capire se esistono altre pagine da visitare.

Target: Cerca un tag <a> con testo "Next" o attributi specifici.

Esempio HTML:

HTML
<a rel="nofollow" href="https://github.com/username?page=2&amp;tab=followers">Next</a>
Il Profilo Utente (Estrazione Dati): Serve per salvare il nome utente del follower.

Target: Cerca il tag <a> che contiene il link al profilo (spesso dentro una hovercard).

Esempio HTML:

HTML
<a class="d-inline-block no-underline mb-1" href="/NomeUtente" ... >
3. Flusso Logico dell'Algoritmo (Workflow)

Il programma deve seguire questo ciclo di esecuzione:

Inizializzazione:

Definire l'URL di partenza (Pagina 1).

Preparare una lista vuota per raccogliere i follower correnti.

Ciclo di Scraping (Loop):

Scarica: Ottieni il contenuto HTML della pagina corrente.

Estrai Follower: Trova tutti gli elementi utente nella pagina e aggiungili alla lista.

Verifica Paginazione: Controlla se esiste il bottone "Next".

Se esiste: Estrai il nuovo URL dal bottone "Next" e ripeti il ciclo.

Se NON esiste: Il ciclo termina (siamo all'ultima pagina).

Gestione dei Dati (Storage):

Salvare la lista completa (nomi e numero totale).

Destinazione: File locale (es. JSON/CSV) o Foglio di calcolo (Spreadsheet).

4. Logica delle Statistiche (Confronto)

Per ottenere le statistiche giornaliere, il programma deve leggere il file salvato l'ultima volta che è stato eseguito ("Stato Precedente").

Input:

Lista A (Appena scaricata oggi).

Lista B (Salvata ieri).

Calcolo Differenze:

Nuovi Follower: Presenti in A ma non in B.

Unfollowed: Presenti in B ma non in A.