def resolver_hanoi(n, origen, destino, auxiliar):
    if n == 1:
        piedra = origen.quitar_piedra()
        destino.agregar_piedra(piedra)
        print(f"🪨 Mover piedra {piedra} de {origen.nombre} a {destino.nombre}")
    else:
        resolver_hanoi(n - 1, origen, auxiliar, destino)
        resolver_hanoi(1, origen, destino, auxiliar)
        resolver_hanoi(n - 1, auxiliar, destino, origen)
