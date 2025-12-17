"""

"""

from requests import get
import re

BASE_URL: str = "https://github.com/emanuelegurini" 
END_URL: str = "tab=followers"

PATTERN = r'<a\s+[^>]*href="https://github\.com/([^/]+)\?page=(\d+)&amp;tab=followers"[^>]*>Next</a>'

def is_next_button_present(text: str) -> bool:
  if not text:
    raise ValueError("La stringa non puo essere vuota!")

  return bool(re.search(PATTERN, text))

def main() -> None:
  print("Start del programma")

  controller: bool = True
  counter: int = 1

  while controller:
    url = f"{BASE_URL}?page={counter}&{END_URL}"
    try:
      response = get(url)

      with open(f"tmp/pagina-{counter}.txt", "w") as f:
        if controller:
          f.write(response.text)
          controller = is_next_button_present(response.text)
          counter = counter + 1 
          print("File salvato")


    except Exception as e:
      print(f"Errore: {e}") 

  print("fine while perché i dati sono stati tutti scaricati")
 
if __name__ == "__main__":
  main()