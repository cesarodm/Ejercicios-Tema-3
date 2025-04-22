import questionary
from utils import crear_polinomio, mostrar_resultado
from operaciones import restar_polinomios, dividir_polinomios
from polinomio import Polinomio

def iniciar_menu():
    print("\nBienvenido al grimorio de los polinomios encantados.")

    pol1 = crear_polinomio("primer")
    pol2 = crear_polinomio("segundo")

    while True:
        opcion = questionary.select(
            "Selecciona una operación mágica:",
            choices=[
                "1. Restar los polinomios",
                "2. Dividir los polinomios",
                "3. Eliminar un término del primer polinomio",
                "4. Verificar si un término existe en el primer polinomio",
                "5. Mostrar polinomios actuales",
                "6. Salir"
            ]
        ).ask()

        if opcion.startswith("1"):
            resultado = restar_polinomios(pol1, pol2)
            mostrar_resultado(resultado, "Resultado de la resta")

        elif opcion.startswith("2"):
            resultado = dividir_polinomios(pol1, pol2)
            mostrar_resultado(resultado, "Resultado de la división")

        elif opcion.startswith("3"):
            exp = int(input("Introduce el exponente a eliminar: "))
            pol1.eliminar_termino(exp)
            print("Término eliminado.")

        elif opcion.startswith("4"):
            exp = int(input("Introduce el exponente a buscar: "))
            existe = pol1.existe_termino(exp)
            print("El término existe." if existe else "El término no existe.")

        elif opcion.startswith("5"):
            print("Primer polinomio:", pol1)
            print("Segundo polinomio:", pol2)

        elif opcion.startswith("6"):
            print("Hasta la próxima, hechicero.")
            break
