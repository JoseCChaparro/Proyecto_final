from tkinter import messagebox
import pymongo
from datetime import datetime
import calendar
from pymongo import MongoClient
import pymongo
import pprint as pp

global db

def conexion(window):
    global db
    try:
        client = MongoClient('localhost', 27017, serverSelectionTimeoutMS=5)
        client.server_info() 
    except pymongo.errors.ServerSelectionTimeoutError as err:
        print(err)
        messagebox.showerror(message="No se pudo establecer la conexión con la base de datos",title="Error")
        window.destroy()

    db = client.DonaChelaDB

def add_emp(emp_no, ename, sex, hiredate, sal):
    """Añade un empleado

    Parameters
    ----------
        emp_no: Numero del empleado.
        ename: Nombre del empleado.
        sex: Sexo del empleado.
        hiredate: Fecha de contratacion.
        sal: Salario del empleado.

    Return
    ------
    None
    """

    try:
        coleccion = db.employees
        post = {
            "_id":emp_no,
            "name":ename,
            "hiredate": hiredate,
            "sex":sex,
            "sal":sal
        }  
        post_id= coleccion.insert_one(post).inserted_id
        if(post_id):
            messagebox.showinfo(message=f'Empleado creado con exito. Id del empleado:{post_id}')
        else:
            raise Exception("Valores no válidos")

    except ValueError as error:    
        messagebox.showerror(message=error,title="Error")
        print(error)
    except pymongo.errors.DuplicateKeyError as error:
        messagebox.showerror(message="El número de empleado ya existe",title="Error")
        print(error)

def update_emp(emp_no, ename, sex, hiredate, sal):
    """Actualizar los valores del empleado dado por el numero de empleado.
    Parameters
    ----------
    
    
    Returns
    ------
    None
    """
    try:
        coleccion = db.employees
        empleado = { "_id": emp_no }
        post = {
            "_id":emp_no,
            "name":ename,
            "hiredate": hiredate,
            "sex":sex,
            "sal":sal
        }  

        nuevos_valores = { "$set": post }
        result = coleccion.update_one(empleado, nuevos_valores)
        if(result.matched_count > 0):
            messagebox.showinfo(message=f'Empleado actualizado con exito. Id del empleado:{emp_no}')
        else:
            raise pymongo.errors.PyMongoError
    except pymongo.errors.PyMongoError as error:
        messagebox.showerror(message="No se encontró el empleado",title="Error")
        print(error)
    except:
        messagebox.showerror(message="No se pudo actualizar el empleado",title="Error")

def delete_emp(emp_no):
    """Elimina un empleado dado por su numero de empleado.
    
    Parameters
    ----------
    
    pemp_no: int 
        Numero de empleado del empleado a borrar
    
    Returns
    -------
    None
    """
    try:
        coleccion = db.employees
        empleado = { "_id": emp_no }
        result = coleccion.delete_one(empleado)
        if result.deleted_count > 0:
            messagebox.showinfo(message='Empleado eliminado con exito')
        else:
            raise Exception("No pudo eliminarse el empleado")
    except Exception as error:    
        messagebox.showerror(message=error,title="Error")
        print(error)

def add_supp(supp_no, suppname):
    """Añade un empleado cuyos valores son los parametros definidos a continuación

    Parameters
    ----------
    
    

    Return
    ------
    None
    """
    try:
        coleccion = db.suppliers
        post = {
            "_id":supp_no,
            "name":suppname
        }  
        post_id= coleccion.insert_one(post).inserted_id
        if(post_id):
            messagebox.showinfo(message=f'Proveedor creado con exito. Id del proveedor:{post_id}')
        else:
            raise Exception("Valores no válidos")

    except ValueError as error:    
        messagebox.showerror(message=error,title="Error")
        print(error)
    except pymongo.errors.DuplicateKeyError as error:
        messagebox.showerror(message="El número de proveedor ya existe",title="Error")
        print(error)

