peso = float(input("Ingresa tu peso en kg: "))
altura = float(input("Ingresa tu altura en metros: "))

imc = peso / (altura ** 2)

if imc < 18.5:
    clasificacion = "Bajo peso"
elif imc < 25:
    clasificacion = "Normal"
elif imc < 30:
    clasificacion = "Sobrepeso"
else:
    clasificacion = "Obesidad"

print(f"Tu IMC es {imc:.1f} y tu clasificación es {clasificacion}")