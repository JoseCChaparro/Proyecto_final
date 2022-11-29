#producto_id
#nombre_producto
#costo
#en_inventario
#descripcion

import tkinter as tk
from functools import partial
from config.interfaz_config import callback,check_window_open,handle_focus_in,font_1,color_3
import config.interfaz_config as interfaz_config
from operaciones import add_product,update_product,delete_product

def add_product_window(ventana):
    
    check_window_open()
    
    print(interfaz_config.counter_windows)
    if interfaz_config.counter_windows == 0:
        interfaz_config.counter_windows += 1
        add_product_window = tk.Toplevel(ventana)
        add_product_window.protocol("WM_DELETE_WINDOW", partial(callback,add_product_window))
        add_product_window.minsize(300,300)
        add_product_window.title("Añadir producto")

        
        
        id_entry = tk.Entry(add_product_window, font=('Helvetica 12'), fg="grey" )
        id_label = tk.Label(add_product_window, text="Numero del producto:")
        id_label.pack()

        id_entry.insert(tk.END, "Ejemplo: 1234")
        id_entry.pack(pady=5)

        id_entry.bind("<FocusIn>", handle_focus_in)
        


        nombre_label = tk.Label(add_product_window, text="Nombre del producto nuevo:")
        nombre_label.pack()
        nombre_entry = tk.Entry(add_product_window, font=('Helvetica 12'), fg="grey")
        nombre_entry.insert(tk.END, "Ejemplo: Manzana")
        nombre_entry.pack(pady=5)

        nombre_entry.bind("<FocusIn>", handle_focus_in)



        costo_label = tk.Label(add_product_window, text="Costo del producto:")
        costo_label.pack()
        costo_entry = tk.Entry(add_product_window, font=('Helvetica 12'), fg="grey")
        costo_entry.insert(tk.END, "Ejemplo: 30")
        costo_entry.pack(pady=5)

        costo_entry.bind("<FocusIn>", handle_focus_in)
        
        en_inventario_label = tk.Label(add_product_window, text="Cantidad de inventario del producto:")
        en_inventario_label.pack()
        en_inventario_entry = tk.Entry(add_product_window, font=('Helvetica 12'), fg="grey")
        en_inventario_entry.insert(tk.END, "Ejemplo: 160")
        en_inventario_entry.pack(pady=5)

        en_inventario_entry.bind("<FocusIn>", handle_focus_in)


        descripcion_label = tk.Label(add_product_window, text="Descripcion del producto:")
        descripcion_label.pack()
        descripcion_entry = tk.Entry(add_product_window, font=('Helvetica 12'), fg="grey")
        descripcion_entry.insert(tk.END, "Ejemplo: Una manzana")
        descripcion_entry.pack(pady=5)

        descripcion_entry.bind("<FocusIn>", handle_focus_in)
        
        def ok():
            id = int(id_entry.get())
            nombre = str(nombre_entry.get())
            costo = int(costo_entry.get())
            en_inventario = int(en_inventario_entry.get())
            descripcion = str(descripcion_entry.get())


            print("add_product(",id, nombre ,costo  ,en_inventario,descripcion ,")")
            add_product(id, nombre ,costo  ,en_inventario,descripcion )
            




        boton = tk.Button(add_product_window, text="Añadir producto", command=ok )

        boton.pack()

