Datos_personales = {

    "nombre" : "Omar Lopez",
    "edad": "18",
    "ciudad":"Escuintla",
    "lenguaje_favorito":"Español",
    "Correo":"Papa@gmail.com",
    "Pais":"Guatemala"

}

Datos_personales["universidad"] = "San Pablo"
Datos_personales["edad"] = "25"

for clave, valor in Datos_personales.items() :
    print(clave, ":", valor)


if "Correo" in Datos_personales:
    print("La clave 'Correo' existe en el diccionario.")
else :
     print("La clave 'Correo' no existe en el diccionario.")

telefono = Datos_personales.get("telefono")

print("Telefono:", telefono)





