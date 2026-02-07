# Calculadora básica en Python   main()

try:
    numero_1 = int(input("Ingrese un número: "))
except ValueError:
    print("Error: El primer valor ingresado no es un número válido.")
    exit()

try:
    numero_2 = int(input("Ingrese otro número: "))
except ValueError:
    print("Error: El segundo valor ingresado no es un número válido.")
    exit()


print("seleccione una operación")
print("Sus opciones son las siguientes ")
print("Suma: +")
print("Resta: -")
print("Multiplicación: *")
print("Divición: /")
operacion=input("Seleccione el simbolo de la operación")

if operacion=="+":
    print(f"Resultado:{numero_1 + numero_2}")
elif operacion=="-":     
    print(f"Resultado:{numero_1 - numero_2}")
elif operacion=="*":
    print(f"Resultado:{numero_1 * numero_2}")
elif operacion=="/":
    
    if numero_2 == 0:
        print("Error: No se puede dividir por cero.")
    else:
        print(f"Resultado:{numero_1 / numero_2}")
else:
     print("La operacion ingresada no es valida")

print("Gracias por usar la calculadora")




