import sqlite3
import pandas as pd

conexion = sqlite3.connect("videojuegos.db")
cursor = conexion.cursor()

archivo_datos= "Datos_Tablas_Videojuegos.xlsx"
xls = pd.ExcelFile(archivo_datos)

for hojan in xls.sheet_names:
    df = pd.read_excel(xls, sheet_name=Usuario)
    df.to_sql(Usuario, conexion, if_exists="replace", index=False)

def crear_tablas():
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS Usuarios (
        id_usuario INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        email TEXT UNIQUE NOT NULL,
        telefono TEXT)''')
    cursor.execute('''CREATE TABLE IF NOT EXISTS Videojuegos (
        id_videojuego INTEGER PRIMARY KEY AUTOINCREMENT,
        titulo TEXT NOT NULL,
        plataforma TEXT NOT NULL,
        stock INTEGER NOT NULL)''')
    cursor.execute('''CREATE TABLE IF NOT EXISTS Prestamos (
        id_prestamo INTEGER PRIMARY KEY AUTOINCREMENT,
        id_usuario INTEGER NOT NULL,
        id_videojuego INTEGER NOT NULL,
        fecha_prestamo TEXT NOT NULL,
        fecha_devolucion TEXT NOT NULL,
        FOREIGN KEY (id_usuario) REFERENCES Usuarios(id_usuario),
        FOREIGN KEY (id_videojuego) REFERENCES Videojuegos(id_videojuego))''')
    conexion.commit()
    conexion.close()

def insertar_usuario(nombre, email, telefono):
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("INSERT INTO Usuarios (nombre, email, telefono) VALUES (?, ?, ?)", (nombre, email, telefono))
    conexion.commit()
    conexion.close()

def menu():
    crear_tablas()
    while True:
        print(" 1. Insertar usuario 2. Insertar videojuego 3. Insertar préstamo 4. Mostrar usuarios 5. Eliminar usuario 6. Eliminar préstamo 7. Salir")
        opcion = input("Elige una opción: ")
        if opcion == "1":
            insertar_usuario(input("Nombre: "), input("Email: "), input("Teléfono: "))
        elif opcion == "2":
            insertar_videojuego(input("Título: "), input("Plataforma: "), int(input("Stock: ")))
        elif opcion == "3":
            insertar_prestamo(int(input("ID Usuario: ")), int(input("ID Videojuego: ")), input("Fecha préstamo: "), input("Fecha devolución: "))
        elif opcion == "4":
            mostrar_usuarios()
        elif opcion == "5":
            eliminar_usuario(int(input("ID Usuario a eliminar: ")))
        elif opcion == "6":
            eliminar_prestamo(int(input("ID Préstamo a eliminar: ")))
        elif opcion == "7":
            break
        else:
            print("Opción no válida")

if __name__ == "__main__":
    menu()