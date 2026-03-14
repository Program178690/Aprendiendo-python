def area_circulo(radio):
    pi = 3.14159
    return pi * radio ** 2


print (area_circulo(5))
print (area_circulo(10))
print (area_circulo(2.5))

print("\n")

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


print(es_primo(7))   
print(es_primo(10))  
print(es_primo(2))
print("\n")

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


print(factorial(5)) 
print(factorial(3))
print(factorial(2)) 
print("\n")

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


print(fibonacci(5)) 
print(fibonacci(10)) 
print(fibonacci(15)) 
print("\n")

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



print(celsius_a_fahrenheit(50))   
print(celsius_a_fahrenheit(100))  
print(celsius_a_fahrenheit(150)) 
print("\n")

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



print(numero_maximo([3, 7, 2, 9, 5]))  
print(numero_maximo([-10, -3, -25, -1]))  
print(numero_maximo([-10, -3, -25, 50]))  

