class Matriz:
    def __init__(self, datos):
        if len(datos) != 3 or any(len(fila) != 3 for fila in datos):
            raise ValueError("La matriz debe ser 3x3.")
        self.datos = datos

    def __str__(self):
        filas = ["\t".join(f"{val:^5}" for val in fila) for fila in self.datos]
        return "\n".join(filas)
