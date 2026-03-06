from rich.console import Console
from rich.prompt import Prompt

console = Console()

console.print("[bold green]Super Kalkulator 3000[/bold green] 🚀")

while True:
    dzialanie = Prompt.ask("Co chcesz zrobić", choices=["+", "-", "*", "/", "q"])
    if dzialanie == "q":
        break
    a = float(Prompt.ask("Liczba 1"))
    b = float(Prompt.ask("Liczba 2"))
    
    if dzialanie == "+":  wynik = a + b
    elif dzialanie == "-": wynik = a - b
    elif dzialanie == "*": wynik = a * b
    elif dzialanie == "/": wynik = a / b if b != 0 else "Nie dziel przez zero!"
    
    console.print(f"[bold yellow]Wynik:[/bold yellow] {wynik}")