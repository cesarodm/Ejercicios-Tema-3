class Nave:
    def __init__(self, nombre, longitud, tripulacion, pasajeros):
        self.nombre = nombre
        self.longitud = float(longitud)
        self.tripulacion = int(tripulacion)
        self.pasajeros = int(pasajeros)

    def __str__(self):
        return (
            f"Nombre: {self.nombre}\n"
            f"Longitud: {self.longitud} m\n"
            f"Tripulación: {self.tripulacion}\n"
            f"Pasajeros: {self.pasajeros}\n"
        )
