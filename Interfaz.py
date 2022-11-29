import tkinter as tk
from tkinter import font as tkfont
from tkinter import ttk

from config.interfaz_config import *
import os
from tkinter import messagebox
from PIL import ImageTk, Image

from functools import partial

from interfaces.employees import add_emp_window, update_emp_window, delete_emp_window, search_emp_window, noemp_depto_window
from interfaces.productos import add_product_window, update_product_window, delete_product_window
from interfaces.proveedores import add_proveedor_window, update_proveedor_window, delete_proveedor_window
from interfaces.productos_ventas import read_sale_window
from interfaces.productos_compras import read_purchase_window

from operaciones import conexion, read_products,add_sale,add_product_sale,add_produc_purchase,add_purchase
import datetime as dt

class SampleApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.minsize(600, 800)
        
        conexion(self)

        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic",)

        self.photo = tk.PhotoImage(file = os.getcwd()+"\\images\\uach.png")
        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        

        self.frames = {}
        for F in (StartPage, Employees, Productos, Ventas, Compras, Proveedores,Productos_Ventas, Productos_Compras):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()


class StartPage(tk.Frame):
    
    def __init__(self, parent, controller):

        self.b_width = 15
        self.controller = controller

        ##INICIA LO QUE METI
        #-----------------------------------------------------------------------------------
        tk.Frame.__init__(self, parent,bg=color_1)
        

        # Botones frame
        frame_2 = tk.Frame(self, bg = color_2)
        frame_2.place(x=0, y=0, width=200, height = 100)
        frame_2.pack(fill =tk.BOTH,side=tk.BOTTOM,expand=False, padx=5, pady=5,anchor=tk.S)

        mini_frame_1 = tk.Frame(frame_2, bg = color_2)
        mini_frame_1.pack(padx=10,pady=10, side=tk.LEFT, fill=tk.BOTH, expand=True)

        mini_frame_2 = tk.Frame(frame_2, bg = color_2)
        mini_frame_2.pack(padx=10,pady=10,side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Datos del equipo
        titulo_consulta2 = tk.Label(self, text="Proyecto Final", bg = color_1, fg = color_4, font='Helvetica 18 bold')
        titulo_consulta2.pack()
        titulo = tk.Label(self, text="Programa Abarrotes Doña Chela\n En este programa se simula\n un sistema de abarrotes el cual \ntrabaja sobre una base de datos MongoDB", bg = color_1, fg = color_4, font='Helvetica 16')
        titulo.pack()
        titulo_consulta = tk.Label(self, text="Integrantes", bg = color_1, fg = color_4, font='Helvetica 18 bold')
        titulo_consulta.pack()
        integrantes = tk.Label(self, text="José Carlos Chaparro Morales - 329613\nJuan Luis Del Valle Sotelo - 338912\nOmar Alonso Escápita Chacón - 338912", bg = color_1, fg = color_4, font='Helvetica 16')
        integrantes.pack()
        resultado_sulta = tk.Label(self, text="Docente", bg = color_1, fg = color_4, font='Helvetica 18 bold')
        resultado_sulta.pack()
        profe = tk.Label(self, text="M. A. José Saúl De Lira Miramontes", bg = color_1, fg = color_4, font='Helvetica 16')
        profe.pack()

        label1 = tk.Label(self, image = controller.photo)
        label1.pack(pady=40)

        #-----------------------------------------------------------------------------------
        ##TERMINA LO QUE METI
        employees_window = tk.Button(mini_frame_1, text='Empleados', font=(font_1, 12), bd=2, command=lambda: controller.show_frame("Employees") , cursor="hand2", bg=color_b,fg=color_3,width=self.b_width).pack( padx=5, pady=5, side=tk.TOP, anchor=tk.CENTER)

        productos_window = tk.Button(mini_frame_1, text='Productos', font=(font_1, 12), bd=2, command=lambda: controller.show_frame("Productos") , cursor="hand2", bg=color_b,fg=color_3,width=self.b_width).pack( padx=5, pady=5, side=tk.TOP, anchor=tk.CENTER)

        ventas_window = tk.Button(mini_frame_2, text='Ventas', font=(font_1, 12), bd=2, command=lambda: controller.show_frame("Ventas"), cursor="hand2", bg=color_b,fg=color_3,width=self.b_width).pack( padx=5, pady=5, side=tk.TOP, anchor=tk.CENTER)

        proveedores_window = tk.Button(mini_frame_1, text='Proveedores', font=(font_1, 12), bd=2, command=lambda: controller.show_frame("Proveedores") , cursor="hand2", bg=color_b,fg=color_3,width=self.b_width).pack( padx=5, pady=5, side=tk.TOP, anchor=tk.CENTER)

        compras_window = tk.Button(mini_frame_2, text='Compras', font=(font_1, 12), bd=2, command=lambda: controller.show_frame("Compras") , cursor="hand2", bg=color_b,fg=color_3,width=self.b_width).pack( padx=5, pady=5, side=tk.TOP, anchor=tk.CENTER)

        productos_compras_window = tk.Button(mini_frame_2, text='Productos-compras', font=(font_1, 12), bd=2, command=lambda: controller.show_frame("Productos_Compras") , cursor="hand2", bg=color_b,fg=color_3,width=self.b_width).pack( padx=5, pady=5, side=tk.TOP, anchor=tk.CENTER)

        productos_ventas_window = tk.Button(mini_frame_2, text='Productos-Ventas', font=(font_1, 12), bd=2, command=lambda: controller.show_frame("Productos_Ventas") , cursor="hand2", bg=color_b,fg=color_3,width=self.b_width).pack( padx=5, pady=5, side=tk.TOP, anchor=tk.CENTER)




class Employees(tk.Frame):
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg=color_1)
        self.controller = controller
        label = tk.Label(self, text="Operaciones con Empleados", font=controller.title_font, bg=color_1, fg=color_4)
        label.pack(side=tk.TOP, fill="x", pady=10)
        

        add_emp_bt = tk.Button(self, text='Añadir empleado', font=(font_1, 12), bd=2, command=partial(add_emp_window,controller) , cursor="hand2", bg=color_b,fg=color_3,width=25).pack( padx=5, pady=5)

        view_bt = tk.Button(self, text='Modificar empleado', font=(font_1, 12), bd=2, command=partial(update_emp_window,controller), cursor="hand2", bg=color_b,fg=color_3,width=25).pack(   padx=5, pady=5)

        delete_empn_bt = tk.Button(self, text='Borrar empleado', font=(font_1, 12), bd=2, command=partial(delete_emp_window,controller),cursor="hand2", bg=color_b,fg=color_3,width=25).pack(padx=5, pady=5)

        #get_no_emp_bt = tk.Button(self, text='No. Empleados', font=(font_1, 12), bd=2, command=partial(noemp_depto_window,controller), cursor="hand2", bg=color_b,fg=color_3,anchor=tk.CENTER,width=25).pack(padx=5, pady=5)

        #buscar_emp_bt = tk.Button(self, text='Buscar un empleado', font=(font_1, 12), bd=2, command=partial(search_emp_window,controller), cursor="hand2", bg=color_b,fg=color_3,anchor=tk.CENTER,width=25).pack(padx=5, pady=5)

        button = tk.Button(self, text="Atras",font=(font_1, 12),command=lambda: controller.show_frame("StartPage"))
        button.pack()


