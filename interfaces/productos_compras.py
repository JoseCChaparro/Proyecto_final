import tkinter as tk
from functools import partial
from config.interfaz_config import callback,check_window_open,handle_focus_in,font_1,color_3
import config.interfaz_config as interfaz_config
from operaciones import read_purchases
from tkinter import messagebox
from datetime import datetime
import pprint
def read_purchase_window(window):
        
        check_window_open()
        
        print(interfaz_config.counter_windows)
        if interfaz_config.counter_windows == 0:
            interfaz_config.counter_windows += 1
            read_sale_window = tk.Toplevel(window)
            read_sale_window.protocol("WM_DELETE_WINDOW", partial(callback,read_sale_window))
            read_sale_window.minsize(300,100)
            read_sale_window.title("Leer venta")
    
            product_id_label = tk.Label(read_sale_window, text="Numero de compra:")
            product_id_label.pack()
            product_id_entry = tk.Entry(read_sale_window, font=('Helvetica 12'), fg="grey" )
            product_id_entry.insert(tk.END, "Ejemplo: 1")
            product_id_entry.pack(pady=5)
            product_id_entry.bind("<FocusIn>", handle_focus_in)
            
            def ok():
                
                try:
                    product_id = int(product_id_entry.get())
                    print("product_id en compras",product_id)
                    compra = read_purchases(product_id)
                    string_compra = pprint.pformat(compra)
                except Exception as error:
                    messagebox.showerror("Error", error)
                    return

                print(string_compra)
                messagebox.showinfo("Compra", f"Compras leida:{string_compra}",    parent=read_sale_window)
                
            boton = tk.Button(read_sale_window, text="Leer compra", command=ok )
    
            boton.pack()
    
            boton.pack()
