

import sys   # Se importa para modificar el limite de recursion del interprete
import time  # Se importa para medir el tiempo de ejecucion con perf_counter
import random  # Se importa para generar listas con elementos aleatorios

sys.setrecursionlimit(25000)  # Amplia el limite de recursion a 25000 para soportar listas de hasta 10000 elementos


# ALGORITMOS DE BUSQUEDA


# Busqueda secuencial iterativa
# Entradas: lista es la lista de elementos donde se busca, objetivo es el valor buscado
# Salidas: retorna el indice de la primera ocurrencia del objetivo, o -1 si no existe
# Restricciones: lista no debe ser None ni vacia, los elementos deben ser comparables con ==
# Funcionamiento: recorre la lista posicion a posicion desde el inicio hasta el final
def busqueda_secuencial_iterativa(lista, objetivo):
    for i in range(len(lista)):  # Recorre cada indice de la lista desde el primero hasta el ultimo
        if lista[i] == objetivo:  # Compara el elemento en la posicion i con el valor que se busca
            return i  # Retorna el indice actual porque se encontro el objetivo
    return -1  # Retorna -1 porque se recorrio toda la lista sin encontrar el objetivo


# Busqueda secuencial recursiva
# Entradas: lista es la lista de elementos, objetivo es el valor buscado,
#           indice es la posicion actual y debe ser 0 en la llamada externa
# Salidas: retorna el indice de la primera ocurrencia del objetivo, o -1 si no existe
# Restricciones: lista no debe ser None ni vacia, los elementos deben ser comparables con ==,
#                indice no debe modificarse externamente, puede fallar con listas muy grandes
# Funcionamiento: compara lista en indice con objetivo y avanza de uno en uno de forma recursiva
def busqueda_secuencial_recursiva(lista, objetivo, indice=0):
    if indice >= len(lista):  # Caso base: se llego al final de la lista sin encontrar el objetivo
        return -1  # Retorna -1 porque el objetivo no esta en la lista
    if lista[indice] == objetivo:  # Compara el elemento en la posicion actual con el objetivo
        return indice  # Retorna el indice actual porque hay coincidencia
    return busqueda_secuencial_recursiva(lista, objetivo, indice + 1)  # Llama recursivamente avanzando al siguiente indice



# Entradas: lista es una lista ordenada ascendentemente, objetivo es el valor buscado
# Salidas: retorna el indice del elemento encontrado, o -1 si no existe
# Restricciones: lista DEBE estar ordenada ascendentemente, no debe ser None ni vacia,
#                los elementos deben ser comparables con los operadores menor, mayor e igual
# Funcionamiento: divide el espacio de busqueda a la mitad en cada iteracion usando dos punteros
def busqueda_binaria_iterativa(lista, objetivo):
    izquierda, derecha = 0, len(lista) - 1  # Inicializa el puntero izquierdo al primer indice y el derecho al ultimo
    while izquierda <= derecha:  # Repite mientras el rango de busqueda tenga al menos un elemento
        medio = (izquierda + derecha) // 2  # Calcula el indice del elemento central del rango activo
        if lista[medio] == objetivo:  # Verifica si el elemento central es exactamente el objetivo
            return medio  # Retorna el indice del elemento central porque es el objetivo
        elif lista[medio] < objetivo:  # Verifica si el elemento central es menor que el objetivo
            izquierda = medio + 1  # Descarta la mitad izquierda porque el objetivo esta a la derecha
        else:  # Si el elemento central es mayor que el objetivo entra al else
            derecha = medio - 1  # Descarta la mitad derecha porque el objetivo esta a la izquierda
    return -1  # Retorna -1 porque el rango quedo vacio y el objetivo no existe