class Productos(tk.Frame):
    
        def __init__(self, parent, controller):
            tk.Frame.__init__(self, parent, bg=color_1)
            self.controller = controller
            label = tk.Label(self, text="Operaciones con Productos", font=controller.title_font, bg=color_1, fg=color_4)
            label.pack(side="top", fill="x", pady=10)

            add_product_bt = tk.Button(self, text='Añadir producto', font=(font_1, 12), bd=2, command=partial(add_product_window,controller) , cursor="hand2", bg=color_b,fg=color_3,width=25).pack( padx=5, pady=5)

            update_product_bt = tk.Button(self, text='Modificar producto', font=(font_1, 12), bd=2, command=partial(update_product_window,controller), cursor="hand2", bg=color_b,fg=color_3,width=25).pack( padx=5, pady=5)

            delete_product_bt = tk.Button(self, text='Borrar producto', font=(font_1, 12), bd=2, command=partial(delete_product_window,controller),cursor="hand2",    bg=color_b,fg=color_3,width=25).pack(padx=5, pady=5)

            button = tk.Button(self, text="Atras",font=(font_1, 12),command=lambda: controller.show_frame("StartPage"))
            button.pack()
            
class Proveedores(tk.Frame):
    
        def __init__(self, parent, controller):
            tk.Frame.__init__(self, parent, bg=color_1)
            self.controller = controller
            label = tk.Label(self, text="Operaciones con Proveedores", font=controller.title_font, bg=color_1, fg=color_4)
            label.pack(side="top", fill="x", pady=10)

            add_proveedor_bt = tk.Button(self, text='Añadir proveedor', font=(font_1, 12), bd=2, command=partial(add_proveedor_window,controller) , cursor="hand2", bg=color_b,fg=color_3,width=25).pack( padx=5, pady=5)

            update_proveedor_bt = tk.Button(self, text='Modificar proveedor', font=(font_1, 12), bd=2, command=partial(update_proveedor_window,controller), cursor="hand2", bg=color_b,fg=color_3,width=25).pack( padx=5, pady=5)

            delete_proveedor_bt = tk.Button(self, text='Borrar proveedor', font=(font_1, 12), bd=2, command=partial(delete_proveedor_window,controller),cursor="hand2", bg=color_b,fg=color_3,width=25).pack(padx=5, pady=5)

            button = tk.Button(self, text="Atras",font=(font_1, 12),command=lambda: controller.show_frame("StartPage"))
            button.pack()

