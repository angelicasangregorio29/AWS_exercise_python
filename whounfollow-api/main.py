from console import print_menu
from service import get_followers, get_statistiche, get_statistiche

def main() -> None:

    while True:
        print_menu()

        option = input("Seleziona l'operazione che vuoi eseguire:")
        
        match option:
            case "1":
                get_followers()
            case "2":
                get_statistiche()
            case "3":
                print("Hai scelto i dati di un giorno specifico!")
            case "exit":
                print("Perfetto, programma terminato, grazie mille!")
                break
            case _:
                print("Inserisci un'opzione valida!")

if __name__ == "__main__":
    main()