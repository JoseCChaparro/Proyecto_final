import tkinter as tk
from functools import partial
from config.interfaz_config import callback,check_window_open,handle_focus_in,font_1,color_3
import config.interfaz_config as interfaz_config
import datetime
from tkinter import messagebox
from operaciones import add_emp,delete_emp,update_emp
def add_emp_window(ventana):
    
    check_window_open()
    
    print(interfaz_config.counter_windows)
    if interfaz_config.counter_windows == 0:
        interfaz_config.counter_windows += 1
        new_emp_window = tk.Toplevel(ventana)
        new_emp_window.protocol("WM_DELETE_WINDOW", partial(callback,new_emp_window))
        new_emp_window.minsize(300,300)
        new_emp_window.title("Añadir empleado")

        empno_entry = tk.Entry(new_emp_window, font=('Helvetica 12'), fg="grey" )
        empno_label = tk.Label(new_emp_window, text="Numero de empleado:")
        empno_label.pack()

        empno_entry.insert(tk.END, "Ejemplo: 1234")
        empno_entry.pack(pady=5)

        empno_entry.bind("<FocusIn>", handle_focus_in)


        nombre_label = tk.Label(new_emp_window, text="Nombre del empleado :")
        nombre_label.pack()
        nombre_entry = tk.Entry(new_emp_window, font=('Helvetica 12'), fg="grey")
        nombre_entry.insert(tk.END, "Ejemplo: Jose")
        nombre_entry.pack(pady=5)

        nombre_entry.bind("<FocusIn>", handle_focus_in)


        sex_label = tk.Label(new_emp_window, text="Sexo del empleado:")
        sex_label.pack()
        sex_entry = tk.Entry(new_emp_window, font=('Helvetica 12'), fg="grey")
        sex_entry.insert(tk.END, "Ejemplo: Hombre")
        sex_entry.pack(pady=5)

        sex_entry.bind("<FocusIn>", handle_focus_in)


        hiredate_label = tk.Label(new_emp_window, text="Fecha de contratación de empleado:")
        hiredate_label.pack()
        hiredate_entry = tk.Entry(new_emp_window, font=('Helvetica 12'), fg="grey")
        hiredate_entry.insert(tk.END, "Ejemplo: 27/11/2022")
        hiredate_entry.pack(pady=5)

        hiredate_entry.bind("<FocusIn>", handle_focus_in)

        salary_label = tk.Label(new_emp_window, text="Salario del empleado:")
        salary_label.pack()
        salary_entry = tk.Entry(new_emp_window, font=('Helvetica 12'), fg="grey")
        salary_entry.insert(tk.END, "Ejemplo: 1600")
        salary_entry.pack(pady=5)

        salary_entry.bind("<FocusIn>", handle_focus_in)
        
        def ok():
            empno = int(empno_entry.get())
            nombre = str(nombre_entry.get())
            sex = str(sex_entry.get())
            
            
            
            try:
                hiredate = datetime.datetime.strptime(hiredate_entry.get(), "%d/%m/%Y")
            except ValueError as e:
                messagebox.showinfo("Formato de fecha incorrecto debe ser DD/MM/YYYY")
            salary = int(salary_entry.get())
            print("add_emp(",empno, nombre ,sex ,hiredate ,salary ,")")
            add_emp(empno, nombre, sex, hiredate, salary)
            




        boton = tk.Button(new_emp_window, text="Añadir empleado", command=ok )

        boton.pack()


def update_emp_window(ventana):
    
    check_window_open()

    if interfaz_config.counter_windows == 0:
        interfaz_config.counter_windows += 1
        edit_emp_window = tk.Toplevel(ventana)
        edit_emp_window.protocol("WM_DELETE_WINDOW", partial(callback,edit_emp_window))
        edit_emp_window.minsize(300,300)
        edit_emp_window.title("Modificar empleado")

        empno_entry = tk.Entry(edit_emp_window, font=('Helvetica 12'), fg="grey" )
        empno_label = tk.Label(edit_emp_window, text="Numero del empleado a editar:")
        empno_label.pack()

        empno_entry.insert(tk.END, "Ejemplo: 1234")
        empno_entry.pack(pady=5)

        empno_entry.bind("<FocusIn>", handle_focus_in)


        nombre_label = tk.Label(edit_emp_window, text="Nuevo nombre del empleado a editar:")
        nombre_label.pack()
        nombre_entry = tk.Entry(edit_emp_window, font=('Helvetica 12'), fg="grey")
        nombre_entry.insert(tk.END, "Ejemplo: Jose")
        nombre_entry.pack(pady=5)

        nombre_entry.bind("<FocusIn>", handle_focus_in)


        sex_label = tk.Label(edit_emp_window, text="Nuevo sexo del empleado a editar:")
        sex_label.pack()
        sex_entry = tk.Entry(edit_emp_window, font=('Helvetica 12'), fg="grey")
        sex_entry.insert(tk.END, "Ejemplo: Mujer")
        sex_entry.pack(pady=5)

        sex_entry.bind("<FocusIn>", handle_focus_in)


        hiredate_label = tk.Label(edit_emp_window, text="Nueva fecha de contratación de empleado a editar:")
        hiredate_label.pack()
        hiredate_entry = tk.Entry(edit_emp_window, font=('Helvetica 12'), fg="grey")
        hiredate_entry.insert(tk.END, "Ejemplo: 20/11/2022")
        hiredate_entry.pack(pady=5)

        hiredate_entry.bind("<FocusIn>", handle_focus_in)

        salary_label = tk.Label(edit_emp_window, text="Nuevo salario del empleado a editar:")
        salary_label.pack()
        salary_entry = tk.Entry(edit_emp_window, font=('Helvetica 12'), fg="grey")
        salary_entry.insert(tk.END, "Ejemplo: 1600")
        salary_entry.pack(pady=5)

        salary_entry.bind("<FocusIn>", handle_focus_in)


        def ok():
            empno = int(empno_entry.get())
            nombre = str(nombre_entry.get())
            sex = str(sex_entry.get())
            
            try:
                hiredate = datetime.datetime.strptime(hiredate_entry.get(), "%d/%m/%Y")
            except ValueError as e:
                messagebox.showinfo("Formato de fecha incorrecto debe ser DD/MM/YYYY")
            salary = int(salary_entry.get())

            print("update_emp(",empno, nombre ,sex ,hiredate ,salary,")")
            update_emp(empno, nombre ,sex ,hiredate ,salary)

        boton = tk.Button(edit_emp_window, text="Modificar empleado", command=ok )

        boton.pack()

