Coordenadas = (14.30097,-90.78816)

lat, lon = Coordenadas

print("Latidud:",lat)
print("Longitud:",lon)

print("\n")

def estadisticas ( lista_numeros):
    minimo = min (lista_numeros)
    maximo = max (lista_numeros)
    promedio = sum(lista_numeros) / len (lista_numeros)
    return ( minimo, maximo, promedio)

numeros = [10,20,30,40,50]
resultado = estadisticas(numeros) 

print("resultado:", resultado)


print("\n")
print("Tuplas como claves de un diccionario")
print("\n")

distancias = {
     ("Guate", "Escuintla"): 58,
     ("Guate", "Antigua"): 45,
     ("Escuintla", "Puerto quetzal"): 30

}

print("Distancia Guate - Escuintla:", distancias[("Guate", "Escuintla")], "km")
print("Distancia Guate - Antigua:", distancias[("Guate", "Antigua")], "km")

"""
Al intentar modificar el diccionario de tuplas con los códig 
anteriores como    Coordenadas["mesero"] = "111"
nos dara un error ya que no se puede modificar la información
de las tuplas.

"""




