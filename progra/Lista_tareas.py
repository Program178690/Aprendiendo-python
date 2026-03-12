tareas = []

while True:
    print('\n--- Lista de Tareas ---')
    print('1. Agregar tarea')
    print('2. Ver tareas')
    print('3. Eliminar tarea')
    print('4. Marcar/Desmarcar tarea')
    print('5. Salir')

    opcion = input('Opción: ')

    if opcion == "1":
        tarea = input('Nueva tarea: ')
        tareas.append({"nombre": tarea, "completada": False})
        print("✅ Agregada")

    elif opcion == "2":
        if not tareas:
            print("No hay tareas.")
        else:
            for i, t in enumerate(tareas, 1):
                estado = "✔️" if t["completada"] else "❌"
                print(f'{i}. {t["nombre"]} [{estado}]')

    elif opcion == "3":
        idx = int(input("# a eliminar: "))
        if 0 < idx <= len(tareas):
            tareas.pop(idx - 1)
            print("🗑️ Eliminada")
        else:
            print("Número inválido.")

    elif opcion == "4":
        idx = int(input("# a marcar/desmarcar: "))
        if 0 < idx <= len(tareas):
            tareas[idx - 1]["completada"] = not tareas[idx - 1]["completada"]
            estado = "completada" if tareas[idx - 1]["completada"] else "pendiente"
            print(f'🔄 Tarea marcada como {estado}')
        else:
            print("Número inválido.")

    elif opcion == "5":
        break
