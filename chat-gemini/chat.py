import google.generativeai as genai
import os
import sys

# --- CONFIGURAZIONE ---
# Incolla qui sotto la tua API KEY tra le virgolette
API_KEY = "INCOLLA_QUI_LA_TUA_API_KEY_COPIATA_PRIMA"

def main():
    # 1. Configura la chiave API
    if API_KEY == "INCOLLA_QUI_LA_TUA_API_KEY_COPIATA_PRIMA":
        print("ERRORE: Devi inserire la tua API Key nel file chat.py!")
        return

    genai.configure(api_key=API_KEY)

    # 2. Seleziona il modello (gemini-1.5-flash è veloce ed economico/gratis)
    try:
        model = genai.GenerativeModel('gemini-1.5-flash')
    except Exception as e:
        print(f"Errore nella connessione: {e}")
        return

    # 3. Avvia la chat (history=[] permette di ricordare i messaggi precedenti)
    chat = model.start_chat(history=[])

    print("\n" + "="*40)
    print("🤖 CHAT CON GEMINI (Terminale)")
    print("Scrivi 'esci' per chiudere il programma.")
    print("="*40 + "\n")

    # 4. Ciclo infinito per inviare messaggi
    while True:
        try:
            # Prende l'input dell'utente
            user_input = input("Tu: ")
            
            # Controlla se l'utente vuole uscire
            if user_input.lower() in ['esci', 'exit', 'quit']:
                print("👋 Ciao!")
                break
            
            if not user_input.strip():
                continue

            print("Gemini: ", end="", flush=True)

            # 5. Invia il messaggio e ricevi la risposta (in streaming per effetto 'scritura')
            response = chat.send_message(user_input, stream=True)
            
            for chunk in response:
                print(chunk.text, end="", flush=True)
            
            print("\n") # Nuova riga alla fine della risposta

        except KeyboardInterrupt:
            # Gestisce CTRL+C per uscire
            print("\n👋 Uscita forzata.")
            break
        except Exception as e:
            print(f"\n❌ Errore: {e}")

if __name__ == "__main__":
    main()