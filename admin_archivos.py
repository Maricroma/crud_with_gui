import json
import os
import sys

def obtener_ruta_datos():
    """
    Devuelve la ruta absoluta al archivo datos_empleados.json.
    """
    if getattr(sys, 'frozen', False):  # Si está ejecutando como un ejecutable PyInstaller
        base_path = sys._MEIPASS
    else:
        base_path = os.path.dirname(__file__)
    
    return os.path.join(base_path, "datos_empleados.json")

# funcion que trae los datos del json
def importar_datos():
    try:
        with open(obtener_ruta_datos(), "r") as archivo:
            datos_empleados = json.load(archivo)
    except (json.decoder.JSONDecodeError, FileNotFoundError):
        datos_empleados = []
    return datos_empleados

#función que actualiza los datos en el json
def exportar_datos(empleados):
    try:
        with open(obtener_ruta_datos(), "w") as archivo:
            json.dump(empleados, archivo)
    except IOError as e:
        print(f"Error al escribir en el archivo: {e}")    