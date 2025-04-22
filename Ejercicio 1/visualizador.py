import time

LOG_PATH = "log.txt"

def imprimir_torres(origen, auxiliar, destino):
    print("\n📊 Estado actual:")
    print(f"{origen}")
    print(f"{auxiliar}")
    print(f"{destino}")
    print("-" * 40)

def registrar_movimiento(piedra, origen, destino):
    texto = f"🪨 Mover piedra {piedra} de {origen} a {destino}"
    print(texto)
    with open(LOG_PATH, "a", encoding="utf-8") as log:
        log.write(texto + "\n")

def iniciar_log():
    with open(LOG_PATH, "w", encoding="utf-8") as log:
        log.write("🔺 REGISTRO DE MOVIMIENTOS DEL PUZZLE 🔺\n\n")

def finalizar_log():
    with open(LOG_PATH, "a", encoding="utf-8") as log:
        log.write("\n✅ Puzzle completado con éxito.\n")

def temporizador(funcion):
    def wrapper(*args, **kwargs):
        inicio = time.time()
        resultado = funcion(*args, **kwargs)
        fin = time.time()
        print(f"\n⏱ Tiempo total: {fin - inicio:.2f} segundos.")
        return resultado
    return wrapper
