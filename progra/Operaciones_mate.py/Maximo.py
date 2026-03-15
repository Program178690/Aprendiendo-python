def numero_maximo(lista):
    """
    Encuentra el número máximo dentro de una lista de números.

    Parámetros:
    lista (list): Lista de números (enteros o flotantes).

    Retorna:
    float: El número máximo encontrado en la lista.

    Ejemplo:
    >>> numero_maximo([3, 7, 2, 9, 5])
    9
    """
    if not lista:
        raise ValueError("La lista no puede estar vacía.")
    
    maximo = lista[0]
    for numero in lista[1:]:
        if numero > maximo:
            maximo = numero
    return maximo