# Entradas: lista es una lista ordenada ascendentemente, objetivo es el valor buscado,
#           izquierda es el limite inferior del rango y derecha es el limite superior,
#           ambos deben omitirse en la llamada externa
# Salidas: retorna el indice del elemento encontrado, o -1 si no existe
# Restricciones: lista DEBE estar ordenada ascendentemente, no debe ser None ni vacia,
#                los elementos deben ser comparables con menor, mayor e igual,
#                izquierda y derecha no deben pasarse en la llamada externa
# Funcionamiento: divide el espacio de busqueda a la mitad en cada llamada recursiva
def busqueda_binaria_recursiva(lista, objetivo, izquierda=0, derecha=None):
    if derecha is None:  # En la primera llamada derecha llega como None y se debe inicializar
        derecha = len(lista) - 1  # Asigna el indice del ultimo elemento como limite superior inicial
    if izquierda > derecha:  # Caso base: el rango quedo vacio, el objetivo no existe en la lista
        return -1  # Retorna -1 porque no hay elementos que revisar
    medio = (izquierda + derecha) // 2  # Calcula el indice del elemento central del rango actual
    if lista[medio] == objetivo:  # Verifica si el elemento central coincide con el objetivo
        return medio  # Retorna el indice central porque se encontro el objetivo
    elif lista[medio] < objetivo:  # Verifica si el elemento central es menor que el objetivo
        return busqueda_binaria_recursiva(lista, objetivo, medio + 1, derecha)  # Recurre sobre la mitad derecha
    else:  # Si el elemento central es mayor que el objetivo entra al else
        return busqueda_binaria_recursiva(lista, objetivo, izquierda, medio - 1)  # Recurre sobre la mitad izquierda

# Ordenamiento burbuja iterativo
# Entradas: lista es la lista de elementos a ordenar
# Salidas: retorna una nueva lista con los mismos elementos en orden ascendente,
#          la lista original no es modificada
# Restricciones: lista no debe ser None, los elementos deben ser comparables con mayor e igual
# Funcionamiento: compara pares de elementos adyacentes e intercambia los que estan fuera de orden
def burbuja_iterativo(lista):
    resultado = lista[:]  # Crea una copia de la lista para no modificar la original
    n = len(resultado)  # Guarda la cantidad de elementos en la lista
    for i in range(n - 1):  # Bucle externo que controla el numero de pasadas, necesita n menos 1 pasadas
        for j in range(n - 1 - i):  # Bucle interno que compara pares adyacentes ignorando los ya ubicados al final
            if resultado[j] > resultado[j + 1]:  # Compara el elemento actual con el siguiente para ver si estan fuera de orden
                resultado[j], resultado[j + 1] = resultado[j + 1], resultado[j]  # Intercambia los dos elementos porque estan en orden incorrecto
    return resultado  # Retorna la lista con todos los elementos en orden ascendente


# Ordenamiento burbuja recursivo
# Entradas: lista es la lista de elementos a ordenar,
#           n es la cantidad de elementos activos y debe omitirse en la llamada externa
# Salidas: retorna la lista con los mismos elementos en orden ascendente
# Restricciones: lista no debe ser None, los elementos deben ser comparables con mayor e igual,
#                n no debe pasarse en la llamada externa,
#                puede fallar con listas muy grandes por el limite de recursion
# Funcionamiento: realiza una pasada burbuja sobre los primeros n elementos y recurre con n menos 1
def burbuja_recursiva(lista, n=None):
    if n is None:  # En la primera llamada n llega como None y se debe inicializar
        lista = lista[:]  # Crea una copia de la lista para no modificar la original
        n = len(lista)  # Asigna la cantidad total de elementos como tamano activo inicial
    if n <= 1:  # Caso base: una lista de 0 o 1 elementos ya esta ordenada
        return lista  # Retorna la lista porque no hay nada que ordenar
    for j in range(n - 1):  # Realiza una pasada burbuja sobre los primeros n elementos
        if lista[j] > lista[j + 1]:  # Compara el elemento actual con el siguiente
            lista[j], lista[j + 1] = lista[j + 1], lista[j]  # Intercambia los dos elementos si estan en orden incorrecto
    return burbuja_recursiva(lista, n - 1)  # Recurre sobre los primeros n menos 1 elementos porque el mayor ya quedo al final


