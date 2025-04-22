import questionary
from matriz import Matriz
from determinante import determinante_recursivo, determinante_sarrus
from utils import pedir_matriz, mostrar_resultado

def iniciar_menu():
    print("\n🔐 Bienvenido al Secreto de la Cifra Mágica 🔐")

    matriz = pedir_matriz()

    while True:
        opcion = questionary.select(
            "¿Qué método deseas usar para calcular el determinante?",
            choices=[
                "📐 Método recursivo (expansión por cofactores)",
                "📏 Método iterativo (regla de Sarrus)",
                "🔁 Introducir nueva matriz",
                "❌ Salir"
            ]
        ).ask()

        if opcion.startswith("📐"):
            resultado = determinante_recursivo(matriz.datos)
            mostrar_resultado(resultado, "recursivo")

        elif opcion.startswith("📏"):
            resultado = determinante_sarrus(matriz.datos)
            mostrar_resultado(resultado, "iterativo")

        elif opcion.startswith("🔁"):
            matriz = pedir_matriz()

        elif opcion.startswith("❌"):
            print("👋 Gracias por participar en esta búsqueda mágica.")
            break
