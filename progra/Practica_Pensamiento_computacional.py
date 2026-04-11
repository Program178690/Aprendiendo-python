print("Bienvenido al programa de cálculo de billetes.")
print("\n")

def calcular_billetes(monto):
   
   # El monto debe ser un númeor multiplo de 5 
    if monto % 5 != 0:
        print("Error: el monto debe ser múltiplo de 5.")
        return None

    # Lista de denominaciones disponibles
    denominaciones = [200, 100, 50, 20, 10, 5]
    resultado = {}

    # Calcular billetes
    for billete in denominaciones:
        cantidad = monto // billete
        if cantidad > 0:
            resultado[billete] = cantidad
            monto %= billete

    # Mostrar resultado
    salida = ", ".join([f"{resultado[b]}x Q{b}" for b in resultado])
    print(salida)
    return resultado

print(calcular_billetes(500))
print(calcular_billetes(725))

print("\n")

print("Validador de contraseñas")

print("\n")

def validar_password(password: str) -> bool:
    # Regla 1: mínimo 8 caracteres
    if len(password) < 8:
        return False
    
    # Regla 2: al menos una letra mayúscula
    if not any(c.isupper() for c in password):
        return False
    
    # Regla 3: al menos un dígito
    if not any(c.isdigit() for c in password):
        return False
    
    # Regla 4: al menos un carácter especial
    especiales = "!@#$%"
    if not any(c in especiales for c in password):
        return False
    
    return True


def diagnosticar_password(password: str) -> None:
    errores = []
    
    if len(password) < 8:
        errores.append("❌ Debe tener al menos 8 caracteres.")
    
    if not any(c.isupper() for c in password):
        errores.append("❌ Debe contener al menos una letra mayúscula.")
    
    if not any(c.isdigit() for c in password):
        errores.append("❌ Debe contener al menos un dígito.")
    
    especiales = "!@#$%"
    if not any(c in especiales for c in password):
        errores.append("❌ Debe contener al menos un carácter especial (!, @, #, $, %).")
    
    if errores:
        print("La contraseña NO cumple con las siguientes reglas:")
        for e in errores:
            print(e)
    else:
        print("✅ La contraseña cumple todas las reglas.")


# Ejemplo de uso
print(validar_password("Arcoiris@##23"))   # True
diagnosticar_password("Arcoiris@##23")      # Muestra qué reglas fallan

print("\n")

print("Conversor universal de temperaturas")

print("\n")

def celsius_a_fahrenheit(c: float) -> float:
    return c * 9/5 + 32

def fahrenheit_a_celsius(f: float) -> float:
    return (f - 32) * 5/9

def celsius_a_kelvin(c: float) -> float:
    return c + 273.15

def convertir(valor: float, origen: str, destino: str) -> float | None:
    origen = origen.upper()
    destino = destino.upper()
    
    # Si origen y destino son iguales, simplemente retorna el mismo valor
    if origen == destino:
        return valor
    
    # Convertir primero a Celsius como escala intermedia
    if origen == 'C':
        c = valor
    elif origen == 'F':
        c = fahrenheit_a_celsius(valor)
    elif origen == 'K':
        c = valor - 273.15
    else:
        return None  # Escala origen inválida
    
    # Ahora convertir desde Celsius a la escala destino
    if destino == 'C':
        return c
    elif destino == 'F':
        return celsius_a_fahrenheit(c)
    elif destino == 'K':
        return celsius_a_kelvin(c)
    else:
        return None  # Escala destino inválida



print(convertir(0, 'C', 'F'))   
print(convertir(32, 'F', 'C'))  
print(convertir(500, 'C', 'K')) 
print(convertir(212, 'F', 'K')) 
print(convertir(300, 'K', 'F')) 

print("\n")

print("Análisis de calificaciones")

print("\n")

def promedio(notas: list[float]) -> float:
    return sum(notas) / len(notas) if notas else 0

def mayor(notas: list[float]) -> float:
    if not notas:
        return None
    maximo = notas[0]
    for n in notas[1:]:
        if n > maximo:
            maximo = n
    return maximo

def menor(notas: list[float]) -> float:
    if not notas:
        return None
    minimo = notas[0]
    for n in notas[1:]:
        if n < minimo:
            minimo = n
    return minimo

def contar_aprobados(notas: list[float], minimo: int = 61) -> int:
    return sum(1 for n in notas if n >= minimo)

def reporte(notas: list[float]) -> None:
    print("📊 Reporte de Notas")
    print("-------------------")
    print(f"Promedio: {promedio(notas):.2f}")
    print(f"Nota más alta: {mayor(notas)}")
    print(f"Nota más baja: {menor(notas)}")
    print(f"Aprobados (mínimo 61): {contar_aprobados(notas)} de {len(notas)}")


# Prueba con la lista de notas
notas = [90, 45, 100, 65, 55, 90, 38, 77, 95, 45]

reporte(notas)

print("\n")

print("Generador de Tablas de Multiplicar")

print("\n")

import math

