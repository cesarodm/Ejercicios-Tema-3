from polinomio import Polinomio, Termino

def restar_polinomios(p1, p2):
    resultado = Polinomio()
    # Copiar todos los términos de p1
    for t in p1.terminos:
        resultado.agregar_termino(t.coef, t.exp)
    # Restar los términos de p2
    for t in p2.terminos:
        resultado.agregar_termino(-t.coef, t.exp)
    return resultado

def dividir_polinomios(p1, p2):
    resultado = Polinomio()
    p1_ordenado = sorted(p1.terminos, key=lambda t: -t.exp)
    p2_ordenado = sorted(p2.terminos, key=lambda t: -t.exp)

    dividendo = p1_ordenado.copy()
    divisor = p2_ordenado

    while dividendo and dividendo[0].exp >= divisor[0].exp:
        lead_dividendo = dividendo[0]
        lead_divisor = divisor[0]
        nuevo_coef = lead_dividendo.coef / lead_divisor.coef
        nuevo_exp = lead_dividendo.exp - lead_divisor.exp
        resultado.agregar_termino(nuevo_coef, nuevo_exp)
        # Crear subpolinomio para restar
        sub = Polinomio([Termino(nuevo_coef * t.coef, t.exp + nuevo_exp) for t in divisor])
        dividendo = restar_polinomios(Polinomio(dividendo), sub).terminos
        dividendo = sorted(dividendo, key=lambda t: -t.exp)
    return resultado
