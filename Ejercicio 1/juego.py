from torre import Torre
from solucionador import resolver_hanoi
from visualizador import iniciar_log, finalizar_log, imprimir_torres, temporizador

class JuegoPiramide:
    def __init__(self, numero_piedras=74):
        self.torre_origen = Torre("Torre Origen")
        self.torre_auxiliar = Torre("Torre Auxiliar")
        self.torre_destino = Torre("Torre Destino")
        self.numero_piedras = numero_piedras

        for tamaño in range(numero_piedras, 0, -1):
            self.torre_origen.agregar_piedra(tamaño)

    @temporizador
    def iniciar(self):
        iniciar_log()
        print(f"\n🔄 Trasladando {self.numero_piedras} piedras desde la Torre Origen hasta la Torre Destino...\n")
        imprimir_torres(self.torre_origen, self.torre_auxiliar, self.torre_destino)
        resolver_hanoi(self.numero_piedras, self.torre_origen, self.torre_destino, self.torre_auxiliar)
        print("\n✅ Puzzle completado. ¡Has descubierto el tesoro escondido!")
        finalizar_log()