def update_supp(supp_no, suppname):
    """Actualizar los valores del empleado dado por el numero de empleado.
    Parameters
    ----------
   
    
    Returns
    ------
    None
    """
    try:
        coleccion = db.suppliers
        proveedor = { "_id": supp_no }
        post = {
            "_id":supp_no,
            "name":suppname
        }   

        nuevos_valores = { "$set": post }
        result = coleccion.update_one(proveedor, nuevos_valores)
        if(result.matched_count > 0):
            messagebox.showinfo(message=f'Proveedor actualizado con exito. Id del empleado:{supp_no}')
        else:
            raise pymongo.errors.PyMongoError
    except pymongo.errors.PyMongoError as error:
        messagebox.showerror(message="No se encontró el proveedor",title="Error")
        print(error)
    except:
        messagebox.showerror(message="No se pudo actualizar el proveedor",title="Error")

def delete_supp(supp_no):
    """Elimina un empleado dado por su numero de empleado.
    
    Parameters
    ----------
    
    pemp_no: int 
        Numero de empleado del empleado a borrar
    
    Returns
    -------
    None
    """
    try:
        coleccion = db.suppliers
        proveedor = { "_id": supp_no }
        result = coleccion.delete_one(proveedor)
        if result.deleted_count > 0:
            messagebox.showinfo(message='Proveedor eliminado con exito')
        else:
            raise Exception("No pudo eliminarse el proveedor")
    except Exception as error:    
        messagebox.showerror(message=error,title="Error")
        print(error)

def add_product(produc_no, producname, produccost, produccant, producdesc):
    """Añade un empleado cuyos valores son los parametros definidos a continuación

    Parameters
    ----------
    
    

    Return
    ------
    None
    """
    try:
        coleccion = db.products
        post = {
            "_id":produc_no,
            "name":producname,
            "cost":produccost,
            "inventory":produccant,
            "description":producdesc
        }  
        post_id= coleccion.insert_one(post).inserted_id
        if(post_id):
            messagebox.showinfo(message=f'Producto creado con exito. Id del producto:{post_id}')
        else:
            raise "Valores no válidos"

    except ValueError as error:    
        messagebox.showerror(message=error,title="Error")
        print(error)
    except pymongo.errors.DuplicateKeyError as error:
        messagebox.showerror(message="El número de producto ya existe",title="Error")
        print(error)

def update_product(produc_no, producname, produccost, produccant, producdesc):
    """Actualizar los valores del empleado dado por el numero de empleado.
    Parameters
    ----------
   
    
    Returns
    ------
    None
    """
    try:
        coleccion = db.products
        producto = { "_id": produc_no }
        post = {
            "_id":produc_no,
            "name":producname,
            "cost":produccost,
            "inventory":produccant,
            "description":producdesc
        }   

        nuevos_valores = { "$set": post }
        result = coleccion.update_one(producto, nuevos_valores)
        if(result.matched_count > 0):
            messagebox.showinfo(message=f'Producto actualizado con exito. Id del empleado:{produc_no}')
        else:
            raise pymongo.errors.PyMongoError
    except pymongo.errors.PyMongoError as error:
        messagebox.showerror(message="No se encontró el producto",title="Error")
        print(error)
    except:
        messagebox.showerror(message="No se pudo actualizar el producto",title="Error")

def delete_product(produc_no):
    """Elimina un empleado dado por su numero de empleado.
    
    Parameters
    ----------
    
    pemp_no: int 
        Numero de empleado del empleado a borrar
    
    Returns
    -------
    None
    """
    try:
        coleccion = db.products
        producto = { "_id": produc_no }
        result = coleccion.delete_one(producto)
        if result.deleted_count > 0:
            messagebox.showinfo(message='Producto eliminado con exito')
        else:
            raise Exception("No pudo eliminarse el producto")
    except Exception as error:    
        messagebox.showerror(message=error,title="Error")
        print(error)

def add_sale( sale_date, sale_cost, sale_emp):
    try:
        coleccion = db.sales
        post = {
            #"_id":sale_no,
            "date": sale_date,
            "total":sale_cost,
            "emp_name":sale_emp
        }  
        post_id= coleccion.insert_one(post).inserted_id
        if(post_id):
            messagebox.showinfo(message=f'Venta creada con exito. Id de la venta:{post_id}')
            return post_id
        else:
            raise Exception("Valores no válidos")

    except ValueError as error:    
        messagebox.showerror(message=error,title="Error")
        print(error)
    except pymongo.errors.DuplicateKeyError as error:
        messagebox.showerror(message="El número de venta ya existe",title="Error")
        print(error)

