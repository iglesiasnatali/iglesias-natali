"""Manejo de la conexión a la base de datos.

Recibe un objeto ConnectionConfig con los datos ya cargados y validados,
en lugar de tener las credenciales escritas directamente en el código.
"""

from config import ConnectionConfig


class Conexion:
    """Representa una conexión a la base de datos."""

    def __init__(self, config):
        if not isinstance(config, ConnectionConfig):
            raise TypeError(
                "La conexión necesita un objeto ConnectionConfig, "
                f"se recibió {type(config).__name__}"
            )
        self.config = config
        self.conectada = False

    def conectar(self):
        # Acá iría la conexión real (por ejemplo con psycopg2 o mysql.connector).
        # Los datos se toman del objeto de configuración, no de valores fijos.
        print(
            f"Conectando a la base '{self.config.base_de_datos}' en "
            f"{self.config.host}:{self.config.puerto} "
            f"como usuario '{self.config.usuario}'..."
        )
        self.conectada = True
        return self.conectada

    def desconectar(self):
        self.conectada = False
        print("Conexión cerrada.")
