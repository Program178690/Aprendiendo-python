"""Programa para calcular el Índice de Masa Corporal (IMC).

El usuario introduce su altura en metros y su peso en kilogramos. Se valida
la entrada para asegurar que sean números positivos y se permite repetir el
cálculo varias veces. Las categorías de IMC siguen los umbrales estándar.
Se aceptan comas como separadores decimales para mayor comodidad.
"""


def pedir_flotante(prompt: str) -> float:
    """Solicita al usuario un número de punto flotante positivo.

    El valor se repite hasta que el usuario ingresa un número válido. Se
    convierten comas a puntos para facilitar la entrada en locales hispanohablantes.
    """

    while True:
        texto = input(prompt).strip().replace(",", ".")
        try:
            valor = float(texto)
            if valor <= 0:
                print("El valor debe ser mayor que cero. Intenta de nuevo.")
                continue
            return valor
        except ValueError:
            print("Entrada inválida. Por favor ingresa un número.")


def calcular_imc():
    """Calcula e imprime el IMC y su clasificación."""

    altura = pedir_flotante("Ingresa tu altura en metros: ")
    peso = pedir_flotante("Ingresa tu peso en kg: ")

    imc = peso / (altura ** 2)
    imc_redondeado = round(imc, 1)

    if imc < 18.5:
        categoria = "Bajo peso"
    elif imc < 25:
        categoria = "Peso normal"
    elif imc < 30:
        categoria = "Sobrepeso"
    else:
        categoria = "Obesidad"

    print(f"\nTu Índice de Masa Corporal (IMC) es: {imc_redondeado}")
    print(f"Clasificación: {categoria}\n")


def main():
    """Bucle principal que permite calcular varios IMC consecutivos."""

    while True:
        calcular_imc()
        otra = input("¿Deseas calcular otro IMC? (s/n): ").strip().lower()
        if otra.startswith("n"):
            print("¡Hasta luego!")
            break


if __name__ == "__main__":
    main()

