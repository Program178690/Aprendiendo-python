import time

for Num in range(1, 13):
    print(f"\n=== Tabla del {Num} ===")
    for i in range(1, 13):
        resultado = Num * i
        print(f"{Num} x {i:2d} = {resultado:2d}")
        time.sleep(0.05)  # Pequeño retraso para efecto animado

