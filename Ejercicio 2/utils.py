from matriz import Matriz

def pedir_matriz():
    print("\n🧮 Introduce los 9 valores de la matriz 3x3 (fila por fila):")
    datos = []
    for i in range(3):
        while True:
            fila = input(f"  ➤ Fila {i+1} (3 números separados por espacios): ").strip().split()
            if len(fila) == 3 and all(n.lstrip('-').isdigit() for n in fila):
                datos.append([int(n) for n in fila])
                break
            else:
                print("   ⚠️ Entrada inválida. Intenta de nuevo.")
    matriz = Matriz(datos)
    print("\n📋 Matriz introducida:")
    print(matriz)
    return matriz

def mostrar_resultado(valor, metodo):
    print(f"\n🔎 Determinante calculado por el método {metodo}:")
    print(f"\n✨ Resultado final: {valor}\n")
