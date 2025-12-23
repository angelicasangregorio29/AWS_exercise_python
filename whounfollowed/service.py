"""Logica di business principale"""

import datetime
import uuid

from github_client import (
    is_valid_username_format,
    check_user_exists,
    fetch_followers_page,
    has_next_page
)
from file_manager import (
    ensure_tmp_dir_exists,
    clear_tmp_dir,
    save_page,
    extract_all_usernames
)
from data.repository import save_json_db
from config import DB_PATH


def prompt_for_valid_username() -> str | None:
    """Chiede username finché non è valido o l'utente esce"""
    while True:
        username = input("Inserisci lo username GitHub: ").strip()

        if username.lower() == "exit":
            return None

        if not is_valid_username_format(username):
            print("Formato non valido. Usa solo lettere, numeri e trattini.")
            continue

        if not check_user_exists(username):
            print("Profilo non trovato su GitHub.")
            continue

        print(f"Profilo {username} trovato!")
        return username


def scrape_all_followers_pages(username: str) -> int:
    """Scarica tutte le pagine di follower, restituisce il numero di pagine"""
    ensure_tmp_dir_exists()
    page = 1

    while True:
        print(f"Scarico pagina {page}...")
        html = fetch_followers_page(username, page)
        save_page(page, html)

        if not has_next_page(html):
            break
        page += 1

    return page


def create_record(usernames: list[str]) -> dict:
    """Crea l'oggetto record da salvare nel db"""
    now_utc = datetime.datetime.now(datetime.timezone.utc)
    clean_date = now_utc.isoformat(timespec='milliseconds').replace('+00:00', 'Z')

    return {
        'id': str(uuid.uuid4()),
        'createdAt': clean_date,
        'users': usernames,
        'numberOfUsers': len(usernames)
    }


def get_followers() -> None:
    """Funzione principale: orchestra tutto il processo"""
    username = prompt_for_valid_username()

    if username is None:
        print("Operazione annullata.")
        return

    page_count = scrape_all_followers_pages(username)
    usernames = extract_all_usernames(page_count)

    record = create_record(usernames)
    save_json_db(DB_PATH, record)

    clear_tmp_dir()
    print(f"Salvati {len(usernames)} follower nel database!")