def update_product_window(ventana):
    
    check_window_open()

    if interfaz_config.counter_windows == 0:
        interfaz_config.counter_windows += 1
        edit_product_window = tk.Toplevel(ventana)
        edit_product_window.protocol("WM_DELETE_WINDOW", partial(callback,edit_product_window))
        edit_product_window.minsize(300,300)
        edit_product_window.title("Modificar producto")

        id_entry = tk.Entry(edit_product_window, font=('Helvetica 12'), fg="grey" )
        id_label = tk.Label(edit_product_window, text="Numero del producto a editar:")
        id_label.pack()

        id_entry.insert(tk.END, "Ejemplo: 1234")
        id_entry.pack(pady=5)

        id_entry.bind("<FocusIn>", handle_focus_in)


        nombre_label = tk.Label(edit_product_window, text="Nuevo nombre del producto a editar:")
        nombre_label.pack()
        nombre_entry = tk.Entry(edit_product_window, font=('Helvetica 12'), fg="grey")
        nombre_entry.insert(tk.END, "Ejemplo: Pera")
        nombre_entry.pack(pady=5)

        nombre_entry.bind("<FocusIn>", handle_focus_in)

        costo_label = tk.Label(edit_product_window, text="Nuevo costo del producto a editar:")
        costo_label.pack()
        costo_entry = tk.Entry(edit_product_window, font=('Helvetica 12'), fg="grey")
        costo_entry.insert(tk.END, "Ejemplo: 20")
        costo_entry.pack(pady=5)

        costo_entry.bind("<FocusIn>", handle_focus_in)



        en_inventario_label = tk.Label(edit_product_window, text="Nueva cantidad en inventario del producto a editar:")
        en_inventario_label.pack()
        en_inventario_entry = tk.Entry(edit_product_window, font=('Helvetica 12'), fg="grey")
        en_inventario_entry.insert(tk.END, "Ejemplo: 12")
        en_inventario_entry.pack(pady=5)

        en_inventario_entry.bind("<FocusIn>", handle_focus_in)


        descripcion_label = tk.Label(edit_product_window, text="Nueva descripción del  producto a editar:")
        descripcion_label.pack()
        descripcion_entry = tk.Entry(edit_product_window, font=('Helvetica 12'), fg="grey")
        descripcion_entry.insert(tk.END, "Ejemplo: Una pera")
        descripcion_entry.pack(pady=5)

        descripcion_entry.bind("<FocusIn>", handle_focus_in)


        def ok():
            id = int(id_entry.get())
            nombre = str(nombre_entry.get())
            costo = int(costo_entry.get())
            en_inventario = int(en_inventario_entry.get())
            descripcion = str(descripcion_entry.get())


            print("update_product(",id, nombre ,costo  ,en_inventario,descripcion ,")")
            update_product(id, nombre ,costo  ,en_inventario,descripcion)


        boton = tk.Button(edit_product_window, text="Modificar producto", command=ok )

        boton.pack()


def delete_product_window(ventana):
    
    check_window_open()

    if interfaz_config.counter_windows == 0:
        interfaz_config.counter_windows += 1
        delete_product_window = tk.Toplevel(ventana)
        delete_product_window.protocol("WM_DELETE_WINDOW", partial(callback,delete_product_window))
        delete_product_window.minsize(300,100)
        delete_product_window.title("Eliminar producto")

        id_entry = tk.Entry(delete_product_window, font=('Helvetica 12'), fg="grey" )
        id_label = tk.Label(delete_product_window, text="Numero del producto a eliminar:")
        id_label.pack()

        id_entry.insert(tk.END, "Ejemplo: 1234")
        id_entry.pack(pady=5)

        id_entry.bind("<FocusIn>", handle_focus_in)


        def ok():
            id = int(id_entry.get())
            print("delete_product(",id,")")
            delete_product(id)



        boton = tk.Button(delete_product_window, text="Eliminar producto", command=ok )

        boton.pack()


def create_productos_window(window):
    
    color_b = "gray92"
    ventana = tk.Toplevel(window)
    ventana.title("productos")
    ventana.minsize(300,300)
    ventana.protocol("WM_DELETE_WINDOW", partial(callback,ventana))
    tk.Label(ventana, text="productos").pack()

    add_emp_bt = tk.Button(ventana, text='Añadir producto', font=(font_1, 12), bd=2, command=partial(add_product_window,window) , cursor="hand2", bg=color_b,fg=color_3,width=25).pack( padx=5, pady=10)

    update_product_bt = tk.Button(ventana, text='Modificar producto', font=(font_1, 12), bd=2, command=partial(update_product_window,window), cursor="hand2", bg=color_b,fg=color_3,width=25).pack( padx=5, pady=10)

    delete_product_bt = tk.Button(ventana, text='Borrar producto', font=(font_1, 12), bd=2, command=partial(delete_product_window,window),cursor="hand2", bg=color_b,fg=color_3,width=25).pack(padx=5, pady=10)

