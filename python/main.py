"""Prueba: demuestra que las variables del .env se cargaron correctamente."""

from config import ConnectionConfig, ENV_PATH
from conections import Conexion


def main():
    print(f"Leyendo la configuración desde: {ENV_PATH}\n")

    # 1) Cargar y validar la configuración desde el .env.
    try:
        config = ConnectionConfig()
    except ValueError as error:
        print("ERROR de configuración:", error)
        return

    # 2) Mostrar que cada variable se cargó correctamente.
    print("Variables cargadas correctamente:")
    datos = config.resumen()
    for clave in ("nombre", "host", "puerto", "usuario", "contrasena", "base_de_datos"):
        print(f"  {clave:<14} = {datos[clave]}")

    print(
        f"\n  El puerto se guardó como {type(config.puerto).__name__} (valor: {config.puerto})."
    )
    print(
        f"  La contraseña se cargó oculta ({len(config.contrasena)} caracteres)."
    )

    # 3) Usar la configuración para crear la conexión.
    print()
    conexion = Conexion(config)
    conexion.conectar()
    conexion.desconectar()


if __name__ == "__main__":
    main()
