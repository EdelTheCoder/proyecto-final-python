# 📋 Gestor de Tareas Administrativas

Sistema de gestión de tareas por consola desarrollado en Python. Permite crear, organizar y dar seguimiento a tareas, guardando todo automáticamente en un archivo `.json`.

## ▶️ Cómo ejecutar

```bash
python Entregable_final.py
```

> No requiere instalación de librerías externas. Solo Python 3.x.

## 🧭 Opciones del menú

| # | Función |
|---|---------|
| 1 | Crear tarea |
| 2 | Mostrar todas las tareas |
| 3 | Actualizar tarea |
| 4 | Eliminar tarea |
| 5 | Ordenar tareas por prioridad |
| 6 | Ver tareas próximas a vencer (≤ 3 días) |
| 7 | Marcar tarea como completada |
| 8 | Salir |

## 📝 Datos de cada tarea

- **ID** — generado automáticamente
- **Descripción** y **Responsable**
- **Fecha límite** — formato `YYYY-MM-DD` (no se permiten fechas pasadas)
- **Prioridad** — `Alta`, `Media` o `Baja`
- **Estado** — `Pendiente` o `Completo`

## 💾 Almacenamiento

Los datos se guardan en `tareas_administrativas.json`, que se crea automáticamente al agregar la primera tarea.
