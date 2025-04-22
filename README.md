# Ejercicios-Tema-3

https://github.com/cesarodm/Ejercicios-Tema-3.git


Puzle de la piramide de piedras preciosas

> Proyecto desarrollado en Python utilizando Programación Orientada a Objetos (POO) para resolver una variante del clásico problema de la Torre de Hanói.

---

Descripción

En lo profundo de una antigua pirámide egipcia yace una cámara secreta con una columna de 74 piedras preciosas de diferentes tamaños. Tu objetivo es trasladar todas estas piedras a otra columna, siguiendo reglas sagradas:

1. Solo puedes mover una piedra a la vez.
2. No se puede colocar una piedra más grande sobre una más pequeña.

Este reto es una adaptación del famoso problema de la **Torre de Hanói**, y al resolverlo correctamente, según la leyenda, descubrirás un antiguo tesoro escondido.

Estructura de proyecto 

piramide/ ├── main.py # Punto de entrada del programa ├── menu.py # Menú interactivo (interfaz de usuario) ├── juego.py # Lógica principal del puzzle ├── torre.py # Clases Torre y lógica de apilamiento ├── solucionador.py # Algoritmo recursivo para resolver el puzzle ├── visualizador.py # Visualización en consola, logs, temporizador └── log.txt # Registro de movimientos (generado automáticamente)












# El Secreto de la Cifra Mágica

Este proyecto resuelve el determinante de una matriz cuadrada de 3x3 utilizando dos métodos distintos:

- Método recursivo (expansión por cofactores)
- Método iterativo (regla de Sarrus)

El ejercicio consiste en introducir una matriz 3x3 y calcular su determinante mediante uno de los dos métodos, que se pueden seleccionar a través de un menú interactivo en consola.

## Descripción del ejercicio

En las páginas de un antiguo libro de matemáticas aparece una matriz cuadrada de 3x3 con números desconocidos. Se dice que al resolver el determinante de esta matriz, se revelará la ubicación de una cifra mágica. Para ello, se debe implementar un programa que calcule el determinante de la matriz utilizando:

- El método recursivo
- El método iterativo

## Estructura del proyecto

- `main.py`: punto de entrada del programa.
- `menu.py`: contiene el menú interactivo.
- `matriz.py`: clase `Matriz` para representar y validar una matriz 3x3.
- `determinante.py`: funciones que implementan ambos métodos de cálculo del determinante.
- `utils.py`: funciones auxiliares para entrada y salida de datos.