"""Gestor de tareas de consola.

El proyecto usa tres librerias externas:

- rich: imprime titulos y paneles con formato en la consola.
- tabulate: genera la tabla de tareas.
- colorama: colorea los mensajes de la consola.

La logica principal (agregar, completar, eliminar y filtrar tareas) esta en
funciones puras para poder probarlas de forma sencilla con unittest.
"""

from colorama import Fore, Style
from colorama import init as colorama_init
from rich.console import Console
from rich.panel import Panel
from tabulate import tabulate

colorama_init(autoreset=True)

console = Console(safe_box=True)


def crear_tarea(id_tarea, titulo):
    """Crea una tarea nueva (sin completar)."""
    return {"id": id_tarea, "titulo": titulo, "completada": False}


def agregar_tarea(tareas, titulo):
    """Agrega una tarea a la lista y devuelve la tarea creada."""
    nuevo_id = 1 if not tareas else max(t["id"] for t in tareas) + 1
    tarea = crear_tarea(nuevo_id, titulo)
    tareas.append(tarea)
    return tarea


def buscar_tarea(tareas, id_tarea):
    """Devuelve la tarea con ese id, o None si no existe."""
    for tarea in tareas:
        if tarea["id"] == id_tarea:
            return tarea
    return None


def completar_tarea(tareas, id_tarea):
    """Marca una tarea como completada. Devuelve True si la encontro."""
    tarea = buscar_tarea(tareas, id_tarea)
    if tarea is None:
        return False
    tarea["completada"] = True
    return True


def eliminar_tarea(tareas, id_tarea):
    """Elimina una tarea. Devuelve True si la encontro."""
    tarea = buscar_tarea(tareas, id_tarea)
    if tarea is None:
        return False
    tareas.remove(tarea)
    return True


def tareas_pendientes(tareas):
    """Devuelve solo las tareas que todavia no estan completadas."""
    return [t for t in tareas if not t["completada"]]


def formatear_tabla(tareas):
    """Construye la tabla de tareas usando la libreria tabulate."""
    if not tareas:
        return "No hay tareas cargadas."
    filas = [
        [t["id"], t["titulo"], "SI" if t["completada"] else "NO"]
        for t in tareas
    ]
    return tabulate(filas, headers=["ID", "Tarea", "Completada"], tablefmt="grid")


def mostrar_tareas(tareas):
    """Muestra la tabla de tareas (rich) y el total pendiente (colorama)."""
    console.print(Panel.fit(formatear_tabla(tareas), title="Gestor de Tareas"))
    pendientes = len(tareas_pendientes(tareas))
    color = Fore.GREEN if pendientes else Fore.YELLOW
    print(color + "Tareas pendientes: %d" % pendientes + Style.RESET_ALL)


def main():
    console.print(Panel.fit("Gestor de Tareas", style="bold cyan"))

    tareas = []
    agregar_tarea(tareas, "Estudiar para la prueba")
    agregar_tarea(tareas, "Completar el TP de Python")
    agregar_tarea(tareas, "Subir el trabajo a GitHub")
    completar_tarea(tareas, 2)

    mostrar_tareas(tareas)

    console.print("\n[bold]Agregando una tarea nueva...[/bold]")
    nueva = agregar_tarea(tareas, "Repasar requirements.txt")
    print(Fore.CYAN + "  + Tarea #%d: %s" % (nueva["id"], nueva["titulo"]) + Style.RESET_ALL)

    mostrar_tareas(tareas)


if __name__ == "__main__":
    main()
