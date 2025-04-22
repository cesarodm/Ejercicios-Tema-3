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


# Ejercicio 3: El Gran Rally Espacial

Este proyecto consiste en la gestión y análisis de una lista de naves espaciales pertenecientes a una carrera intergaláctica. Cada nave posee información como nombre, longitud, cantidad de tripulantes y pasajeros.

El programa permite realizar diferentes operaciones sobre esta lista mediante un menú interactivo en consola.

## Funcionalidades implementadas

1. Ordenar las naves por nombre (ascendente).
2. Ordenar las naves por longitud (descendente).
3. Mostrar la información de las naves "Cometa Veloz" y "Titán del Cosmos".
4. Determinar las cinco naves con mayor cantidad de pasajeros.
5. Indicar la nave que requiere la mayor cantidad de tripulación.
6. Mostrar todas las naves cuyo nombre comience con "GX".
7. Listar todas las naves que pueden llevar seis o más pasajeros.
8. Mostrar la nave más pequeña y la más grande.
9. Salir del programa.

## Estructura del proyecto

- `main.py`: punto de entrada del programa.
- `menu.py`: contiene el menú interactivo y la lógica de navegación.
- `nave.py`: clase `Nave`, que representa a cada nave espacial.
- `flota.py`: clase `Flota`, que gestiona la lista de naves y contiene todos los métodos de ordenamiento, búsqueda y filtrado.
- `datos_prueba.py`: lista de naves de ejemplo para pruebas.
- `README.md`: documentación del proyecto.




# Ejercicio 4: La Matemática de los Encantamientos

Este proyecto implementa un sistema de manipulación de polinomios utilizando programación orientada a objetos en Python. El objetivo es simular la interacción con un grimorio mágico que contiene estructuras de datos que representan polinomios.

## Descripción del ejercicio

Se debe implementar una aplicación que permita realizar las siguientes operaciones sobre polinomios:

1. Restar dos polinomios.
2. Dividir dos polinomios.
3. Eliminar un término de un polinomio.
4. Verificar si un término específico (por exponente) existe en un polinomio.

Estas funcionalidades se acceden mediante un menú interactivo en consola.

## Estructura del proyecto

- `main.py`: punto de entrada del programa.
- `menu.py`: contiene el menú interactivo con navegación por flechas.
- `polinomio.py`: definición de las clases `Polinomio` y `Termino`.
- `operaciones.py`: funciones para realizar la resta y la división de polinomios.
- `utils.py`: funciones auxiliares para la entrada de datos y visualización de resultados.
- `README.md`: documentación del proyecto.