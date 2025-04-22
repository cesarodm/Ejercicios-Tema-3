class Termino:
    def __init__(self, coef, exp):
        self.coef = coef
        self.exp = exp

    def __str__(self):
        return f"{self.coef}x^{self.exp}"

class Polinomio:
    def __init__(self, terminos=None):
        self.terminos = terminos if terminos else []

    def agregar_termino(self, coef, exp):
        self.terminos.append(Termino(coef, exp))

    def eliminar_termino(self, exp):
        self.terminos = [t for t in self.terminos if t.exp != exp]

    def existe_termino(self, exp):
        return any(t.exp == exp for t in self.terminos)

    def __str__(self):
        if not self.terminos:
            return "0"
        ordenados = sorted(self.terminos, key=lambda t: t.exp, reverse=True)
        return " + ".join(str(t) for t in ordenados)
