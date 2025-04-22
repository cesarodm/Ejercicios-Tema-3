class Flota:
    def __init__(self, lista_naves):
        self.naves = lista_naves

    def ordenar_por_nombre(self):
        ordenadas = sorted(self.naves, key=lambda nave: nave.nombre)
        for nave in ordenadas:
            print(nave)

    def ordenar_por_longitud(self):
        ordenadas = sorted(self.naves, key=lambda nave: nave.longitud, reverse=True)
        for nave in ordenadas:
            print(nave)

    def mostrar_naves_especificas(self, nombres):
        for nave in self.naves:
            if nave.nombre in nombres:
                print(nave)

    def top_pasajeros(self, n):
        top = sorted(self.naves, key=lambda nave: nave.pasajeros, reverse=True)[:n]
        for nave in top:
            print(nave)

    def nave_max_tripulacion(self):
        max_nave = max(self.naves, key=lambda nave: nave.tripulacion)
        print(max_nave)

    def naves_con_prefijo(self, prefijo):
        for nave in self.naves:
            if nave.nombre.startswith(prefijo):
                print(nave)

    def naves_min_pasajeros(self, minimo):
        for nave in self.naves:
            if nave.pasajeros >= minimo:
                print(nave)

    def nave_extremos(self):
        menor = min(self.naves, key=lambda nave: nave.longitud)
        mayor = max(self.naves, key=lambda nave: nave.longitud)
        print("Nave más pequeña:\n", menor)
        print("Nave más grande:\n", mayor)