# Ordenamiento por seleccion iterativo
# Entradas: lista es la lista de elementos a ordenar
# Salidas: retorna una nueva lista con los mismos elementos en orden ascendente,
#          la lista original no es modificada
# Restricciones: lista no debe ser None, los elementos deben ser comparables con menor e igual
# Funcionamiento: busca el minimo del subarreglo no ordenado y lo coloca en su posicion definitiva
def seleccion_iterativo(lista):
    resultado = lista[:]  # Crea una copia de la lista para no modificar la original
    n = len(resultado)  # Guarda la cantidad de elementos en la lista
    for i in range(n - 1):  # Bucle externo que avanza la posicion donde se colocara el minimo encontrado
        idx_min = i  # Asume que el elemento minimo esta en la posicion i
        for j in range(i + 1, n):  # Recorre el subarreglo no ordenado buscando un elemento mas pequeno
            if resultado[j] < resultado[idx_min]:  # Compara si el elemento actual es menor que el minimo conocido
                idx_min = j  # Guarda el indice del nuevo minimo encontrado
        resultado[i], resultado[idx_min] = resultado[idx_min], resultado[i]  # Coloca el minimo encontrado en su posicion definitiva
    return resultado  # Retorna la lista con todos los elementos en orden ascendente


# Ordenamiento por seleccion recursivo
# Entradas: lista es la lista de elementos a ordenar,
#           inicio es la posicion desde donde comienza el subarreglo sin ordenar,
#           debe ser 0 en la llamada externa
# Salidas: retorna la lista con los mismos elementos en orden ascendente
# Restricciones: lista no debe ser None, los elementos deben ser comparables con menor e igual,
#                inicio debe ser 0 en la llamada inicial,
#                puede fallar con listas muy grandes por el limite de recursion
# Funcionamiento: busca el minimo desde inicio, lo coloca ahi y recurre sobre el resto
def seleccion_recursiva(lista, inicio=0):
    if inicio == 0:  # En la primera llamada crea una copia para no modificar la lista original
        lista = lista[:]  # Copia la lista para trabajar sobre ella sin alterar la original
    n = len(lista)  # Obtiene la longitud total de la lista
    if inicio >= n - 1:  # Caso base: el subarreglo no ordenado tiene 0 o 1 elemento
        return lista  # Retorna la lista porque ya esta completamente ordenada
    idx_min = inicio  # Asume que el minimo esta en la posicion inicio
    for j in range(inicio + 1, n):  # Recorre el subarreglo buscando el elemento minimo
        if lista[j] < lista[idx_min]:  # Compara si el elemento actual es menor que el minimo conocido
            idx_min = j  # Guarda el indice del nuevo elemento minimo
    lista[inicio], lista[idx_min] = lista[idx_min], lista[inicio]  # Coloca el minimo en su posicion definitiva
    return seleccion_recursiva(lista, inicio + 1)  # Recurre sobre el siguiente subarreglo avanzando inicio en uno


