from tkinter import messagebox
from admin_archivos import exportar_datos, importar_datos

def validar(dni, legajo, apellido_nombre, domicilio):
    return len(dni.get()) > 0 and len(legajo.get()) > 0 and len(apellido_nombre.get()) > 0 and len(domicilio.get()) > 0
    
def vaciar_datos(tabla_emp):
    filas = tabla_emp.get_children() # Obtiene una lista de todas las filas en el Treeview.
    for fila in filas:
        tabla_emp.delete(fila)

def cargar_datos(tabla_emp):
    vaciar_datos(tabla_emp)
    datos_empleados = importar_datos()
    for empleado in datos_empleados:
        dni = empleado["dni"]
        values = [] # Inicializa una lista vacía para almacenar los valores de las columnas.
        for v in empleado.values():
            values.append(v)
        # Inserta una nueva fila en el Treeview con el DNI como identificador y los valores como contenido.
        tabla_emp.insert("", "end", dni, text=dni, values=values)
    
def eliminar_registro(tabla_emp):
    respuesta = messagebox.askquestion("Eliminar", message="¿Estás seguro de eliminar el registro seleccionado?")
    if respuesta == "yes":
        try:
            dni_seleccionado = tabla_emp.selection()[0]
            datos_actualizados = []
            datos_empleados = importar_datos()
            for item in datos_empleados:
                if item["dni"] != dni_seleccionado:
                    datos_actualizados.append(item)  
            exportar_datos(datos_actualizados)
            tabla_emp.delete(dni_seleccionado)
            messagebox.showinfo("Eliminación", "El registro se ha eliminado correctamente.")
            cargar_datos(tabla_emp)
        except IndexError:
            messagebox.showerror("Error", "No se seleccionó ningún registro.")

def agregar_nuevo_registro(ventana_agregar, dni, legajo, apellido_nombre, domicilio, tabla_emp):
    respuesta = messagebox.askquestion("Agregar", message="¿Estás seguro de agregar el nuevo registro?")
    if respuesta == "yes":
        if validar(dni, legajo, apellido_nombre, domicilio):
            encontrado = False
            datos_empleados = importar_datos()
            for empleado in datos_empleados:
                if dni.get() in empleado.values() or legajo.get() in empleado.values():
                    messagebox.showerror("Error", "DNI y legajo deben ser únicos.")
                    encontrado = True
                    break
            if not encontrado:
                nuevo_empleado = {
                    "dni": dni.get(),
                    "legajo": legajo.get(),
                    "apellido_nombre": apellido_nombre.get(),
                    "domicilio": domicilio.get()
                }
                datos_empleados.append(nuevo_empleado)
                exportar_datos(datos_empleados)
                messagebox.showinfo("Creación", "El registro se ha agregado correctamente.")
                ventana_agregar.destroy()  # Cierra la ventana emergente después de agregar
                cargar_datos(tabla_emp)  # Actualiza la tabla de empleados en la ventana principal
        else:
            messagebox.showerror("Error", "No se pueden dejar campos vacíos.")   

def actualizar_registro(ventana_actualizar, dni, legajo, apellido_nombre, domicilio, tabla_emp):
    respuesta = messagebox.askquestion("Actualizar", message="¿Estás seguro de actualizar el registro seleccionado?")
    if respuesta == "yes":
        if validar(dni, legajo, apellido_nombre, domicilio):  
            datos_empleados = importar_datos()
        
            for empleado in datos_empleados:
                if empleado["dni"] == dni.get():
                    empleado["legajo"] = legajo.get()
                    empleado["apellido_nombre"] = apellido_nombre.get()
                    empleado["domicilio"] = domicilio.get()
                    encontrado = True
                    exportar_datos(datos_empleados)
                    messagebox.showinfo("Actualización", "El registro se ha actualizado correctamente.")
                    ventana_actualizar.destroy()
                    cargar_datos(tabla_emp)
            if not encontrado:
                messagebox.showerror("Error", "El DNI no existe.")
        else:
            messagebox.showerror("Error", "No se pueden dejar campos vacíos.")
