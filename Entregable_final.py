#Importar librerias
import json
import os
from datetime import datetime
 
ARCHIVO = "tareas_administrativas.json"
 
#Función para cargar tareas
def cargar_tareas():
    if os.path.exists(ARCHIVO):
        with open(ARCHIVO,"r") as archivo:
            return json.load(archivo)
    return []
 
#Función para guardar tareas
def guardar_tarea(tareas):
    with open(ARCHIVO, "w") as archivo:
        json.dump(tareas, archivo, indent=4)
 
#Función para validar prioridad
def validar_prioridad(prioridad):
    prioridades_validas = ["Alta","Media","Baja"]
    if prioridad.capitalize() in prioridades_validas:
        return prioridad.capitalize()
    else:
        print("Prioridad invalida. Use Alta, Media o Baja")
        return None
 
#Función para crear ID
def generar_id(tareas):
    if not tareas:
        return 1
    return max(t["id"] for t in tareas) + 1
 
#Función para validar fecha
def validar_fecha(fecha):
    try:
        fecha_agregada = datetime.strptime(fecha, "%Y-%m-%d").date()
 
        if fecha_agregada < datetime.now().date():
            print("Solo se permite fecha(s) actual o posteriores")
            return None
        return fecha_agregada.strftime("%Y-%m-%d")
    except ValueError:
        print("Formato inválido. Ingrese YYYY-MM-DD")
        return None
 
#Función de crear tarea
def crear_tarea(tareas):
    descripcion = input("Descripción: ")
    responsable = input("Responsable: ")
 
    while True:
        fecha = input("Fecha limite(YYYY-MM-DD): ")
        fecha_validada = validar_fecha(fecha)
        if fecha_validada:
            break
 
    while True:
        prioridad = input("Prioridad(Alta/Media/Baja): ")
        prioridad_validada = validar_prioridad(prioridad)
        if prioridad_validada:
            break
 
    tarea = {
        "id":generar_id(tareas),
        "descripcion": descripcion,
        "fecha_limite":fecha_validada,
        "responsable": responsable,
        "prioridad": prioridad_validada,
        "estado":"Pendiente"
        }
 
    tareas.append(tarea)
    guardar_tarea(tareas)
    print("Tarea generada exitosamente")
 
#Función visualizar tareas
def visualizar_tareas(tareas):
 
    if not tareas:
        print("No hay tareas registradas")
        return
 
    fecha_actual = datetime.now().date()
 
    for tarea in tareas:
        fecha_tarea = datetime.strptime(tarea["fecha_limite"], "%Y-%m-%d").date()
        dias_restantes = (fecha_tarea - fecha_actual).days
 
        estado_auto = ""
 
        if dias_restantes < 0:
            estado_auto = "Tarea vencida."
        elif dias_restantes <= 3:
            estado_auto = "Proximo a vencer."
 
        print("-------------------------------")
        print(f"ID: {tarea['id']}")
        print(f"Descripción: {tarea['descripcion']}")
        print(f"Fecha Limite: {tarea['fecha_limite']} ({dias_restantes} dias) {estado_auto}")
        print(f"Responsable: {tarea['responsable']}")
        print(f"Prioridad: {tarea['prioridad']}")
        print(f"Estado: {tarea['estado']}")
        print("-------------------------------")
 
#Mejora 1: ordenar tareas por prioridad
def ordenar_por_prioridad(tareas):
 
    orden_prioridad = {"Alta":1,"Media":2,"Baja":3}
 
    tareas_ordenadas = sorted(tareas, key=lambda t: orden_prioridad.get(t["prioridad"],4))
 
    visualizar_tareas(tareas_ordenadas)
 
#Mejora 2: detectar tareas proximas a vencer
def tareas_proximas(tareas):
 
    fecha_actual = datetime.now().date()
 
    print("Tareas próximas a vencer:")
 
    for tarea in tareas:
 
        fecha_tarea = datetime.strptime(tarea["fecha_limite"], "%Y-%m-%d").date()
        dias_restantes = (fecha_tarea - fecha_actual).days
 
        if 0 <= dias_restantes <= 3 and tarea["estado"] != "Completo":
 
            print("-------------------------------")
            print(f"ID: {tarea['id']}")
            print(f"Descripción: {tarea['descripcion']}")
            print(f"Fecha Limite: {tarea['fecha_limite']}")
            print(f"Días restantes: {dias_restantes}")
            print("-------------------------------")
 
#Mejora 3: marcar tarea como completada
def marcar_completada(tareas):
 
    try:
        id_tarea = int(input("Ingrese el ID de la tarea completada: "))
    except ValueError:
        print("ID inválido")
        return
 
    for tarea in tareas:
 
        if tarea["id"] == id_tarea:
 
            tarea["estado"] = "Completo"
            guardar_tarea(tareas)
 
            print("Tarea marcada como completada.")
            return
 
    print("Tarea no encontrada.")
 
#Actualizar tarea
def actualizar_tarea(tareas):
 
    try:
        id_tarea = int(input("Ingresa el ID de la tarea: "))
    except ValueError:
        print("ID inválido")
        return
 
    for tarea in tareas:
 
        if tarea["id"] == id_tarea:
 
            tarea["descripcion"] = input("Nueva descripción: ")
            tarea["responsable"] = input("Nuevo Responsable: ")
 
            while True:
                nueva_fecha = input("Nueva fecha limite(YYYY-MM-DD): ")
                fecha_validada = validar_fecha(nueva_fecha)
                if fecha_validada:
                    tarea["fecha_limite"] = fecha_validada
                    break
 
            while True:
                nueva_prioridad = input("Nueva prioridad(Alta/Media/Baja): ")
                prioridad_validada = validar_prioridad(nueva_prioridad)
                if prioridad_validada:
                    tarea["prioridad"] = prioridad_validada
                    break
 
            tarea["estado"] = input("Estado(Pendiente/Completo): ")
 
            guardar_tarea(tareas)
            print("Tarea actualizada.")
            return
 
    print("Tarea no encontrada.")
 
#Función Eliminar tarea
def eliminar_tarea(tareas):
 
    try:
        id_tarea = int(input("Ingresa el ID a eliminar: "))
    except ValueError:
        print("ID inválido.")
        return
 
    for tarea in tareas:
 
        if tarea["id"] == id_tarea:
 
            tareas.remove(tarea)
            guardar_tarea(tareas)
            print("Tarea eliminada.")
            return
 
    print("Tarea no encontrada.")
 
#Menú
def menu():
 
    tareas = cargar_tareas()
 
    while True:
 
        print("----- Gestor de tareas -----")
        print("1. Crear tarea")
        print("2. Mostrar tareas")
        print("3. Actualizar tarea")
        print("4. Eliminar tarea")
        print("5. Ordenar tareas por prioridad")
        print("6. Ver tareas próximas a vencer")
        print("7. Marcar tarea como completada")
        print("8. Salir")
 
        opcion = input("Selecciona una opción: ")
 
        if opcion == "1":
            crear_tarea(tareas)
 
        elif opcion == "2":
            visualizar_tareas(tareas)
 
        elif opcion == "3":
            actualizar_tarea(tareas)
 
        elif opcion == "4":
            eliminar_tarea(tareas)
 
        elif opcion == "5":
            ordenar_por_prioridad(tareas)
 
        elif opcion == "6":
            tareas_proximas(tareas)
 
        elif opcion == "7":
            marcar_completada(tareas)
 
        elif opcion == "8":
            break
 
        else:
            print("Opción invalida.")
 
 
if __name__ == "__main__":
    menu()