def update_sale(sale_no, sale_date, sale_cost, sale_emp):
    """Actualizar los valores del empleado dado por el numero de empleado.
    Parameters
    ----------
    
    
    Returns
    ------
    None
    """
    try:
        coleccion = db.sales
        venta = { "_id": sale_no }
        post = {
            "_id":sale_no,
            "date": datetime.strptime(sale_date,"%d/%m/%Y"),
            "cantidad":sale_cost,
            "emp_name":sale_emp
        }  

        nuevos_valores = { "$set": post }
        result = coleccion.update_one(venta, nuevos_valores)
        if(result.matched_count > 0):
            messagebox.showinfo(message=f'Venta actualizada con exito. Id de la venta:{sale_no}')
        else:
            raise pymongo.errors.PyMongoError
    except pymongo.errors.PyMongoError as error:
        messagebox.showerror(message="No se encontró la venta",title="Error")
        print(error)
    except:
        messagebox.showerror(message="No se pudo actualizar la venta",title="Error")

def delete_sale(sale_no):
    """Elimina un empleado dado por su numero de empleado.
    
    Parameters
    ----------
    
    pemp_no: int 
        Numero de empleado del empleado a borrar
    
    Returns
    -------
    None
    """
    try:
        coleccion = db.sales
        venta = { "_id": sale_no }
        result = coleccion.delete_one(venta)
        if result.deleted_count > 0:
            messagebox.showinfo(message='Venta eliminado con exito')
        else:
            raise Exception("No pudo eliminarse la venta")
    except Exception as error:    
        messagebox.showerror(message=error,title="Error")
        print(error)

def add_purchase(purchase_no, purchase_date, ename, supp_no):
    try:
        coleccion = db.purchases
        post = {
            "_id":purchase_no,
            "date": purchase_date,
            "emp_name":ename,
            "supplier":supp_no
        }  
        post_id= coleccion.insert_one(post).inserted_id
        if(post_id):
            messagebox.showinfo(message=f'Compra creada con exito. Id de la compra:{post_id}')
            return post_id
        else:
            raise Exception("Valores no válidos")

    except ValueError as error:    
        messagebox.showerror(message=error,title="Error")
        print(error)
    except pymongo.errors.DuplicateKeyError as error:
        messagebox.showerror(message="El número de compra ya existe",title="Error")
        print(error)

def update_purchase(purchase_no, purchase_date, ename, supp_no):
    """Actualizar los valores del empleado dado por el numero de empleado.
    Parameters
    ----------
    
    
    Returns
    ------
    None
    """
    try:
        coleccion = db.purchases
        compra = { "_id": purchase_no }
        post = {
            "_id":purchase_no,
            "date": datetime.strptime(purchase_date,"%d/%m/%Y"),
            "emp_name":ename,
            "supplier":supp_no
        }  

        nuevos_valores = { "$set": post }
        result = coleccion.update_one(compra, nuevos_valores)
        if(result.matched_count > 0):
            messagebox.showinfo(message=f'Compra actualizada con exito. Id de la venta:{purchase_no}')
        else:
            raise pymongo.errors.PyMongoError
    except pymongo.errors.PyMongoError as error:
        messagebox.showerror(message="No se encontró la compra",title="Error")
        print(error)
    except:
        messagebox.showerror(message="No se pudo actualizar la compra",title="Error")

def delete_purchase(purchase_no):
    """Elimina un empleado dado por su numero de empleado.
    
    Parameters
    ----------
    
    pemp_no: int 
        Numero de empleado del empleado a borrar
    
    Returns
    -------
    None
    """
    try:
        coleccion = db.purchases
        compra = { "_id": purchase_no }
        result = coleccion.delete_one(compra)
        if result.deleted_count > 0:
            messagebox.showinfo(message='Compra eliminada con exito')
        else:
            raise Exception("No pudo eliminarse la compra")
    except Exception as error:    
        messagebox.showerror(message=error,title="Error")
        print(error)

def add_product_sale(product_no, sale_no, cant):
    try:
        coleccion = db.sales_products
        post = {
            "product_no":product_no,
            "sale_no":sale_no,  # id: {a: 1, b:1} ????
            "cantidad":cant
        }  
        post = coleccion.insert_one(post)
        if(not(post)):
            raise Exception("Valores no válidos")
        else:
            return post.inserted_id
    except ValueError as error:    
        messagebox.showerror(message=error,title="Error")
        print(error)