class Productos_Ventas(tk.Frame):
    
        def __init__(self, parent, controller):
            tk.Frame.__init__(self, parent, bg=color_1)
            self.controller = controller
            label = tk.Label(self, text="Productos en ventas", font=controller.title_font, bg=color_1, fg=color_4)
            label.pack(side="top", fill="x", pady=10)

            consultar_venta_bt = tk.Button(self, text='Consultar venta', font=(font_1, 12), bd=2, command=partial(read_sale_window,controller) , cursor="hand2", bg=color_b,fg=color_3,width=25)
            consultar_venta_bt.pack( padx=5, pady=5)

            button = tk.Button(self, text="Atras",font=(font_1, 12),command=lambda: controller.show_frame("StartPage"))
            button.pack() 

class Productos_Compras(tk.Frame):
    
        def __init__(self, parent, controller):
            tk.Frame.__init__(self, parent, bg=color_1)
            self.controller = controller
            label = tk.Label(self, text="Productos en compras", font=controller.title_font, bg=color_1, fg=color_4)
            label.pack(side="top", fill="x", pady=10)

            consultar_compra_bt = tk.Button(self, text='Consultar compra', font=(font_1, 12), bd=2, command=partial(read_purchase_window,controller) , cursor="hand2", bg=color_b,fg=color_3,width=25)
            consultar_compra_bt.pack( padx=5, pady=5)

            button = tk.Button(self, text="Atras",font=(font_1, 12),command=lambda: controller.show_frame("StartPage"))
            button.pack()  

