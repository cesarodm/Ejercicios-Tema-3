from polinomio import Polinomio

def crear_polinomio(identificador=""):
    print(f"Ingresando términos del {identificador} polinomio:")
    pol = Polinomio()
    while True:
        coef = input("Coeficiente (o vacío para terminar): ")
        if coef.strip() == "":
            break
        exp = input("Exponente: ")
        try:
            pol.agregar_termino(float(coef), int(exp))
        except ValueError:
            print("Entrada inválida. Intenta de nuevo.")
    return pol

def mostrar_resultado(polinomio, titulo="Resultado"):
    print(f"\n{titulo}:")
    print(polinomio)
