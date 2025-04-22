import time
from visualizador import imprimir_torres, registrar_movimiento

def resolver_hanoi(n, origen, destino, auxiliar):
    if n == 1:
        piedra = origen.quitar_piedra()
        destino.agregar_piedra(piedra)
        registrar_movimiento(piedra, origen.nombre, destino.nombre)
        imprimir_torres(origen, auxiliar, destino)
        time.sleep(0.1)
    else:
        resolver_hanoi(n - 1, origen, auxiliar, destino)
        resolver_hanoi(1, origen, destino, auxiliar)
        resolver_hanoi(n - 1, auxiliar, destino, origen)

