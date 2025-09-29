from colorama import init, Fore, Style
from datetime import datetime

# Inicializa colorama
init(autoreset=True)

TIPO_CORES = {
    "INF": Fore.CYAN,
    "ASK": Fore.YELLOW,
    "WRN": Fore.MAGENTA,
    "ERR": Fore.RED
}

def timestamp() -> str:
    return datetime.now().strftime("%H:%M:%S")

def log(message: str, tipo: str = "INF"):
    cor = TIPO_CORES.get(tipo, Fore.LIGHTBLACK_EX)
    print(f"{Fore.LIGHTBLACK_EX}[{timestamp()}] {cor}[{tipo}]{Style.RESET_ALL} {message}")

def info(message: str):
    log(message, "INF")

def warn(message: str):
    log(message, "WRN")

def error(message: str):
    log(message, "ERR")

def ask(message: str) -> str:
    return input(f"{Fore.LIGHTBLACK_EX}[{timestamp()}] {Fore.YELLOW}[ASK]{Style.RESET_ALL} {message}")
