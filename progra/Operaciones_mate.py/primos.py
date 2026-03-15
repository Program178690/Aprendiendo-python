def es_primo(n):
    """
    argumentos:
    Determina si un número es primo.

    Parámetros:
    n (int): Número entero mayor que 1.

    Retorna:
    bool: True si el número es primo, False en caso contrario.

    Ejemplo:
    >>> es_primo(7)
    True
    >>> es_primo(10)
    False
    """
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True