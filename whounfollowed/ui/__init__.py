class RetroColor:
    CYAN = '\033[96m'
    MAGENTA = '\033[95m'
    YELLOW = '\033[93m'
    GREEN = '\033[92m'
    RESET = '\033[0m'
    BOLD = '\033[1m'

def print_welcome_arcade():
    c = RetroColor # Scorciatoia per leggibilità
    
    # Caratteri per i bordi
    TL = "╔" # Top Left
    TR = "╗" # Top Right
    BL = "╚" # Bottom Left
    BR = "╝" # Bottom Right
    H = "═"  # Horizontal
    V = "║"  # Vertical
    WIDTH = 42

    print("\n")
    # Linea superiore ciano neon
    print(f"{c.CYAN}{TL}{H*WIDTH}{TR}{c.RESET}")
    
    # Corpo centrale con effetto "Scanline" alternato
    print(f"{c.CYAN}{V}{c.RESET}{' '*WIDTH}{c.CYAN}{V}{c.RESET}")
    
    # Testo centrale: Magenta grassetto per il titolo
    title = " W E L C O M E   T O ".center(WIDTH)
    print(f"{c.CYAN}{V}{c.BOLD}{c.MAGENTA}{title}{c.RESET}{c.CYAN}{V}{c.RESET}")
    
    # Nome dell'app: Giallo "Insert Coin" style
    app_name = "WHOUNFOLLOWED".center(WIDTH)
    print(f"{c.CYAN}{V}{c.BOLD}{c.YELLOW}{app_name}{c.RESET}{c.CYAN}{V}{c.RESET}")

    # Linea decorativa "pixel"
    pixel_line = "░▒▓▒░"*8 + "░▒"
    print(f"{c.CYAN}{V}{c.GREEN}{pixel_line.center(WIDTH)}{c.RESET}{c.CYAN}{V}{c.RESET}")
    
    # Linea inferiore
    print(f"{c.CYAN}{BL}{H*WIDTH}{BR}{c.RESET}")
    
    # "Press Start" footer
    print(f"\n{' '*12}{c.BOLD}{c.GREEN}> INSERT COIN TO START <{c.RESET}\n")
    print("")

def print_menu() -> None:
  print("*"*30)
  print("*"*3 + " MENU")
  print("*"*30)

  print(
  """
  Scegli quale operazione effettuare:
  1. Scarica follower
  2. Restituisci statistiche
  3. Guarda i dati di un giorno specifico
  """)