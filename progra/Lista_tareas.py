import json

try:
    with open("tareas.json", "r") as f:
        tareas = json.load(f)
except FileNotFoundError:
    tareas = []

while True:
    print("\n=== Lista de tareas")
    print("1. Agregar tareas ")
    print("2. Ver tareas ")
    print("3. Eliminar tareas ")
    print("4. Marcar como completada ")
    print("5. Salir ")

    opcion = input("Seleccione una opción: ")
    if opcion == "1":
        tarea = input("Nueva tarea: ")
        tareas.append({"task": tarea, "completed": False})
        print("Tarea agregada")
    elif opcion == "2":
        if not tareas:
            print("No hay tareas.")
        else:
            for i, t in enumerate(tareas, 1):
                status = "[X]" if t["completed"] else "[ ]"
                print(f"{i}. {status} {t['task']}")
    elif opcion == "3":
        if not tareas:
            print("No hay tareas para eliminar.")
        else:
            idx = int(input("Número de tarea a eliminar: "))
            if 1 <= idx <= len(tareas):
                tareas.pop(idx - 1)
                print("Tarea eliminada")
            else:
                print("Número inválido.")
    elif opcion == "5":
        if not tareas:
            print("No hay tareas para marcar.")
        else:
            idx = int(input("Número de tarea a marcar como completada: "))
            if 1 <= idx <= len(tareas):
                tareas[idx - 1]["completed"] = True
                print("Tarea marcada como completada")
            else:
                print("Número inválido.")
    elif opcion == "5":
        with open("tareas.json", "w") as f:
            json.dump(tareas, f)
        print("Tareas guardadas. Saliendo...")
        break
    else:
        print("Opción inválida.")
        

