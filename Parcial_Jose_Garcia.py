import sqlite3
from sqlite3 import Error

try:
    con = sqlite3.connect('inventario507.db')

    print("Conexion exitosa")
except Error:
    print("Conexion fallida")

try:
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS inventario(id integer PRIMARY KEY, articulo text, precio float)")
    print("Creacion exitosa")
except Error:
    print("Error en creacion")

print("INVENTARIO")
print("SELECCIONE UNA DE LAS SIGUIENTES OPCIONES:")
print("1: Agregar")
print("2: Editar")
print("3: Eliminar")
print("4: Ver lista de articulos")
print("5: Buscar articulo")
seleccion = int(input(""))

if seleccion == 1:

    id = int(input("ID: "))
    articulo = input("Articulo: ")
    precio = float(input("Precio: "))

    try:
        cur = con.cursor()
        cur.execute('''INSERT INTO inventario VALUES(?, ?, ? )''', (id, articulo, precio))
        con.commit()
        print("Insercion exitosa")
    except Error:
        print("Error en insercion")

elif seleccion == 2:

    try:
        editar_articulo = input("Articulo a editar: ")
        editar_precio = float(input("Nuevo precio: "))
        cur = con.cursor()
        cur.execute('UPDATE inventario SET precio = ? WHERE articulo = ?',  (editar_precio, editar_articulo,))
        con.commit()
        print("Actualizacion exitosa")
    except Error:
        print("Error al actualizar datos")

elif seleccion == 3:

    try:

        remover = input("Eliminar: ")
        cur = con.cursor()
        cur.execute('DELETE FROM inventario WHERE articulo = ?', (remover,))
        con.commit()
        print("Registro Eliminado")
    except Error:
        print("Error al eliminar")

elif seleccion == 4:
    try:

        cur = con.cursor()
        cur.execute('SELECT id, articulo, precio FROM inventario ')
        p = cur.fetchall()

        for i in p:
            print(i)


    except:
        print("Error al traer datos")

elif seleccion == 5:
    try:
        peticion = input("Buscar: ")
        cur = con.cursor()
        cur.execute('SELECT precio FROM inventario WHERE articulo = ?', (peticion,))
        print(cur.fetchall())

    except Error:
        print("Error al traer datos")

con.close()