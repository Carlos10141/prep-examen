"""Módulo para cargar y mostrar configuración de la aplicación.

Carga valores desde variables de entorno."""
import os

try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass

app = os.getenv("APP_NAME", "sin nombre")
version = os.getenv("APP_VERSION", "1.0")
debug = os.getenv("DEBUG", "False")


def mostrar_config(app, version, debug):
    if debug == "True":
        print(f"[DEBUG] App: {app} v{version}")
    else:
        print(f"App: {app} v{version}")
    return {"app": app, "version": version, "debug": debug}


config = mostrar_config(app, version, debug)
print(f"Configuración cargada: {len(config)} variables")


def calcular_promedio(notas):
    """Calcula el promedio de una lista de notas numéricas.

    Args:
        notas (list): Lista de números con las notas.

    Returns:
        float: El promedio de las notas, o 0 si la lista está vacía.
    """
    if not notas:
        return 0
    return sum(notas) / len(notas)