# Ordenamiento rapido iterativo
# Entradas: lista es la lista de elementos a ordenar
# Salidas: retorna una nueva lista con los mismos elementos en orden ascendente,
#          la lista original no es modificada
# Restricciones: lista no debe ser None, los elementos deben ser comparables con menor igual e igual
# Funcionamiento: simula la recursion con una pila explicita y usa el pivote central
#                 para evitar el peor caso en listas ya ordenadas o invertidas
def ordenamiento_rapido_iterativo(lista):
    resultado = lista[:]  # Crea una copia de la lista para no modificar la original
    n = len(resultado)  # Guarda la cantidad de elementos en la lista
    if n <= 1:  # Una lista de 0 o 1 elementos ya esta ordenada, no hay nada que hacer
        return resultado  # Retorna la copia directamente porque no requiere ordenamiento
    pila = [(0, n - 1)]  # Inicializa la pila con el rango completo de la lista
    while pila:  # Repite mientras haya rangos pendientes de ordenar en la pila
        bajo, alto = pila.pop()  # Extrae el rango mas reciente de la pila
        if bajo < alto:  # Solo procesa rangos que tengan al menos dos elementos
            medio = (bajo + alto) // 2  # Calcula el indice del elemento central del rango
            resultado[medio], resultado[alto] = resultado[alto], resultado[medio]  # Mueve el pivote central al final para facilitar la particion
            pivote = resultado[alto]  # Guarda el valor del pivote que ahora esta al final
            i = bajo - 1  # Puntero que delimita el limite de la particion izquierda
            for j in range(bajo, alto):  # Recorre el rango sin incluir la posicion del pivote
                if resultado[j] <= pivote:  # Si el elemento es menor o igual al pivote lo mueve a la izquierda
                    i += 1  # Avanza el puntero de la particion izquierda
                    resultado[i], resultado[j] = resultado[j], resultado[i]  # Intercambia para colocar el elemento en la particion correcta
            pos_pivote = i + 1  # Calcula la posicion definitiva del pivote
            resultado[pos_pivote], resultado[alto] = resultado[alto], resultado[pos_pivote]  # Coloca el pivote en su posicion definitiva
            pila.append((bajo, pos_pivote - 1))  # Agrega el subrango izquierdo a la pila para ordenarlo despues
            pila.append((pos_pivote + 1, alto))  # Agrega el subrango derecho a la pila para ordenarlo despues
    return resultado  # Retorna la lista completamente ordenada


