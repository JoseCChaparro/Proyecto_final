#proveedor_id
#nombre_provedor


import tkinter as tk
from functools import partial
from config.interfaz_config import callback,check_window_open,handle_focus_in,font_1,color_3
import config.interfaz_config as interfaz_config
from operaciones import add_supp, update_supp, delete_supp

def add_proveedor_window(ventana):
    
    check_window_open()
    
    print(interfaz_config.counter_windows)
    if interfaz_config.counter_windows == 0:
        interfaz_config.counter_windows += 1
        add_proveedor_window = tk.Toplevel(ventana)
        add_proveedor_window.protocol("WM_DELETE_WINDOW", partial(callback,add_proveedor_window))
        add_proveedor_window.minsize(300,150)
        add_proveedor_window.title("Añadir proveedor")

        
        
        id_entry = tk.Entry(add_proveedor_window, font=('Helvetica 12'), fg="grey" )
        id_label = tk.Label(add_proveedor_window, text="Numero del proveedor:")
        id_label.pack()

        id_entry.insert(tk.END, "Ejemplo: 1234")
        id_entry.pack(pady=5)

        id_entry.bind("<FocusIn>", handle_focus_in)
        


        nombre_label = tk.Label(add_proveedor_window, text="Nombre del proveedor nuevo:")
        nombre_label.pack()
        nombre_entry = tk.Entry(add_proveedor_window, font=('Helvetica 12'), fg="grey")
        nombre_entry.insert(tk.END, "Ejemplo: Juan")
        nombre_entry.pack(pady=5)

        nombre_entry.bind("<FocusIn>", handle_focus_in)
        

        def ok():
            id = int(id_entry.get())
            nombre = str(nombre_entry.get())


            print("add_supp(",id, nombre,")")
            add_supp(id, nombre)
            




        boton = tk.Button(add_proveedor_window, text="Añadir proveedor", command=ok )

        boton.pack()

def update_proveedor_window(ventana):
    
    check_window_open()

    if interfaz_config.counter_windows == 0:
        interfaz_config.counter_windows += 1
        edit_proveedor_window = tk.Toplevel(ventana)
        edit_proveedor_window.protocol("WM_DELETE_WINDOW", partial(callback,edit_proveedor_window))
        edit_proveedor_window.minsize(300,150)
        edit_proveedor_window.title("Modificar proveedor")

        id_entry = tk.Entry(edit_proveedor_window, font=('Helvetica 12'), fg="grey" )
        id_label = tk.Label(edit_proveedor_window, text="Numero del proveedor a editar:")
        id_label.pack()

        id_entry.insert(tk.END, "Ejemplo: 1234")
        id_entry.pack(pady=5)

        id_entry.bind("<FocusIn>", handle_focus_in)


        nombre_label = tk.Label(edit_proveedor_window, text="Nuevo nombre del proveedor a editar:")
        nombre_label.pack()
        nombre_entry = tk.Entry(edit_proveedor_window, font=('Helvetica 12'), fg="grey")
        nombre_entry.insert(tk.END, "Ejemplo: Carlos")
        nombre_entry.pack(pady=5)

        nombre_entry.bind("<FocusIn>", handle_focus_in)


        def ok():
            id = int(id_entry.get())
            nombre = str(nombre_entry.get())
            

            print("update_supp(",id, nombre ,")")
            update_supp(id, nombre)


        boton = tk.Button(edit_proveedor_window, text="Modificar proveedor", command=ok )

        boton.pack()


def delete_proveedor_window(ventana):
    
    check_window_open()

    if interfaz_config.counter_windows == 0:
        interfaz_config.counter_windows += 1
        delete_proveedor_window = tk.Toplevel(ventana)
        delete_proveedor_window.protocol("WM_DELETE_WINDOW", partial(callback,delete_proveedor_window))
        delete_proveedor_window.minsize(300,100)
        delete_proveedor_window.title("Eliminar proveedor")

        id_entry = tk.Entry(delete_proveedor_window, font=('Helvetica 12'), fg="grey" )
        id_label = tk.Label(delete_proveedor_window, text="Numero del proveedor a eliminar:")
        id_label.pack()

        id_entry.insert(tk.END, "Ejemplo: 1234")
        id_entry.pack(pady=5)

        id_entry.bind("<FocusIn>", handle_focus_in)


        def ok():
            id = int(id_entry.get())
            print("delete_supp(",id,")")
            delete_supp(id)



        boton = tk.Button(delete_proveedor_window, text="Eliminar proveedor", command=ok )

        boton.pack()


def create_proveedores_window(window):
    
    color_b = "gray92"
    ventana = tk.Toplevel(window)
    ventana.title("proveedores")
    ventana.minsize(300,300)
    ventana.protocol("WM_DELETE_WINDOW", partial(callback,ventana))
    tk.Label(ventana, text="proveedores").pack()

    add_proveedor_bt = tk.Button(ventana, text='Añadir proveedor', font=(font_1, 12), bd=2, command=partial(add_proveedor_window,window) , cursor="hand2", bg=color_b,fg=color_3,width=25).pack( padx=5, pady=10)

    update_proveedor_bt = tk.Button(ventana, text='Modificar proveedor', font=(font_1, 12), bd=2, command=partial(update_proveedor_window,window), cursor="hand2", bg=color_b,fg=color_3,width=25).pack( padx=5, pady=10)

    delete_proveedor_bt = tk.Button(ventana, text='Borrar proveedor', font=(font_1, 12), bd=2, command=partial(delete_proveedor_window,window),cursor="hand2", bg=color_b,fg=color_3,width=25).pack(padx=5, pady=10)

