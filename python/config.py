"""Configuración de la conexión a base de datos.

Los datos de conexión se leen desde el archivo .env (con python-dotenv),
nunca se escriben directamente en el código fuente.
"""

import os
from pathlib import Path

from dotenv import load_dotenv

# Ruta absoluta al archivo .env (está un nivel arriba de esta carpeta).
ENV_PATH = Path(__file__).resolve().parent.parent / ".env"

# Carga las variables del .env dentro de las variables de entorno del proceso.
load_dotenv(dotenv_path=ENV_PATH)


class ConnectionConfig:
    """Contiene y valida los datos de conexión leídos desde el .env."""

    def __init__(self):
        self.nombre = self._obtener_obligatoria("DB_NAME")
        self.host = self._obtener_obligatoria("DB_HOST")
        self.puerto = self._convertir_a_entero(
            self._obtener_obligatoria("DB_PORT"), "DB_PORT"
        )
        self.usuario = self._obtener_obligatoria("DB_USER")
        self.contrasena = self._obtener_obligatoria("DB_PASSWORD")
        self.base_de_datos = self._obtener_obligatoria("DB_DATABASE")

    @staticmethod
    def _obtener_obligatoria(nombre_variable):
        """Devuelve el valor de una variable o falla si falta o está vacía."""
        valor = os.getenv(nombre_variable)
        if valor is None or valor.strip() == "":
            raise ValueError(
                f"La variable de entorno '{nombre_variable}' no está configurada "
                f"o está vacía. Revisá tu archivo .env"
            )
        return valor.strip()

    @staticmethod
    def _convertir_a_entero(valor, nombre_variable):
        """Convierte el puerto (texto) a entero, avisando si no es válido."""
        try:
            return int(valor)
        except ValueError:
            raise ValueError(
                f"La variable '{nombre_variable}' debe ser un número entero. "
                f"Valor recibido: '{valor}'"
            )

    def resumen(self, mostrar_password=False):
        """Devuelve los datos cargados (la contraseña queda oculta por defecto)."""
        return {
            "nombre": self.nombre,
            "host": self.host,
            "puerto": self.puerto,
            "usuario": self.usuario,
            "contrasena": self.contrasena if mostrar_password else "********",
            "base_de_datos": self.base_de_datos,
        }

    def __repr__(self):
        return (
            f"ConnectionConfig(nombre={self.nombre!r}, host={self.host!r}, "
            f"puerto={self.puerto!r}, usuario={self.usuario!r}, "
            f"base_de_datos={self.base_de_datos!r})"
        )
