import os
import sys
import sqlite3
from sqlite3 import Error
import datetime
suma_venta = []
#Crea una tabla en SQLite3

try:
    with sqlite3.connect("evidencia3.db") as conn:
        c = conn.cursor()
        c.execute("CREATE TABLE IF NOT EXISTS venta (folio INTEGER PRIMARY KEY AUTOINCREMENT,descripcion TEXT NOT NULL , cantidad_articulo INTEGER NOT NULL,precio_unitario FLOAT NOT NULL , FechaVenta timestamp NOT NULL);")
        print("Tabla creada exitosamente")
except Error as e:
    print (e)
except:
    print(f"Se produjo el siguiente error: {sys.exc_info()[0]}")
finally:
    conn.close()

def registrarArticulo():
    try:
        with sqlite3.connect("evidencia3.db") as conn: #1- Puente
            mi_cursor = conn.cursor() #2- Mensajero
            valores = {"descripcion":descripcion,"cantidad_articulo":cantidad_articulo,"precio_unitario":precio_unitario, "Fecha":fechaprocesada}
            mi_cursor.execute("INSERT INTO venta VALUES(null,:descripcion,:cantidad_articulo,:precio_unitario,:Fecha)", valores)
            print("Registro agregado exitosamente")
            input("Presione cualquier tecla para continuar...")
    except Error as e:
        print (e)
    except:
        print(f"Se produjo el siguiente error: {sys.exc_info()[0]}")
    finally:
        if (conn):
            conn.close()

def consultarArticulo(valor_folio):
    try:
        with sqlite3.connect("evidencia3.db") as conn:#1 Crear la conexión
            mi_cursor = conn.cursor()#2 Crear el cursor (emisario)
            valores = {"folio":valor_folio}
            mi_cursor.execute("SELECT * FROM venta WHERE folio = :folio", valores)
            registro = mi_cursor.fetchall()#4 Recuperamos los datos resultantes
            print("Folio\tArtículo\tCantidad\tPrecio\tfecha")
            print("*" * 30)
            if registro:
                for folio, descripcion, cantidad, precio, fecha in registro:
                    print(f"{folio} \t", end="")
                    print(f"{descripcion} \t", end="")
                    print(f"{cantidad} \t", end="")
                    print(f"{precio} \t", end="")
                    print(f"{fecha} \t", end="")
                    input("Presione cualquier tecla para continuar...")
            else:
                print(f"No se encontró un articulo asociado con la clave {valor_clave}")
                input("Presione cualquier tecla para continuar...")
    except Error as e:
        print (e)
    except:
        print(f"Se produjo el siguiente error: {sys.exc_info()[0]}")
 
def consultarFecha():
    try:
        with sqlite3.connect("evidencia3.db") as conn:#1 Crear la conexión
            mi_cursor = conn.cursor()#2 Crear el cursor (emisario)
            valores = {"fecha":fechaprocesada}
            mi_cursor.execute("SELECT * FROM venta WHERE FechaVenta = :fecha", valores)
            registro = mi_cursor.fetchall()#4 Recuperamos los datos resultantes
            print("Folio\tArticulo\tCantidad\tPrecio\tfecha")
            print("*" * 30)
            if registro:
                for folio, descripcion, cantidad, precio, fecha in registro:
                    print(f"{folio} \t", end="")
                    print(f"{descripcion} \t", end="")
                    print(f"{cantidad} \t", end="")
                    print(f"{precio} \t", end="")
                    print(f"{fecha} \t")
                input("Presione cualquier tecla para continuar...")
            else:
                print(f"No se encontraron articulos")
                input("Presione cualquier tecla para continuar...")

    except Error as e:
        print (e)
    except:
        print(f"Se produjo el siguiente error: {sys.exc_info()[0]}")

while True:
    print()
    print("[1] Registrar una venta")
    print("[2] Consultar una venta")
    print("[3] Consultar una venta por una fecha en específico")
    print("[4] Salir")
    respuesta = int(input("Elige una opción: "))
    if respuesta == 1:
        while True:
            print("--- Registro de articulo ---")
            descripcion = input("Ingresa el nombre del articulo: ")
            cantidad_articulo = int(input("Ingresa la cantidad del articulo: "))
            precio_unitario = float(input("Ingresa el precio unitario del articulo: "))
            subtotal = cantidad_articulo * precio_unitario
            suma_venta.append(subtotal)
            fecha = input("Fecha de la venta (dd/mm/aa): ")
            fechaprocesada = datetime.datetime.strptime(fecha, "%d/%m/%Y").date()
            registrarArticulo()
            opcion = int(input("\n ¿Deseas capturar otro registro? \n(1-Si / 0-No): "))
            if opcion == 0:
                total = sum(suma_venta)
                print("EL TOTAL A PAGAR ES: ",total)
                break
    elif respuesta == 2:
        print("--------- Consulta de articulo ---------")
        folio = int(input("Folio a consultar: "))
        consultarArticulo(folio)
    elif respuesta == 3:
        print("----------- Consulta del catalogo -----------")
        fecha_consulta = input("Fecha a consultar (dd/mm/aa): ")
        fechaprocesada = datetime.datetime.strptime(fecha_consulta, "%d/%m/%Y").date()
        consultarFecha()
    elif respuesta == 4:
        print("--- Fin del programa ---")
        break
    else:
        print("Opcion no encontrada")
        input("Presione cualquier tecla para continuar...")