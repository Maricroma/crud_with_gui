import tkinter as tk
from tkinter import Toplevel
from funciones_crud import agregar_nuevo_registro, actualizar_registro
    
def deseleccionar(tabla_emp, eliminar_btn, modificar_btn):
    seleccion = tabla_emp.selection()
    if seleccion:
        tabla_emp.selection_remove(seleccion)
    eliminar_btn.config(state="disabled")
    modificar_btn.config(state="disabled")

def verificar_click_fuera(event, tabla_emp, eliminar_btn, modificar_btn):
    widget = event.widget
    if widget != tabla_emp and widget != eliminar_btn and widget != modificar_btn:
        deseleccionar(tabla_emp, eliminar_btn, modificar_btn)

def habilitar_botones(eliminar_btn, modificar_btn):
    eliminar_btn.config(state="normal")
    modificar_btn.config(state="normal")

def deshabilitar_botones(eliminar_btn, modificar_btn, agregar_btn):
    eliminar_btn.config(state="disabled")
    modificar_btn.config(state="disabled")
    agregar_btn.config(state="normal")


def seleccionar(event, tabla_emp, dni, legajo, apellido_nombre, domicilio, eliminar_btn, modificar_btn):
    seleccion = tabla_emp.selection()
    if seleccion:
        dni_as_id = seleccion[0]
        values = tabla_emp.item(dni_as_id, "values")
        if values:
            dni.set(values[0])
            legajo.set(values[1])
            apellido_nombre.set(values[2])
            domicilio.set(values[3])
            habilitar_botones(eliminar_btn, modificar_btn)
        else:
            deshabilitar_botones(eliminar_btn, modificar_btn)  
                  

def abrir_ventana_agregar(marco, tabla_emp):
    ventana_agregar = Toplevel(marco)  # Crea una nueva ventana emergente
    ventana_agregar.title("Agregar Nuevo Registro")

    ancho_marco = marco.winfo_width() # método para obtener el ancho
    alto_marco = marco.winfo_height() # método para obtener el alto
    posicion_x = marco.winfo_rootx() + ancho_marco // 2 - 200  # Ajusta 200 según el ancho de tu ventana emergente
    posicion_y = marco.winfo_rooty() + alto_marco // 2 - 100   # Ajusta 100 según el alto de tu ventana emergente

    # Configura la posición de la ventana emergente
    ventana_agregar.geometry(f"300x200+{posicion_x}+{posicion_y}")
    ventana_agregar.resizable(0, 0)

    # Labels y Entries para ingresar los datos
    tk.Label(ventana_agregar, text="DNI:").grid(row=0, column=0, padx=10, pady=5)
    dni_entry = tk.Entry(ventana_agregar)
    dni_entry.grid(row=0, column=1)

    tk.Label(ventana_agregar, text="Legajo:").grid(row=1, column=0, padx=10, pady=5)
    legajo_entry = tk.Entry(ventana_agregar)
    legajo_entry.grid(row=1, column=1)

    tk.Label(ventana_agregar, text="Nombre completo:").grid(row=2, column=0, padx=10, pady=5)
    apellido_nombre_entry = tk.Entry(ventana_agregar)
    apellido_nombre_entry.grid(row=2, column=1)

    tk.Label(ventana_agregar, text="Domicilio:").grid(row=3, column=0, padx=10, pady=5)
    domicilio_entry = tk.Entry(ventana_agregar)
    domicilio_entry.grid(row=3, column=1)

    # Botón para agregar el nuevo registro
    tk.Button(ventana_agregar, text="Guardar", command=lambda: agregar_nuevo_registro(ventana_agregar, dni_entry, legajo_entry, apellido_nombre_entry, domicilio_entry, tabla_emp)).grid(row=4, column=0, columnspan=2, pady=15, sticky="e")


def abrir_ventana_actualizar(marco, dni, legajo, apellido_nombre, domicilio, tabla_emp):
    ventana_actualizar = Toplevel(marco)  # Crea una nueva ventana emergente
    ventana_actualizar.title("Actualizar Registro")

    ancho_marco = marco.winfo_width() # método para obtener el ancho
    alto_marco = marco.winfo_height() # método para obtener el alto
    posicion_x = marco.winfo_rootx() + ancho_marco // 2 - 200  # Ajusta 200 según el ancho de tu ventana emergente
    posicion_y = marco.winfo_rooty() + alto_marco // 2 - 100   # Ajusta 100 según el alto de tu ventana emergente

    # Configura la posición de la ventana emergente
    ventana_actualizar.geometry(f"300x200+{posicion_x}+{posicion_y}")
    ventana_actualizar.resizable(0, 0)

    # Labels y Entries para ingresar los datos
    tk.Label(ventana_actualizar, text="DNI:").grid(row=0, column=0, padx=10, pady=5)
    dni_entry = tk.Entry(ventana_actualizar, textvariable=dni)
    dni_entry.grid(row=0, column=1)
    dni_entry.config(state="disabled")

    tk.Label(ventana_actualizar, text="Legajo:").grid(row=1, column=0, padx=10, pady=5)
    legajo_entry = tk.Entry(ventana_actualizar, textvariable=legajo)
    legajo_entry.grid(row=1, column=1)

    tk.Label(ventana_actualizar, text="Nombre completo:").grid(row=2, column=0, padx=10, pady=5)
    apellido_nombre_entry = tk.Entry(ventana_actualizar, textvariable=apellido_nombre)
    apellido_nombre_entry.grid(row=2, column=1)

    tk.Label(ventana_actualizar, text="Domicilio:").grid(row=3, column=0, padx=10, pady=5)
    domicilio_entry = tk.Entry(ventana_actualizar, textvariable=domicilio)
    domicilio_entry.grid(row=3, column=1)

    # Botón para actualizar el registro
    tk.Button(ventana_actualizar, text="Guardar", command=lambda: actualizar_registro(ventana_actualizar, dni, legajo, apellido_nombre, domicilio, tabla_emp)).grid(row=4, column=0, columnspan=2, pady=15, sticky="e")