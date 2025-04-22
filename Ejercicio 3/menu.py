import questionary
from flota import Flota
from datos_prueba import cargar_naves

def iniciar_menu():
    flota = Flota(cargar_naves())

    while True:
        opcion = questionary.select(
            "¿Qué deseas hacer?",
            choices=[
                "1. Ordenar por nombre (ascendente)",
                "2. Ordenar por longitud (descendente)",
                "3. Mostrar 'Cometa Veloz' y 'Titán del Cosmos'",
                "4. Mostrar las 5 naves con más pasajeros",
                "5. Mostrar la nave con más tripulación",
                "6. Mostrar las naves que comienzan con 'GX'",
                "7. Mostrar las naves con ≥ 6 pasajeros",
                "8. Mostrar la nave más pequeña y la más grande",
                "9. Salir"
            ]
        ).ask()

        if opcion.startswith("1"):
            flota.ordenar_por_nombre()
        elif opcion.startswith("2"):
            flota.ordenar_por_longitud()
        elif opcion.startswith("3"):
            flota.mostrar_naves_especificas(["Cometa Veloz", "Titán del Cosmos"])
        elif opcion.startswith("4"):
            flota.top_pasajeros(5)
        elif opcion.startswith("5"):
            flota.nave_max_tripulacion()
        elif opcion.startswith("6"):
            flota.naves_con_prefijo("GX")
        elif opcion.startswith("7"):
            flota.naves_min_pasajeros(6)
        elif opcion.startswith("8"):
            flota.nave_extremos()
        elif opcion.startswith("9"):
            print("¡Fin del programa!")
            break
