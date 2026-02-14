# Ejemplo con bug
numero = input("Ingresa un número: ")

# Prints de depuración
print(f"DEBUG tipo: {type(numero)}")
print(f"DEBUG valor: [{numero}]")
print(f"DEBUG len: {len(numero)}")

# Bug: se compara string con entero
if numero == 10:
    print("¡Correcto!")
else:
    print("Incorrecto")
