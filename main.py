from tkinter import *
from tkinter import ttk, messagebox
import json

# funciones  
def validar():
    return len(dni.get()) > 0 and len(legajo.get()) > 0 and len(nombre.get()) > 0 and len(apellido.get()) > 0
    
def limpiar():
    dni.set("")
    legajo.set("")
    nombre.set("")
    apellido.set("")
    dni_entry.config(state="normal")
    
    
def seleccionar(event):
    seleccion = tabla_estud.selection()
    if seleccion:
        dni_as_id = seleccion[0]
        values = tabla_estud.item(dni_as_id, "values")
        if values:
            dni.set(values[0])
            legajo.set(values[1])
            nombre.set(values[2])
            apellido.set(values[3])
            dni_entry.config(state="readonly")
    
def vaciar_datos():
    #se deben recorrer las filas del treeview y borrar los datos
    filas = tabla_estud.get_children()
    for fila in filas:
        tabla_estud.delete(fila)

def cargar_datos():
    vaciar_datos()
    with open('datos_alumnos.json', 'r') as archivo:
        datos_alumnos = json.load(archivo)
        for item in datos_alumnos:
            dni = item["dni"]
            values = []
            for v in item.values():
                values.append(v)
            tabla_estud.insert("", END, dni, text=dni, values=values)
    
def eliminar():
    respuesta = messagebox.askquestion("Eliminar", message="¿Estás seguro de eliminar el registro seleccionado?")
    if respuesta == "yes":
        try:
            dni = tabla_estud.selection()[0]
            datos_actualizados = []
            with open('datos_alumnos.json', 'r') as archivo:
                datos_alumnos = json.load(archivo)
                for item in datos_alumnos:
                    if item["dni"] != dni:
                        datos_actualizados.append(item)  
            with open('datos_alumnos.json', 'w') as archivo:
                json.dump(datos_actualizados, archivo)
            tabla_estud.delete(dni)
            mensaje_label.config(text="Se ha eliminado el registro correctamente", fg="green")
            cargar_datos()
            limpiar()
        except IndexError:
            mensaje_label.config(text="Seleccione un registro para eliminar", fg="red")

def agregar():
    limpiar()
    respuesta = messagebox.askquestion("Agregar", message="¿Estás seguro de agregar el nuevo registro?")
    if respuesta == "yes":
        if validar():
            # Crear un diccionario con los datos del nuevo alumno
            nuevo_alumno = {
                "dni": dni.get(),
                "legajo": legajo.get(),
                "nombre": nombre.get(),
                "apellido": apellido.get()
            }
            
            # Cargar los datos existentes desde el archivo JSON
            with open('datos_alumnos.json', 'r') as archivo:
                datos_alumnos = json.load(archivo)
            
            # Agregar el nuevo alumno a la lista
            datos_alumnos.append(nuevo_alumno)
            
            # Guardar los datos actualizad|os en el archivo JSON
            with open('datos_alumnos.json', 'w') as archivo:
                json.dump(datos_alumnos, archivo)
                
            mensaje_label.config(text="Registro añadido correctamente", fg="green")
            cargar_datos()
            limpiar()
        else:
            mensaje_label.config(text="Los campos no deben estar vacíos", fg="red")   

def actualizar():
    respuesta = messagebox.askquestion("Actualizar", message="¿Estás seguro de actualizar el registro seleccionado?")
    if respuesta == "yes":
        if validar():  
            # Cargar los datos existentes desde el archivo JSON
            with open('datos_alumnos.json', 'r') as archivo:
                datos_alumnos = json.load(archivo)
            
            for alumno in datos_alumnos:
                if alumno["dni"] == dni.get():
                    alumno["legajo"] = legajo.get()
                    alumno["nombre"] = nombre.get()
                    alumno["apellido"] = apellido.get()
                else:
                    mensaje_label.config(text="El DNI no existe", fg="red")
            # Guardar los datos actualizados en el archivo JSON
            with open('datos_alumnos.json', 'w') as archivo:
                json.dump(datos_alumnos, archivo)
                
            mensaje_label.config(text="Registro actualizado correctamente", fg="green")
            cargar_datos()
            limpiar()
        else:
            mensaje_label.config(text="Los campos no deben estar vacíos", fg="red")

ventana = Tk()
ventana.title("Plataforma de CRUD")
ventana.geometry("600x500") #dimensiones anchoxalto
ventana.resizable(0, 0) #para que el usuario no pueda modificar el tamaño

#vamos a crear un frame, dentro luego los label, botones, etc
marco = LabelFrame(ventana, text="Formulario de Gestión de Estudiantes", font="Courier 10") # ledigo donde va a estar
marco.place(x=50, y=50, width=500, height=400)

#labels y entries
dni = StringVar()
legajo = StringVar()
nombre = StringVar()
apellido = StringVar()

dni_label = Label(marco, text="DNI", font="Courier 10").grid(column=0, row=0, padx=5, pady=5)
dni_entry = Entry(marco, textvariable=dni)
dni_entry.grid(column=1, row=0)

legajo_label = Label(marco, text="Legajo", font="Courier 10").grid(column=0, row=1, padx=5, pady=5)
legajo_entry = Entry(marco, textvariable=legajo)
legajo_entry.grid(column=1, row=1)

nombre_label = Label(marco, text="Nombre", font="Courier 10").grid(column=2, row=0, padx=10, pady=5)
nombre_entry = Entry(marco, textvariable=nombre)
nombre_entry.grid(column=3, row=0)

apellido_label = Label(marco, text="Apellido", font="Courier 10").grid(column=2, row=1, padx=10, pady=5)
apellido_entry = Entry(marco, textvariable=apellido)
apellido_entry.grid(column=3, row=1)

limpiar_btn = Button(marco, text="Limpiar", bd=3, command=lambda:limpiar())
limpiar_btn.grid(column=4, row=1, padx=10)

mensaje_label = Label(marco, text="", fg="green")
mensaje_label.grid(column=0, row=2, columnspan=4, pady=5)

# tabla de lista de estudiantes
tabla_estud = ttk.Treeview(marco)
tabla_estud.grid(column=0, row=3, columnspan=4, pady=10)
tabla_estud["columns"] = ("DNI", "LEGAJO", "NOMBRE", "APELLIDO") #que columnas va a tener
tabla_estud.column("#0", width=0, stretch=NO)
tabla_estud.column("DNI", width=60, anchor=CENTER) #centrado
tabla_estud.column("LEGAJO", width=50, anchor=CENTER)
tabla_estud.column("NOMBRE", width=100, anchor=CENTER)
tabla_estud.column("APELLIDO", width=100, anchor=CENTER)
tabla_estud.heading("#0", text="")
tabla_estud.heading("DNI", text="DNI")
tabla_estud.heading("LEGAJO", text="LEGAJO")
tabla_estud.heading("NOMBRE", text="NOMBRE")
tabla_estud.heading("APELLIDO", text="APELLIDO")
tabla_estud.bind("<<TreeviewSelect>>", seleccionar)

# botones de acciones
agregar_btn = Button(marco, text="Agregar", bd=3, command=lambda:agregar())
agregar_btn.grid(column=1, row=4, padx=5)
modificar_btn = Button(marco, text="Actualizar", bd=3, command=lambda:actualizar())
modificar_btn.grid(column=2, row=4)
eliminar_btn = Button(marco, text="Eliminar", bd=3, command=lambda:eliminar())
eliminar_btn.grid(column=3, row=4)

cargar_datos()
ventana.mainloop()