class Ventas(tk.Frame):
    
        def __init__(self, parent, controller):
            tk.Frame.__init__(self, parent,bg=color_1, padx=15, pady=15)
            
            self.controller = controller
            global arreglo 
            arreglo = []
            global ids
            global total
            total = 0

            label = tk.Label(self, text="Operaciones con Ventas", font=controller.title_font, bg=color_1, fg=color_4)
            label.pack(side="top", fill="x", pady=10)

            added_products_frame  = tk.Frame(self, bg = color_2)
            added_products_frame.place(x=0, y=0, width=50, height = 50)
            added_products_frame.pack(fill =tk.BOTH,side=tk.TOP,expand=True, padx=5, pady=5,anchor=tk.S)

            listbox1_label = tk.Label(added_products_frame, text="Productos añadidos", font=(font_1, 18), bg=color_2, fg=color_3)
            listbox1_label.pack(side=tk.TOP, fill=tk.X, padx=5, pady=5)

            scrollbar1 = tk.Scrollbar(added_products_frame)
            listbox1 = tk.Listbox(added_products_frame,width=30, height=0)
            scrollbar1.config(command=listbox1.yview)
            listbox1.pack(expand=1, fill="both", side=tk.LEFT)
            scrollbar1.pack(side=tk.LEFT, fill=tk.Y)
            listbox1.config(font=(font_1, 18),bg = "#E5CAEE", yscrollcommand=scrollbar1.set)



            list_products_frame  = tk.Frame(self, bg = color_2)
            list_products_frame.place(x=0, y=0, width=50, height = 50)
            list_products_frame.pack(fill =tk.BOTH,side=tk.TOP,expand=True, padx=5, pady=5,anchor=tk.S)

            listbox2_label = tk.Label(list_products_frame, text="Productos disponibles", font=(font_1, 18), bg=color_2, fg=color_3)
            listbox2_label.pack(side=tk.TOP, fill=tk.X, padx=5, pady=5)

            scrollbar2 = tk.Scrollbar(list_products_frame)
            listbox2 = tk.Listbox(list_products_frame,width=30, height=3)
            scrollbar2.pack(side=tk.RIGHT, fill=tk.Y)
            scrollbar2.config(command=listbox1.yview)
            listbox2.pack(expand=1, fill="both", side=tk.LEFT)
            listbox2.config( font=(font_1, 18),bg = "#E5CAEE", yscrollcommand=scrollbar2.set)
            global lista_productos
            lista_productos = []

            def acutalizar_lista_productos():
                borrar_todo()
                global lista_productos
                try:
                    
                    lista_productos = read_products()
                    for document in lista_productos:
                        listbox2.insert(tk.END, str(document["name"]+" $"+str(document["cost"])))

                except Exception as e:
                    print(e)
                    messagebox.showerror("Error", e)

            def add_product_to_list():
                global lista_productos
                global arreglo
                object_index = listbox2.curselection()
                value = listbox2.get(object_index)   
                listbox1.insert('end', value)
                arreglo.append(lista_productos[object_index[0]]["_id"])
                calcular_total()
            
            def calcular_total():
                global lista_productos
                global arreglo
                global ids
                global total
                ids = dict.fromkeys(arreglo)
                #cantidades = dict(ids = arreglo.count(ids[0]))
                for id in ids:
                    ids[id] = arreglo.count(id)
                print("ids:",ids)

                for i in range(listbox1.size()):
                    total += int(listbox1.get(i).split("$")[1])


                var1.set("$"+str(total))
                print(total)
            
            def borrar_producto():
                global arreglo
                object_index = listbox1.curselection()
                print("borrar producto con indice:",object_index)
                print(listbox1.get(object_index))
                listbox1.delete(object_index)
                arreglo.pop(object_index[0])
                calcular_total()
            
            def borrar_todo():
                global arreglo
                listbox2.delete(0, tk.END)
                listbox1.delete(0, tk.END)
                arreglo.clear()
                calcular_total()
            
            def terminar_venta():
                global arreglo
                global ids
                global total
                #para la venta es:
                contador = 0
                try:
                    date = dt.datetime.now()
                    empleado = int(id_entry.get())

                    id_venta = add_sale(date, total, empleado)

                    #para productos en venta:
                    for id in ids:
                        add_product_sale( id,id_venta, ids[id])
                        contador += 1
                    if (contador == len(ids)):
                        messagebox.showinfo("Ventas exitosas", "Ventas registradas con exito")
                    borrar_todo()
                except ValueError:
                    messagebox.showerror("Error", "Ingrese un numero de empleado valido")
                except Exception as e:
                    print(e)
                    messagebox.showerror("Error", e)
                

            # Botones frame
            container = tk.Frame(self, bg = color_2)

            canvas2 = tk.Canvas(container,scrollregion=(0,0,500,800),bg=color_2)
            scrollbar = ttk.Scrollbar(container, orient="vertical", command=canvas2.yview)

            s = ttk.Style()
            # Create style used by default for all Frames
            s.configure('TFrame', background=color_2)

            # Create style for the first frame
            s.configure('Frame1.TFrame', background=color_2)
            
            scrollable_frame = ttk.Frame(canvas2,style='Frame1.TFrame')

            scrollable_frame.bind(
                "<Configure>",
                lambda e: canvas2.configure(
                    scrollregion=canvas2.bbox("all")
                )
            )

            canvas2.create_window((0, 0), window=scrollable_frame, anchor="nw")

            canvas2.configure(yscrollcommand=scrollbar.set)

            container.pack(fill =tk.BOTH,side=tk.BOTTOM,expand=True, padx=5, pady=5,anchor=tk.S)
            canvas2.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
            scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

            buttons_frame_1 = tk.Frame(scrollable_frame, bg = color_2)
            buttons_frame_1.pack(padx=10,pady=10,side=tk.LEFT, fill=tk.BOTH, expand=True)

            buttons_frame_2 = tk.Frame(scrollable_frame, bg = color_2)
            buttons_frame_2.pack(padx=10,pady=10,side=tk.LEFT, fill=tk.BOTH, expand=True)

            boton_agregar_producto = tk.Button(buttons_frame_1, text='Añadir producto', font=(font_1, 11), bd=2, command=add_product_to_list , cursor="hand2", bg=color_b,fg=color_3,width=25)
        
            boton_agregar_producto.pack( padx=5, pady=5)

            delete_product_bt = tk.Button(buttons_frame_1, text='Borrar producto', font=(font_1, 11), bd=2, command=borrar_producto,cursor="hand2",    bg=color_b,fg=color_3,width=25)
            delete_product_bt.pack(padx=5, pady=5)

            id_entry = tk.Entry(buttons_frame_1, font=('Helvetica 12'), fg="grey", width=25)
            id_label = tk.Label(buttons_frame_1, text="ID del empleado que atiende:", bg= color_b,font=(font_1, 11),width=25)
            id_label.pack()

            id_entry.insert(tk.END, "Ejemplo: 1234")
            id_entry.pack(pady=5)
            id_entry.bind("<FocusIn>", handle_focus_in)

            costo_label= tk.Label(buttons_frame_1, text="Costo total de la venta:",font=(font_1, 11), bg=color_b, fg=color_3,width=25)
            costo_label.pack()
            
            var1 = tk.StringVar()
            total_label = tk.Label(buttons_frame_1, bg=color_b, fg=color_3,font=(font_1, 11), width=25, textvariable=var1)
            total_label.pack()

            add_product_bt = tk.Button(buttons_frame_2, text='Terminar venta', font=(font_1, 11), bd=2, command=terminar_venta , cursor="hand2", bg=color_b,fg=color_3,width=25).pack( padx=5, pady=5)

            borrar_todo_button = tk.Button(buttons_frame_2, text='Borrar lista', font=(font_1, 11), bd=2, command=borrar_todo, cursor="hand2", bg=color_b,fg=color_3,width=25).pack( padx=5, pady=5)

            actualizar_lista_button = tk.Button(buttons_frame_2, text='Actualizar lista', font=(font_1, 11), bd=2, command=acutalizar_lista_productos, cursor="hand2", bg=color_b,fg=color_3,width=25)
            actualizar_lista_button.pack( padx=5, pady=5)

            #imprimir_arreglo = tk.Button(buttons_frame, text='Print array', font=(font_1, 12), bd=2, command=lambda:print(arreglo), cursor="hand2", bg=color_b,fg=color_3,width=25)
            #imprimir_arreglo.pack( padx=5, pady=5)

            button = tk.Button(buttons_frame_2, text="Atras",font=(font_1, 12),command=lambda: controller.show_frame("StartPage"))
            button.pack()

