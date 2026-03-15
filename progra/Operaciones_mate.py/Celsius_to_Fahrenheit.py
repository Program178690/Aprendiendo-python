def celsius_a_fahrenheit(celsius):
    """
    Convierte una temperatura de grados Celsius a grados Fahrenheit.

    Parámetros:
    celsius (float): Temperatura en grados Celsius.

    Retorna:
    float: Temperatura equivalente en grados Fahrenheit.

    Fórmula:
    F = (C * 9/5) + 32

    Ejemplo:
    >>> celsius_a_fahrenheit(0)
    32.0
    >>> celsius_a_fahrenheit(100)
    212.0
    """
    return (celsius * 9/5) + 32
