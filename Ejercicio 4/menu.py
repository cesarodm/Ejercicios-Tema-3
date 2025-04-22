import questionary
from rich.console import Console
from rich.panel import Panel
from rich.text import Text

from utils import crear_polinomio, mostrar_resultado
from operaciones import restar_polinomios, dividir_polinomios
from polinomio import Polinomio

console = Console()

def mostrar_titulo():
    console.clear()
    console.rule("[bold blue]📚 La Matemática de los Encantamientos", style="bold purple")
    console.print(Panel.fit("Un grimorio antiguo te reta a manipular polinomios mágicos...\nElige sabiamente tus hechizos.", style="bold green"))

def iniciar_menu():
    mostrar_titulo()

    pol1 = crear_polinomio("primer")
    pol2 = crear_polinomio("segundo")

    while True:
        console.print("\n[bold]📌 Polinomio 1:[/bold]", style="blue")
        console.print(f"[italic cyan]{pol1}[/italic cyan]")
        console.print("[bold]📌 Polinomio 2:[/bold]", style="blue")
        console.print(f"[italic cyan]{pol2}[/italic cyan]")

        opcion = questionary.select(
            "Selecciona un hechizo mágico:",
            choices=[
                "🧮 Restar los polinomios",
                "➗ Dividir los polinomios",
                "❌ Eliminar un término del primer polinomio",
                "🔍 Verificar si un término existe en el primer polinomio",
                "🔄 Reescribir ambos polinomios",
                "📜 Mostrar polinomios actuales",
                "🚪 Salir del grimorio"
            ]
        ).ask()

        if opcion.startswith("🧮"):
            resultado = restar_polinomios(pol1, pol2)
            mostrar_resultado(resultado, "Resultado de la resta")

        elif opcion.startswith("➗"):
            resultado = dividir_polinomios(pol1, pol2)
            mostrar_resultado(resultado, "Resultado de la división")

        elif opcion.startswith("❌"):
            exp = questionary.text("Introduce el exponente del término a eliminar:").ask()
            if exp.isdigit():
                confirm = questionary.confirm(f"¿Eliminar el término x^{exp}?").ask()
                if confirm:
                    pol1.eliminar_termino(int(exp))
                    console.print(f"Término x^{exp} eliminado del primer polinomio.", style="red")
            else:
                console.print("Entrada inválida.", style="bold red")

        elif opcion.startswith("🔍"):
            exp = questionary.text("Introduce el exponente a buscar:").ask()
            if exp.isdigit():
                existe = pol1.existe_termino(int(exp))
                mensaje = f"El término x^{exp} existe." if existe else f"No se encontró x^{exp}."
                console.print(mensaje, style="green" if existe else "yellow")
            else:
                console.print("Entrada inválida.", style="bold red")

        elif opcion.startswith("🔄"):
            pol1 = crear_polinomio("primer")
            pol2 = crear_polinomio("segundo")

        elif opcion.startswith("📜"):
            console.print(f"\n📌 Polinomio 1: [cyan]{pol1}[/cyan]")
            console.print(f"📌 Polinomio 2: [cyan]{pol2}[/cyan]")

        elif opcion.startswith("🚪"):
            confirm = questionary.confirm("¿Seguro que quieres cerrar el grimorio?").ask()
            if confirm:
                console.print("\n[bold green]✨ Has cerrado el grimorio. Hasta la próxima, hechicero.[/bold green]")
                break
