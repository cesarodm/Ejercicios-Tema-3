import questionary
from matriz import Matriz
from utils import pedir_matriz
from determinante import determinante_recursivo, determinante_sarrus

def iniciar_menu():
    print("\n📘 Bienvenido al Secreto de la Cifra Mágica")

    matriz_3x3 = pedir_matriz()

    opcion = questionary.select(
        "¿Qué método deseas usar para calcular el determinante?",
        choices=[
            "📐 Método recursivo (cofactores)",
            "📏 Método iterativo (regla de Sarrus)",
            "❌ Salir"
        ]
    ).ask()

    if opcion.startswith("📐"):
        resultado = determinante_recursivo(matriz_3x3.datos)
        print(f"\n🔢 Determinante (recursivo): {resultado}")

    elif opcion.startswith("📏"):
        resultado = determinante_sarrus(matriz_3x3.datos)
        print(f"\n🔢 Determinante (iterativo): {resultado}")

    elif opcion.startswith("❌"):
        print("👋 ¡Hasta la próxima, matemático aventurero!")