class Compras(tk.Frame):
    
        def __init__(self, parent, controller):
            tk.Frame.__init__(self, parent,bg=color_1, padx=15, pady=15)
            

            
            self.controller = controller
            global arreglo 
            arreglo = []
            global ids
            
            global total
            total = 0

            label = tk.Label(self, text="Operaciones con Ventas", font=controller.title_font, bg=color_1, fg=color_4)
            label.pack(side="top", fill="x", pady=10)

            added_products_frame  = tk.Frame(self, bg = color_2)
            added_products_frame.place(x=0, y=0, width=50, height = 50)
            added_products_frame.pack(fill =tk.BOTH,side=tk.TOP,expand=True, padx=5, pady=5,anchor=tk.S)

            listbox1_label = tk.Label(added_products_frame, text="Productos añadidos", font=(font_1, 18), bg=color_2, fg=color_3)
            listbox1_label.pack(side=tk.TOP, fill=tk.X, padx=5, pady=5)

            scrollbar1 = tk.Scrollbar(added_products_frame)
            listbox1 = tk.Listbox(added_products_frame,width=30, height=8)
            scrollbar1.config(command=listbox1.yview)
            listbox1.pack(expand=
            True, fill=tk.BOTH, side=tk.LEFT,)
            scrollbar1.pack(side=tk.LEFT, fill=tk.Y)
            listbox1.config(font=(font_1, 18),bg = "#E5CAEE", yscrollcommand=scrollbar1.set)



            list_products_frame  = tk.Frame(self, bg = color_2)
            list_products_frame.place(x=0, y=0, width=50, height = 50)
            list_products_frame.pack(fill =tk.BOTH,side=tk.TOP,expand=True, padx=5, pady=5,anchor=tk.S)

            listbox2_label = tk.Label(list_products_frame, text="Productos disponibles", font=(font_1, 18), bg=color_2, fg=color_3)
            listbox2_label.pack(side=tk.TOP, fill=tk.X, padx=5, pady=5)

            scrollbar2 = tk.Scrollbar(list_products_frame)
            listbox2 = tk.Listbox(list_products_frame,width=30, height=8)
            scrollbar2.pack(side=tk.RIGHT, fill=tk.Y)
            scrollbar2.config(command=listbox1.yview)
            listbox2.pack(expand=1, fill="both", side=tk.LEFT)
            listbox2.config(font=(font_1, 18),bg = "#E5CAEE", yscrollcommand=scrollbar2.set)
            global lista_productos
            lista_productos = []

            def acutalizar_lista_productos():
                borrar_todo()
                global lista_productos
                try:
                    
                    lista_productos = read_products()
                    for document in lista_productos:
                        listbox2.insert(tk.END, str(document["name"]+" $"+str(document["cost"])))

                except Exception as e:
                    print(e)
                    messagebox.showerror("Error", e)

            def add_product_to_list():
                global lista_productos
                global arreglo
                object_index = listbox2.curselection()
                value = listbox2.get(object_index)   
                listbox1.insert('end', value)
                arreglo.append(lista_productos[object_index[0]]["_id"])
                calcular_total()
            
            def calcular_total():
                global lista_productos
                global arreglo
                global ids
                global total
                ids = dict.fromkeys(arreglo)
                #cantidades = dict(ids = arreglo.count(ids[0]))
                for id in ids:
                    ids[id] = arreglo.count(id)
                print("ids:",ids)

                for i in range(listbox1.size()):
                    total += int(listbox1.get(i).split("$")[1])


                var1.set("$"+str(total))
                print(total)
            
            def borrar_producto():
                global arreglo
                object_index = listbox1.curselection()
                print("borrar producto con indice:",object_index)
                print(listbox1.get(object_index))
                listbox1.delete(object_index)
                arreglo.pop(object_index[0])
                calcular_total()
            
            def borrar_todo():
                global arreglo
                listbox2.delete(0, tk.END)
                listbox1.delete(0, tk.END)
                arreglo.clear()
                calcular_total()
            
            def terminar_compra():
                global arreglo
                global ids
                global total
                #para la venta es:
                contador = 0
                try:
                    if listbox1.size() > 0:
                        date = dt.datetime.now()
                        empleado = int(id_entry.get())
                        proveedor = int(proveedor_id_entry.get())
                        compra_id = int(compra_id_entry.get())
                        print("compra_id:",compra_id)
                        id_compra = add_purchase(compra_id, date, empleado, proveedor)
                        if id_compra:
                            #para productos en venta:
                            for id in ids:
                                add_produc_purchase( id,id_compra, ids[id])
                                print("agregado con prod id:",id)
                                contador += 1
                            if (contador == len(ids)):
                                messagebox.showinfo("Compras exitosas", "Compras registradas con exito")
                            borrar_todo()
                        else:
                            pass
                    else:
                        messagebox.showerror("Error", "No hay productos en la lista")
                except ValueError:
                    messagebox.showerror("Error", "Ingrese un numero de empleado valido")
                    
                except Exception as e:
                    print(e)
                    messagebox.showerror("Error", e)
                    

            # Botones frame
            container = tk.Frame(self, bg = color_2)

            canvas = tk.Canvas(container,scrollregion=(0,0,500,800),bg=color_2)
            scrollbar = ttk.Scrollbar(container, orient="vertical", command=canvas.yview)
            
            s = ttk.Style()
            # Create style used by default for all Frames
            s.configure('TFrame', background=color_2)

            # Create style for the first frame
            s.configure('Frame1.TFrame', background=color_2)
            
            scrollable_frame = ttk.Frame(canvas,style='Frame1.TFrame')

            scrollable_frame.bind(
                "<Configure>",
                lambda e: canvas.configure(
                    scrollregion=canvas.bbox("all")
                )
            )

            canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")

            canvas.configure(yscrollcommand=scrollbar.set,bg=color_2)

            container.pack(fill =tk.BOTH,side=tk.BOTTOM,expand=True, padx=5, pady=5,anchor=tk.S)
            canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
            scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

            buttons_frame_1 = tk.Frame(scrollable_frame, bg = color_2)
            buttons_frame_1.pack(padx=10,pady=10,side=tk.LEFT, fill=tk.BOTH, expand=True)

            buttons_frame_2 = tk.Frame(scrollable_frame, bg = color_2)
            buttons_frame_2.pack(padx=10,pady=10,side=tk.LEFT, fill=tk.BOTH, expand=True)

    

            boton_agregar_producto = tk.Button(buttons_frame_1, text='Añadir producto', font=(font_1, 11), bd=2, command=add_product_to_list , cursor="hand2", bg=color_b,fg=color_3,width=25)
        
            boton_agregar_producto.pack( padx=5, pady=5)

            delete_product_bt = tk.Button(buttons_frame_1, text='Borrar producto', font=(font_1, 11), bd=2, command=borrar_producto,cursor="hand2",    bg=color_b,fg=color_3,width=25)
            delete_product_bt.pack(padx=5, pady=5)

            id_entry = tk.Entry(buttons_frame_1, font=('Helvetica 12'), fg="grey" ,width=25)
            id_label = tk.Label(buttons_frame_1, text="ID del empleado que atiende:",bg= color_b,font=(font_1, 11),width=25)
            id_label.pack(padx=5, pady=5)

            id_entry.insert(tk.END, "Ejemplo: 1234")
            id_entry.pack(padx=5, pady=5)
            id_entry.bind("<FocusIn>", handle_focus_in)

            compra_id_entry = tk.Entry(buttons_frame_1, font=('Helvetica 12'), fg="grey" , width=25)
            compra_id_label = tk.Label(buttons_frame_1, text="ID de la compra:",bg= color_b,font=(font_1, 11),width=25)
            compra_id_label.pack(padx=5, pady=5)

            compra_id_entry.insert(tk.END, "Ejemplo: 1234")
            compra_id_entry.pack(pady=5)
            compra_id_entry.bind("<FocusIn>", handle_focus_in)

            proveedor_id_entry = tk.Entry(buttons_frame_1, font=('Helvetica 12'), fg="grey", width=25 )
            proveedor_id_label = tk.Label(buttons_frame_1, text="ID del proveedor:",bg= color_b,font=(font_1, 11),width=25)
            proveedor_id_label.pack(padx=5, pady=5)

            proveedor_id_entry.insert(tk.END, "Ejemplo: 1234")
            proveedor_id_entry.pack(padx=5, pady=5)
            proveedor_id_entry.bind("<FocusIn>", handle_focus_in)

            costo_label= tk.Label(buttons_frame_2, text="Costo total de la compra:",font=(font_1, 11), bg=color_b, fg=color_3,width=25)
            costo_label.pack(padx=5, pady=5)
            
            var1 = tk.StringVar()
            total_label = tk.Label(buttons_frame_2, bg=color_b, fg=color_3,font=('Arial', 12), width=25, textvariable=var1)
            total_label.pack(padx=5, pady=5)

            terminar_compra_button = tk.Button(buttons_frame_2, text='Terminar compra', font=(font_1, 11), bd=2, command=terminar_compra , cursor="hand2", bg=color_b,fg=color_3,width=25).pack( padx=5, pady=5)

            borrar_todo_button = tk.Button(buttons_frame_2, text='Borrar lista', font=(font_1, 11), bd=2, command=borrar_todo, cursor="hand2", bg=color_b,fg=color_3,width=25).pack( padx=5, pady=5)

            actualizar_lista_button = tk.Button(buttons_frame_2, text='Actualizar lista', font=(font_1, 11), bd=2, command=acutalizar_lista_productos, cursor="hand2", bg=color_b,fg=color_3,width=25)
            actualizar_lista_button.pack( padx=5, pady=5)

            #imprimir_arreglo = tk.Button(buttons_frame, text='Print array', font=(font_1, 12), bd=2, command=lambda:print(arreglo), cursor="hand2", bg=color_b,fg=color_3,width=25)
            #imprimir_arreglo.pack( padx=5, pady=5)

            

            button = tk.Button(buttons_frame_2, text="Atras",font=(font_1, 12),command=lambda: controller.show_frame("StartPage"))
            button.pack(padx=5, pady=5)



if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()