def tabla(n):
    """Imprime la tabla de multiplicar del número n (del 1 al 10)."""
    print(f"\nTabla del {n}:")
    for i in range(1, 11):
        print(f"{n} x {i} = {n * i}")

def es_primo(n):
    """Retorna True si n es primo, False si no lo es."""
    if n < 2:
        return False
    # Solo necesitamos verificar hasta la raíz cuadrada de n
    limite = int(math.sqrt(n)) + 1
    for i in range(2, limite):
        if n % i == 0:
            return False
    return True

def tablas_primos(limite):
    """Imprime las tablas de los números primos desde 2 hasta 'limite'."""
    for num in range(2, limite + 1):
        if es_primo(num):
            tabla(num)

# Ejemplo de uso:
tablas_primos(10)

print("\n")

print("Cifrado cesar")

def cifrar_caracter(c, desplazamiento):
    """Cifra un solo carácter usando el desplazamiento dado.
    Si no es letra, lo retorna sin cambios."""
    if 'a' <= c <= 'z':  # minúsculas
        return chr((ord(c) - ord('a') + desplazamiento) % 26 + ord('a'))
    elif 'A' <= c <= 'Z':  # mayúsculas
        return chr((ord(c) - ord('A') + desplazamiento) % 26 + ord('A'))
    else:
        return c  # no es letra, se deja igual

def cifrar_mensaje(mensaje, desplazamiento):
    """Cifra un mensaje completo usando cifrar_caracter()."""
    resultado = ""
    for c in mensaje:
        resultado += cifrar_caracter(c, desplazamiento)
    return resultado

def descifrar_mensaje(mensaje, desplazamiento):
    """Descifra un mensaje cifrado con el mismo desplazamiento."""
    return cifrar_mensaje(mensaje, -desplazamiento)

# Ejemplo de uso:
texto = "hola"
cifrado = cifrar_mensaje(texto, 3)
print("Texto original:", texto)
print("Texto cifrado :", cifrado)
print("Texto descifrado:", descifrar_mensaje(cifrado, 3))

print("\n")

print("Calculadora de propina con menu interactivo")

def calcular_propina(subtotal, porcentaje):
    """Retorna el monto de la propina."""
    return subtotal * (porcentaje / 100)

def calcular_total(subtotal, propina):
    """Retorna el total a pagar."""
    return subtotal + propina

def dividir_cuenta(total, personas):
    """Retorna cuánto paga cada persona. Maneja errores si personas <= 0."""
    if personas <= 0:
        return "Error: el número de personas debe ser mayor que 0."
    return total / personas

def aplicar_descuento(subtotal, descuento_pct):
    """Aplica un descuento porcentual y retorna el nuevo subtotal."""
    return subtotal * (1 - descuento_pct / 100)

def mostrar_menu():
    """Imprime las opciones disponibles."""
    print("\n--- Calculadora de Propinas ---")
    print("1. Calcular propina (sugerencias: 10%, 15%, 20%)")
    print("2. Dividir la cuenta entre personas")
    print("3. Aplicar descuento + propina")
    print("4. Salir")

def leer_numero(mensaje):
    """Lee un número con validación de errores."""
    while True:
        try:
            return float(input(mensaje))
        except ValueError:
            print("Entrada inválida. Por favor ingresa un número.")

def main():
    while True:
        mostrar_menu()
        opcion = input("Elige una opción: ")

        if opcion == "1":
            subtotal = leer_numero("Ingresa el subtotal: Q")
            porcentaje = leer_numero("Ingresa el porcentaje de propina: ")
            propina = calcular_propina(subtotal, porcentaje)
            total = calcular_total(subtotal, propina)
            print(f"Propina: Q{propina:.2f}")
            print(f"Total a pagar: Q{total:.2f}")

        elif opcion == "2":
            total = leer_numero("Ingresa el total de la cuenta: Q")
            personas = int(leer_numero("¿Entre cuántas personas dividir?: "))
            resultado = dividir_cuenta(total, personas)
            if isinstance(resultado, str):
                print(resultado)
            else:
                print(f"Cada persona paga: Q{resultado:.2f}")

        elif opcion == "3":
            subtotal = leer_numero("Ingresa el subtotal: Q")
            descuento = leer_numero("Ingresa el porcentaje de descuento: ")
            nuevo_subtotal = aplicar_descuento(subtotal, descuento)
            porcentaje = leer_numero("Ingresa el porcentaje de propina: ")
            propina = calcular_propina(nuevo_subtotal, porcentaje)
            total = calcular_total(nuevo_subtotal, propina)
            print(f"Subtotal con descuento: Q{nuevo_subtotal:.2f}")
            print(f"Propina: Q{propina:.2f}")
            print(f"Total a pagar: Q{total:.2f}")

        elif opcion == "4":
            print("Gracias por usar la calculadora. ¡Hasta pronto!")
            break

        else:
            print("Opción inválida. Intenta de nuevo.")

# Ejecutar el programa
if __name__ == "__main__":
    main()

 






