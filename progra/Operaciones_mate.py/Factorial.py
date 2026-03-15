def factorial(n):
    """
    Calcula el factorial de un número entero no negativo.

    Parámetros:
    n (int): Número entero mayor o igual a 0.

    Retorna:
    int: El factorial de n.

    Ejemplo:
    >>> factorial(5)
    120
    """
    if n < 0:
        raise ValueError("El factorial no está definido para números negativos.")
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
    return resultado
