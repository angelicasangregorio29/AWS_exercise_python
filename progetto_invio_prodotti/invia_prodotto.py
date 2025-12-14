import requests

# URL del server (puoi sostituirlo con quello reale)
SERVER_URL = "http://localhost:5000/products"

def get_valid_input(prompt, validation_func, error_message):
    """Richiede input finché non è valido."""
    while True:
        value = input(prompt).strip()
        if validation_func(value):
            return value
        else:
            print(error_message)

def is_valid_title(title):
    return len(title) > 0

def is_valid_price(price):
    try:
        return float(price) > 0
    except ValueError:
        return False

def is_valid_description(description):
    return len(description) > 0

def main():
    print("Inserisci i dati del prodotto:")

    titolo = get_valid_input("Titolo: ", is_valid_title, "⚠️ Il titolo non può essere vuoto.")
    prezzo = get_valid_input("Prezzo: ", is_valid_price, "⚠️ Inserisci un numero valido e maggiore di 0.")
    descrizione = get_valid_input("Descrizione: ", is_valid_description, "⚠️ La descrizione non può essere vuota.")

    prodotto = {
        "title": titolo,
        "price": float(prezzo),
        "description": descrizione,
        "category": "electronics",   # hard-coded
        "image": "https://example.com/product.jpg"  # hard-coded
    }

    print("\n📦 Dati del prodotto pronti per l'invio:")
    print(prodotto)

    try:
        response = requests.post(SERVER_URL, json=prodotto)
        if response.status_code == 200 or response.status_code == 201:
            print("✅ Prodotto inviato con successo!")
            print("Risposta del server:", response.json())
        else:
            print(f"❌ Errore nell'invio. Codice: {response.status_code}")
            print("Dettagli:", response.text)
    except Exception as e:
        print("❌ Errore di connessione al server:", e)

if __name__ == "__main__":
    main()