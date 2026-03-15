def fibonacci(n):
    """
    Genera una lista con los primeros n números de la secuencia de Fibonacci.

    Parámetros:
    n (int): Cantidad de números de la secuencia que se desean obtener.
             Debe ser un entero mayor o igual a 1.

    Retorna:
    list: Lista con los primeros n números de Fibonacci.

    Ejemplo:
    >>> fibonacci(5)
    [0, 1, 1, 2, 3]
    """
    if n <= 0:
        raise ValueError("n debe ser un entero positivo.")
    
    secuencia = [0, 1]
    while len(secuencia) < n:
        secuencia.append(secuencia[-1] + secuencia[-2])
    
    return secuencia[:n]