def delete_product_sale(product_no, sale_no):
    try:
        coleccion = db.sales_products
        producto = { "_id": {"product_no":product_no, "sale_no":sale_no}}
        result = coleccion.delete_one(producto)
        if result.deleted_count == 0:
           raise Exception("No pudo eliminarse el producto de la venta")
            
    except Exception as error:    
        messagebox.showerror(message=error,title="Error")
        print(error)

def update_produc_sale(produc_no, sale_no, cant):
    try:
        coleccion = db.sales_products
        producto = { "_id": {"produc_no":produc_no, "sale_no":sale_no}}
        post = {
            "_id":{"produc_no":produc_no, "sale_no":sale_no},
            "cantidad":cant
        }  

        nuevos_valores = { "$set": post }
        result = coleccion.update_one(producto, nuevos_valores)
        if(result.matched_count == 0):
            raise Exception("No pudo actualizarse el producto de la venta")
            
    except Exception as error:    
        messagebox.showerror(message=error,title="Error")
        print(error)

def add_produc_purchase(produc_no, purchase_no, cant):
    try:
        coleccion = db.purchases_products
        post = {
            "product_no":produc_no,
            "purchase_no":purchase_no,
            "cantidad":cant
        }  
        post = coleccion.insert_one(post)
        if(not(post)):
            raise Exception("Valores no válidos")
        return post.inserted_id
    except ValueError as error:    
        messagebox.showerror(message=error,title="Error")
        print(error)

def delete_produc_purchase(produc_no, purchase_no):
    try:
        coleccion = db.purchases_products
        producto = { "_id": {"produc_no":produc_no, "purchase_no":purchase_no}}
        result = coleccion.delete_one(producto)
        if result.deleted_count == 0:
           raise Exception("No pudo eliminarse el producto de la compra")
            
    except Exception as error:    
        messagebox.showerror(message=error,title="Error")
        print(error)

def update_produc_purchase(produc_no, purchase_no, cant):
    try:
        coleccion = db.purchases_products
        producto = { "_id": {"produc_no":produc_no, "purchase_no":purchase_no}}
        post = {
            "_id":{"produc_no":produc_no, "purchase_no":purchase_no},
            "cantidad":cant
        }  

        nuevos_valores = { "$set": post }
        result = coleccion.update_one(producto, nuevos_valores)
        if(result.matched_count == 0):
            raise Exception("No pudo actualizarse el producto de la compra")
            
    except Exception as error:    
        messagebox.showerror(message=error,title="Error")
        print(error)
def read_products():
    """Lee los datos de las ventas de la base de datos.
    
    Parameters
    ----------
    
    None
    
    Returns
    -------
    list
        Lista con los datos de las ventas
    """
    try:
        coleccion = db.products
        consulta = coleccion.find({})
        productos = list(consulta)
        if len(productos) == 0:
            raise Exception("No se encontro ningun prodcuto")
        else:
            return productos
    except Exception as error:
        raise Exception(error)

def read_sale(id):
    """Lee los datos de las ventas de la base de datos.
    
    Parameters
    ----------
    
    None
    
    Returns
    -------
    list
        Lista con los datos de las ventas
    """
    try:
        coleccion = db.ventas
        consulta = coleccion.find({"_id":id})
        ventas = list(consulta)
        if len(ventas) == 0:
            raise Exception("No se encontró la venta")
        else:
            return ventas
    except Exception as error:
        raise Exception(error)
def read_sales(product_id):
    """Lee los datos de las ventas de la base de datos.
    
    Parameters
    ----------
    
    None
    
    Returns
    -------
    list
        Lista con los datos de las ventas
    """
    try:
        coleccion = db.sales_products
        print("buscando ventas de producto: ", product_id)
        consulta = coleccion.find({"product_no":product_id})
        ventas = list(consulta)
        if len(ventas) == 0:
            raise Exception("No se encontro ninguna venta")
        else:
            return ventas
    except Exception as error:
        raise Exception(error)

def read_purchases(product_id):
    """Lee los datos de las compras de la base de datos.
    
    Parameters
    ----------
    
    None
    
    Returns
    -------
    list
        Lista con los datos de las compras
    """
    try:
        coleccion = db.purchases_products
        consulta = coleccion.find({"product_no":product_id})
        ventas = list(consulta)
        if len(ventas) == 0:
            raise Exception("No se encontró la compra")
        else:
            return ventas
    except Exception as error:
        raise Exception(error)