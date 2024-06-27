import tkinter as tk
from tkinter import ttk #submódulo de tkinter
from funciones_crud import cargar_datos, eliminar_registro
from funciones_interfaz import abrir_ventana_agregar, abrir_ventana_actualizar, seleccionar, verificar_click_fuera

ventana = tk.Tk()
ventana.title("Plataforma de CRUD")
# Se puede centrar directamente usando funciones para obtener el tamaño de la pantalla
ancho_pantalla = ventana.winfo_screenwidth() # método para obtener el ancho
alto_pantalla = ventana.winfo_screenheight() # método para obtener el alto
ancho_ventana =  700
alto_ventana = 500
posicion_x = (ancho_pantalla - ancho_ventana) // 2 #division entera
posicion_y = (alto_pantalla - alto_ventana) // 2
ventana.geometry(f"{ancho_ventana}x{alto_ventana}+{posicion_x}+{posicion_y}")

ventana.configure(bg='lightblue') # cambiar el color

ventana.resizable(0, 0) #para que el usuario no pueda modificar el tamaño

marco = tk.LabelFrame(ventana, text="Formulario de Gestión de Empleados", font="Courier 12") # le digo donde va a estar
marco.place(x=50, y=50, width=600, height=400)
marco.configure(bg='azure2')

#labels y entries
dni = tk.StringVar()
legajo = tk.StringVar()
apellido_nombre = tk.StringVar()
domicilio = tk.StringVar()

# tabla de lista de empleados
tabla_emp = ttk.Treeview(marco, columns=("DNI", "LEGAJO", "NOMBRE", "DOMICILIO"), show="headings", style="Treeview")
tabla_emp.grid(column=0, row=0, columnspan=7, padx=80, pady=30, sticky="nsew")

# Configurar columnas y encabezados del Treeview
tabla_emp.column("DNI", width=70, anchor=tk.CENTER)
tabla_emp.column("LEGAJO", width=50, anchor=tk.CENTER)
tabla_emp.column("NOMBRE", width=150, anchor=tk.CENTER)
tabla_emp.column("DOMICILIO", width=170, anchor=tk.CENTER)

tabla_emp.heading("DNI", text="DNI")
tabla_emp.heading("LEGAJO", text="LEGAJO")
tabla_emp.heading("NOMBRE", text="NOMBRE")
tabla_emp.heading("DOMICILIO", text="DOMICILIO")

# Configurar estilos para el Treeview
estilo_treeview = ttk.Style()
estilo_treeview.theme_use("default")
estilo_treeview.configure("Treeview", background="white", fieldbackground="white", foreground="black", rowheight=25, font=("Arial", 10))
estilo_treeview.configure("Treeview.Heading", font=("Courier", 10, "bold"))

#Asocia el evento <<TreeviewSelect>> (que se desencadena cuando se selecciona un elemento en la tabla Treeview) con la función seleccionar.
tabla_emp.bind("<<TreeviewSelect>>", lambda event: seleccionar(event, tabla_emp, dni, legajo, apellido_nombre, domicilio, eliminar_btn, modificar_btn))

# botones de acciones
agregar_btn = tk.Button(marco, text="Agregar", command=lambda:abrir_ventana_agregar(marco, tabla_emp))
modificar_btn = tk.Button(marco, text="Actualizar", bd=3, command=lambda:abrir_ventana_actualizar(marco, dni, legajo, apellido_nombre, domicilio, tabla_emp))
modificar_btn.config(state="disabled")
eliminar_btn = tk.Button(marco, text="Eliminar", bd=3, command=lambda:eliminar_registro(tabla_emp))
eliminar_btn.config(state="disabled")

# Alinear botones a la derecha
agregar_btn.grid(column=3, row=1, sticky="e")
modificar_btn.grid(column=4, row=1, sticky="e")
eliminar_btn.grid(column=5, row=1, sticky="e")

cargar_datos(tabla_emp)
# Enlazar el evento de clic en la ventana principal para deseleccionar en el TreeView
ventana.bind("<Button-1>", lambda event: verificar_click_fuera(event, tabla_emp, eliminar_btn, modificar_btn))
ventana.mainloop() 