import questionary
from juego import JuegoPiramide

def iniciar_menu():
    while True:
        print("\n🔺 Bienvenido al Puzzle de la Pirámide de Piedras Preciosas 🔺")

        opcion = questionary.select(
            "¿Qué quieres hacer?",
            choices=[
                "🧠 Resolver automáticamente el puzzle",
                "🔢 Cambiar número de piedras",
                "❌ Salir del juego"
            ]
        ).ask()

        if opcion == "🧠 Resolver automáticamente el puzzle":
            juego = JuegoPiramide()
            juego.iniciar()

        elif opcion == "🔢 Cambiar número de piedras":
            cantidad = questionary.text("Introduce el número de piedras (≥1):").ask()
            if cantidad.isdigit() and int(cantidad) > 0:
                juego = JuegoPiramide(int(cantidad))
                juego.iniciar()
            else:
                print("⚠️ Entrada no válida. Inténtalo con un número mayor a 0.")

        elif opcion == "❌ Salir del juego":
            print("👋 ¡Hasta la próxima, explorador del Nilo!")
            break

