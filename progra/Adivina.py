import random

numero_secreto = random.randint(1, 100)
intentos = 0
max_intentos = 10


while intentos < max_intentos:
    numero_adivinado = int(input("Adivina un número (1-100): "))
    intentos += 1
    
    if numero_adivinado < numero_secreto:
        print("Más alto")
    elif numero_adivinado > numero_secreto:
        print("Más bajo")
    else:
        print(f"¡Correcto en {intentos} intentos!")
        break
else:
    print(f"¡Has fallado! El número secreto era {numero_secreto}")