class Torre:
    def __init__(self, nombre):
        self.nombre = nombre
        self.pila_piedras = []

    def agregar_piedra(self, piedra):
        if self.pila_piedras and self.pila_piedras[-1] < piedra:
            raise ValueError(f"No puedes colocar la piedra {piedra} sobre la más pequeña {self.pila_piedras[-1]}.")
        self.pila_piedras.append(piedra)

    def quitar_piedra(self):
        if not self.pila_piedras:
            raise ValueError(f"La {self.nombre} está vacía.")
        return self.pila_piedras.pop()

    def __str__(self):
        return f"{self.nombre} (tamaño actual: {len(self.pila_piedras)})"