# Ordenamiento rapido recursivo
# Entradas: lista es la lista de elementos a ordenar
# Salidas: retorna una nueva lista con los mismos elementos en orden ascendente,
#          la lista original no es modificada
# Restricciones: lista no debe ser None,
#                los elementos deben ser comparables con menor, mayor e igual
# Funcionamiento: elige el elemento central como pivote, divide en menores iguales y mayores
#                 y concatena el resultado de ordenar cada parte recursivamente
def ordenamiento_rapido_recursivo(lista):
    if len(lista) <= 1:  # Caso base: lista vacia o de un elemento ya esta ordenada
        return lista[:]  # Retorna una copia de la lista porque no necesita ordenamiento
    pivote = lista[len(lista) // 2]  # Selecciona el elemento en la posicion central como pivote
    menores = [x for x in lista if x < pivote]  # Construye la sublista con todos los elementos menores al pivote
    iguales = [x for x in lista if x == pivote]  # Construye la sublista con todos los elementos iguales al pivote
    mayores = [x for x in lista if x > pivote]  # Construye la sublista con todos los elementos mayores al pivote
    return ordenamiento_rapido_recursivo(menores) + iguales + ordenamiento_rapido_recursivo(mayores)  # Retorna la concatenacion de menores ordenados, iguales y mayores ordenados

# Genera una lista ordenada de n enteros ascendentes
# Entradas: n es la cantidad de elementos y debe ser un entero positivo
# Salidas: retorna la lista con los valores de 0 hasta n menos 1 en orden ascendente
# Restricciones: n debe ser un entero positivo
def generar_lista_ordenada(n):
    return list(range(n))  # Genera y retorna la lista de 0 hasta n menos 1 usando range


# Genera una lista invertida de n enteros descendentes
# Entradas: n es la cantidad de elementos y debe ser un entero positivo
# Salidas: retorna la lista con los valores de n menos 1 hasta 0 en orden descendente
# Restricciones: n debe ser un entero positivo
def generar_lista_invertida(n):
    return list(range(n - 1, -1, -1))  # Genera y retorna la lista de n menos 1 hasta 0 usando range con paso negativo


# Genera una lista desordenada de n enteros unicos aleatorios
# Entradas: n es la cantidad de elementos y debe ser un entero positivo
# Salidas: retorna una lista con n enteros unicos tomados al azar del rango de 0 a 10 veces n
# Restricciones: n debe ser un entero positivo
def generar_lista_desordenada(n):
    return random.sample(range(n * 10), n)  # Selecciona n enteros unicos al azar del rango de 0 a 10 veces n sin repeticion

# Mide el tiempo que tarda una funcion en ejecutarse
# Entradas: funcion es el callable a medir, args son los argumentos que recibe la funcion
# Salidas: retorna el tiempo transcurrido en segundos como un numero flotante
# Restricciones: funcion debe ser un callable valido
def medir_tiempo(funcion, *args):
    inicio = time.perf_counter()  # Registra el tiempo exacto antes de ejecutar la funcion
    funcion(*args)  # Ejecuta la funcion pasandole todos los argumentos recibidos
    fin = time.perf_counter()  # Registra el tiempo exacto despues de que la funcion termina
    return fin - inicio  # Retorna la diferencia entre el tiempo final y el inicial en segundos


# Ejecuta todos los algoritmos sobre listas de distintos tamanos y tipos y mide los tiempos
# Entradas: tamanos es una lista de enteros positivos que indican cuantos elementos usar
# Salidas: retorna un diccionario anidado con los tiempos medidos por algoritmo y tipo de lista
# Restricciones: tamanos no debe estar vacio y sus elementos deben ser enteros positivos,
#                con n igual a 10000 burbuja y seleccion pueden tardar varios segundos
def ejecutar_analisis(tamanos):
    resultados = {  # Crea el diccionario que almacenara los tiempos organizados por algoritmo y tipo de lista
        'Busqueda Secuencial': {
            'Iterativa - Ordenada':    [],
            'Iterativa - Desordenada': [],
            'Recursiva - Ordenada':    [],
            'Recursiva - Desordenada': [],
        },
        'Busqueda Binaria': {
            'Iterativa - Ordenada': [],
            'Recursiva - Ordenada': [],
        },
        'Burbuja': {
            'Iterativo - Ordenada':    [],
            'Iterativo - Desordenada': [],
            'Iterativo - Invertida':   [],
            'Recursivo - Ordenada':    [],
            'Recursivo - Desordenada': [],
            'Recursivo - Invertida':   [],
        },
        'Seleccion': {
            'Iterativo - Ordenada':    [],
            'Iterativo - Desordenada': [],
            'Iterativo - Invertida':   [],
            'Recursivo - Ordenada':    [],
            'Recursivo - Desordenada': [],
            'Recursivo - Invertida':   [],
        },
        'Ordenamiento Rapido': {
            'Iterativo - Ordenada':    [],
            'Iterativo - Desordenada': [],
            'Iterativo - Invertida':   [],
            'Recursivo - Ordenada':    [],
            'Recursivo - Desordenada': [],
            'Recursivo - Invertida':   [],
        },
    }

    for n in tamanos:  # Itera sobre cada tamano de lista definido en la lista tamanos
        print(f"  n = {n:>6} ...", end='', flush=True)  # Imprime el tamano actual para indicar el progreso al usuario

        ordenada    = generar_lista_ordenada(n)     # Genera la lista ordenada de n elementos para las pruebas
        desordenada = generar_lista_desordenada(n)  # Genera la lista desordenada de n elementos para las pruebas
        invertida   = generar_lista_invertida(n)    # Genera la lista invertida de n elementos para las pruebas

        obj_ord = ordenada[-1]     # Define el objetivo como el ultimo elemento de la lista ordenada, que es el peor caso para busqueda secuencial
        obj_des = desordenada[-1]  # Define el objetivo como el ultimo elemento de la lista desordenada

        resultados['Busqueda Secuencial']['Iterativa - Ordenada'].append(
            medir_tiempo(busqueda_secuencial_iterativa, ordenada, obj_ord))     # Mide y guarda el tiempo de la busqueda secuencial iterativa sobre lista ordenada
        resultados['Busqueda Secuencial']['Iterativa - Desordenada'].append(
            medir_tiempo(busqueda_secuencial_iterativa, desordenada, obj_des))  # Mide y guarda el tiempo de la busqueda secuencial iterativa sobre lista desordenada
        resultados['Busqueda Secuencial']['Recursiva - Ordenada'].append(
            medir_tiempo(busqueda_secuencial_recursiva, ordenada, obj_ord))     # Mide y guarda el tiempo de la busqueda secuencial recursiva sobre lista ordenada
        resultados['Busqueda Secuencial']['Recursiva - Desordenada'].append(
            medir_tiempo(busqueda_secuencial_recursiva, desordenada, obj_des))  # Mide y guarda el tiempo de la busqueda secuencial recursiva sobre lista desordenada

        resultados['Busqueda Binaria']['Iterativa - Ordenada'].append(
            medir_tiempo(busqueda_binaria_iterativa, ordenada, obj_ord))  # Mide y guarda el tiempo de la busqueda binaria iterativa sobre lista ordenada
        resultados['Busqueda Binaria']['Recursiva - Ordenada'].append(
            medir_tiempo(busqueda_binaria_recursiva, ordenada, obj_ord))  # Mide y guarda el tiempo de la busqueda binaria recursiva sobre lista ordenada

        resultados['Burbuja']['Iterativo - Ordenada'].append(
            medir_tiempo(burbuja_iterativo, ordenada))      # Mide y guarda el tiempo del burbuja iterativo sobre lista ordenada
        resultados['Burbuja']['Iterativo - Desordenada'].append(
            medir_tiempo(burbuja_iterativo, desordenada))   # Mide y guarda el tiempo del burbuja iterativo sobre lista desordenada
        resultados['Burbuja']['Iterativo - Invertida'].append(
            medir_tiempo(burbuja_iterativo, invertida))     # Mide y guarda el tiempo del burbuja iterativo sobre lista invertida
        resultados['Burbuja']['Recursivo - Ordenada'].append(
            medir_tiempo(burbuja_recursiva, ordenada))      # Mide y guarda el tiempo del burbuja recursivo sobre lista ordenada
        resultados['Burbuja']['Recursivo - Desordenada'].append(
            medir_tiempo(burbuja_recursiva, desordenada))   # Mide y guarda el tiempo del burbuja recursivo sobre lista desordenada
        resultados['Burbuja']['Recursivo - Invertida'].append(
            medir_tiempo(burbuja_recursiva, invertida))     # Mide y guarda el tiempo del burbuja recursivo sobre lista invertida

        resultados['Seleccion']['Iterativo - Ordenada'].append(
            medir_tiempo(seleccion_iterativo, ordenada))      # Mide y guarda el tiempo de seleccion iterativo sobre lista ordenada
        resultados['Seleccion']['Iterativo - Desordenada'].append(
            medir_tiempo(seleccion_iterativo, desordenada))   # Mide y guarda el tiempo de seleccion iterativo sobre lista desordenada
        resultados['Seleccion']['Iterativo - Invertida'].append(
            medir_tiempo(seleccion_iterativo, invertida))     # Mide y guarda el tiempo de seleccion iterativo sobre lista invertida
        resultados['Seleccion']['Recursivo - Ordenada'].append(
            medir_tiempo(seleccion_recursiva, ordenada))      # Mide y guarda el tiempo de seleccion recursivo sobre lista ordenada
        resultados['Seleccion']['Recursivo - Desordenada'].append(
            medir_tiempo(seleccion_recursiva, desordenada))   # Mide y guarda el tiempo de seleccion recursivo sobre lista desordenada
        resultados['Seleccion']['Recursivo - Invertida'].append(
            medir_tiempo(seleccion_recursiva, invertida))     # Mide y guarda el tiempo de seleccion recursivo sobre lista invertida

        resultados['Ordenamiento Rapido']['Iterativo - Ordenada'].append(
            medir_tiempo(ordenamiento_rapido_iterativo, ordenada))      # Mide y guarda el tiempo del ordenamiento rapido iterativo sobre lista ordenada
        resultados['Ordenamiento Rapido']['Iterativo - Desordenada'].append(
            medir_tiempo(ordenamiento_rapido_iterativo, desordenada))   # Mide y guarda el tiempo del ordenamiento rapido iterativo sobre lista desordenada
        resultados['Ordenamiento Rapido']['Iterativo - Invertida'].append(
            medir_tiempo(ordenamiento_rapido_iterativo, invertida))     # Mide y guarda el tiempo del ordenamiento rapido iterativo sobre lista invertida
        resultados['Ordenamiento Rapido']['Recursivo - Ordenada'].append(
            medir_tiempo(ordenamiento_rapido_recursivo, ordenada))      # Mide y guarda el tiempo del ordenamiento rapido recursivo sobre lista ordenada
        resultados['Ordenamiento Rapido']['Recursivo - Desordenada'].append(
            medir_tiempo(ordenamiento_rapido_recursivo, desordenada))   # Mide y guarda el tiempo del ordenamiento rapido recursivo sobre lista desordenada
        resultados['Ordenamiento Rapido']['Recursivo - Invertida'].append(
            medir_tiempo(ordenamiento_rapido_recursivo, invertida))     # Mide y guarda el tiempo del ordenamiento rapido recursivo sobre lista invertida

        print(" listo")  # Imprime que el tamano actual termino de procesar

    return resultados  # Retorna el diccionario con todos los tiempos medidos



# Coordina la ejecucion del analisis e imprime los tiempos en consola
# Entradas: ninguna, los parametros estan definidos internamente
# Salidas: ninguna, imprime los resultados en la consola estandar
# Restricciones: con n igual a 10000 burbuja y seleccion recursivos pueden tardar varios segundos
def main():
    tamanos = [10, 100, 1000, 10000]  # Define los cuatro tamanos de lista que se van a evaluar

    print("=" * 52)  # Imprime una linea separadora para mejorar la presentacion visual
    print("Ejecutando pruebas de las listas())...\n")  # Imprime aviso de que las pruebas pueden tardar con listas grandes

    resultados = ejecutar_analisis(tamanos)  # Ejecuta todos los algoritmos y recopila los tiempos

    print()  # Imprime una linea en blanco para separar el progreso de los resultados
    for algoritmo, series in resultados.items():  # Recorre cada algoritmo y sus series de tiempos
        print(f"\n{'-' * 52}")  # Imprime una linea separadora antes del nombre del algoritmo
        print(f"  {algoritmo}")  # Imprime el nombre del algoritmo como titulo de la seccion
        print(f"{'-' * 52}")  # Imprime una linea separadora debajo del nombre
        encabezado = f"  {'Serie (ms)':<28}" + "".join(f"{n:>10}" for n in tamanos)  # Construye la fila de encabezado con los tamanos de lista e indica que los tiempos estan en milisegundos
        print(encabezado)  # Imprime la fila de encabezado en la consola
        for serie, tiempos in series.items():  # Recorre cada variante del algoritmo y sus tiempos
            fila = f"  {serie:<28}" + "".join(f"{t * 1000:>10.4f}" for t in tiempos)  # Construye la fila multiplicando cada tiempo por 1000 para convertir de segundos a milisegundos
            print(fila)  # Imprime la fila de tiempos en milisegundos en la consola

    print(f"\n{'=' * 52}")  # Imprime una linea separadora al final de todos los resultados
    print("Analisis completado exitosamente.")  # Imprime mensaje indicando que el analisis termino correctamente


if __name__ == '__main__':  # Verifica que el script se ejecuta directamente y no fue importado como modulo
    main()  # Llama a la funcion principal para iniciar el analisis
