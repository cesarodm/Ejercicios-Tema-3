class Matriz:
    def __init__(self, datos):
        if len(datos) != 3 or any(len(fila) != 3 for fila in datos):
            raise ValueError("La matriz debe ser de tamaño 3x3.")
        self.datos = datos

    def __str__(self):
        return "\n".join(["\t".join(map(str, fila)) for fila in self.datos])
