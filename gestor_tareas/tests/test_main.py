"""Pruebas automaticas del gestor de tareas.

Se ejecutan con:  python -m unittest discover -s tests -v
"""

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "src"))

import main  # pyright: ignore[reportMissingImports]


class GestorTareasTest(unittest.TestCase):
    def setUp(self):
        self.tareas = []

    def test_crear_tarea_empieza_pendiente(self):
        tarea = main.crear_tarea(1, "Estudiar")
        self.assertEqual(tarea["id"], 1)
        self.assertEqual(tarea["titulo"], "Estudiar")
        self.assertFalse(tarea["completada"])

    def test_agregar_tarea_asigna_id_incremental(self):
        primera = main.agregar_tarea(self.tareas, "Primera")
        segunda = main.agregar_tarea(self.tareas, "Segunda")
        self.assertEqual(primera["id"], 1)
        self.assertEqual(segunda["id"], 2)
        self.assertEqual(len(self.tareas), 2)

    def test_completar_tarea_existente(self):
        main.agregar_tarea(self.tareas, "Estudiar")
        self.assertTrue(main.completar_tarea(self.tareas, 1))
        self.assertTrue(self.tareas[0]["completada"])

    def test_completar_tarea_inexistente_devuelve_false(self):
        self.assertFalse(main.completar_tarea(self.tareas, 99))

    def test_eliminar_tarea(self):
        main.agregar_tarea(self.tareas, "Estudiar")
        self.assertTrue(main.eliminar_tarea(self.tareas, 1))
        self.assertEqual(len(self.tareas), 0)

    def test_eliminar_tarea_inexistente_devuelve_false(self):
        self.assertFalse(main.eliminar_tarea(self.tareas, 99))

    def test_tareas_pendientes_excluye_completadas(self):
        main.agregar_tarea(self.tareas, "A")
        main.agregar_tarea(self.tareas, "B")
        main.completar_tarea(self.tareas, 1)
        pendientes = main.tareas_pendientes(self.tareas)
        self.assertEqual(len(pendientes), 1)
        self.assertEqual(pendientes[0]["id"], 2)

    def test_formatear_tabla_incluye_los_titulos(self):
        main.agregar_tarea(self.tareas, "Comprar cafe")
        tabla = main.formatear_tabla(self.tareas)
        self.assertIn("Comprar cafe", tabla)

    def test_formatear_tabla_sin_tareas(self):
        self.assertIn("No hay tareas", main.formatear_tabla(self.tareas))


if __name__ == "__main__":
    unittest.main()