def delete_emp_window(ventana):
    
    check_window_open()

    if interfaz_config.counter_windows == 0:
        interfaz_config.counter_windows += 1
        delete_emp_window = tk.Toplevel(ventana)
        delete_emp_window.protocol("WM_DELETE_WINDOW", partial(callback,delete_emp_window))
        delete_emp_window.minsize(300,100)
        delete_emp_window.title("Eliminar empleado")

        empno_entry = tk.Entry(delete_emp_window, font=('Helvetica 12'), fg="grey" )
        empno_label = tk.Label(delete_emp_window, text="Numero del empleado a eliminar:")
        empno_label.pack()

        empno_entry.insert(tk.END, "Ejemplo: 1234")
        empno_entry.pack(pady=5)

        empno_entry.bind("<FocusIn>", handle_focus_in)


        def ok():
            empno = int(empno_entry.get())
            print("delete_emp(",empno,")")
            delete_emp(empno)



        boton = tk.Button(delete_emp_window, text="Eliminar empleado", command=ok )

        boton.pack()


def noemp_depto_window(ventana):
    
    check_window_open()

    if interfaz_config.counter_windows == 0:
        interfaz_config.counter_windows += 1
        empleados_windows = tk.Toplevel(ventana)
        empleados_windows.protocol("WM_DELETE_WINDOW", partial(callback,empleados_windows))
        empleados_windows.minsize(300,500)
        empleados_windows.title("Obtener cantidad de empleados de depto")

        empno_entry = tk.Entry(empleados_windows, font=('Helvetica 12'), fg="grey" )
        empno_label = tk.Label(empleados_windows, text="Número de departamento:")
        empno_label.pack()

        empno_entry.insert(tk.END, "Ejemplo: 1234")
        empno_entry.pack(pady=5)

        empno_entry.bind("<FocusIn>", handle_focus_in)

        def ok():
            empno = int(empno_entry.get())

            print("noemp_depto(",empno,")")



        boton = tk.Button(empleados_windows, text="Obtener cantidad de empleados", command=ok )

        boton.pack()

def search_emp_window(ventana):
    
    check_window_open()

    if interfaz_config.counter_windows == 0:
        interfaz_config.counter_windows += 1
        empleados_windows = tk.Toplevel(ventana)
        empleados_windows.protocol("WM_DELETE_WINDOW", partial(callback,empleados_windows))
        empleados_windows.minsize(300,500)
        empleados_windows.title("Buscar empleado")

        empno_entry = tk.Entry(empleados_windows, font=('Helvetica 12'), fg="grey" )
        empno_label = tk.Label(empleados_windows, text="Número de empleado:")
        empno_label.pack()

        empno_entry.insert(tk.END, "Ejemplo: 1234")
        empno_entry.pack(pady=5)

        empno_entry.bind("<FocusIn>", handle_focus_in)

        def ok():
            emp_no = int(empno_entry.get())

            print("read_emp(",emp_no,")")



        boton = tk.Button(empleados_windows, text="Buscar empleado", command=ok )

        boton.pack()


def create_employees_window(window):
    
    color_b = "gray92"
    ventana = tk.Toplevel(window)
    ventana.title("Empleados")
    ventana.minsize(300,300)
    ventana.protocol("WM_DELETE_WINDOW", partial(callback,ventana))
    tk.Label(ventana, text="Empleados").pack()

    add_emp_bt = tk.Button(ventana, text='Añadir empleado', font=(font_1, 12), bd=2, command=partial(add_emp_window,window) , cursor="hand2", bg=color_b,fg=color_3,width=25).pack( padx=5, pady=10)

    view_bt = tk.Button(ventana, text='Modificar empleado', font=(font_1, 12), bd=2, command=partial(update_emp_window,window), cursor="hand2", bg=color_b,fg=color_3,width=25).pack( padx=5, pady=10)

    delete_empn_bt = tk.Button(ventana, text='Borrar empleado', font=(font_1, 12), bd=2, command=partial(delete_emp_window,window),cursor="hand2", bg=color_b,fg=color_3,width=25).pack(padx=5, pady=10)

    get_no_emp_bt = tk.Button(ventana, text='No. Empleados', font=(font_1, 12), bd=2, command=partial(noemp_depto_window,window), cursor="hand2", bg=color_b,fg=color_3,anchor=tk.CENTER,width=25).pack(padx=5, pady=10)

    buscar_emp_bt = tk.Button(ventana, text='Buscar un empleado', font=(font_1, 12), bd=2, command=partial(search_emp_window,window), cursor="hand2", bg=color_b,fg=color_3,anchor=tk.CENTER,width=25).pack(padx=5, pady=10)

