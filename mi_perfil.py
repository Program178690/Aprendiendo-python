# Programa: Tarjeta de presentación

print("=== TARJETA DE PRESENTACIÓN ===")  # Explicación de que es el programa

nombre = input("Ingresa tu nombre: ") # con estos inputs se asigna la información requerida 
edad = input("Ingresa tu edad: ")     # a cada variable
ciudad = input("Ingresa tu ciudad: ")
hobby = input("Ingresa tu hobby: ")

print("\n----- TU TARJETA -----")
print(f"Nombre : {nombre}")
print(f"Edad   : {edad} años")  #Estos print toman los datos almacenados en las variables y los imprimen
print(f"Ciudad : {ciudad}")
print(f"Hobby  : {hobby}")
print("----------------------")