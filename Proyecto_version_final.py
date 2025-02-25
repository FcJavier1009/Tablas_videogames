import sqlite3

def conectar():
    return sqlite3.connect("videojuegos.db")

def crear_tablas():
    conexion = conectar()
    conexion.execute('PRAGMA foreign_keys=ON')
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
        fecha_prestamo DATE NOT NULL,
        fecha_devolucion DATE NOT NULL,
        FOREIGN KEY (id_usuario) REFERENCES Usuarios(id_usuario),
        FOREIGN KEY (id_videojuego) REFERENCES Videojuegos(id_videojuego))''')
    cursor.execute('''INSERT INTO Usuarios (nombre, email, telefono) VALUES (?, ?, ?)''', ("Luis", "aaaaaa@gmail.com", 77744455))
    cursor.execute('''INSERT INTO Videojuegos (titulo, plataforma, stock) VALUES (?, ?, ?)''', ("ARK: Survival Ascended", "Steam,PS5,Xbox Series X/S", 10))
    cursor.execute('''INSERT INTO Prestamos (id_usuario, id_videojuego, fecha_prestamo, fecha_devolucion) VALUES (?, ?, ?, ?)''', (1, 1, "2024-07-22", "2024-09-25"))
    conexion.commit()
    conexion.close()

def insertar_usuario(nombre, email, telefono):
    conexion = conectar()
    conexion.execute('PRAGMA foreign_keys=ON')
    cursor = conexion.cursor()
    cursor.execute('''INSERT INTO Usuarios (nombre, email, telefono) VALUES (?, ?, ?)''', (nombre, email, telefono))
    print("Usuario agregado correctamente")
    conexion.commit()
    conexion.close()

def insertar_videojuego(titulo, plataforma, stock):
    conexion = conectar()
    conexion.execute('PRAGMA foreign_keys=ON')
    cursor = conexion.cursor()
    cursor.execute('''INSERT INTO Videojuegos (titulo, plataforma, stock) VALUES (?, ?, ?)''', (titulo, plataforma, stock))
    print("Usuario agregado correctamente")
    conexion.commit()
    conexion.close()

def insertar_prestamo(id_usuario, id_videojuego, fecha_prestamo, fecha_devolucion):
    conexion = conectar()
    conexion.execute('PRAGMA foreign_keys=ON')
    cursor = conexion.cursor()
    cursor.execute('''INSERT INTO Prestamos (id_usuario, id_videojuego, fecha_prestamo, fecha_devolucion) VALUES (?, ?, ?, ?)''', (id_usuario, id_videojuego, fecha_prestamo, fecha_devolucion))
    print("Prestamo agregado correctamente")
    conexion.commit()
    conexion.close()

def mostrar_usuarios():
    conexion = conectar()
    conexion.execute('PRAGMA foreign_keys=ON')
    cursor = conexion.cursor()
    cursor.execute('''SELECT * FROM Usuarios''')
    for fila in cursor.fetchall():
        print(fila)
    conexion.close()
    
def mostrar_videojuegos():
    conexion = conectar()
    conexion.execute('PRAGMA foreign_keys=ON')
    cursor = conexion.cursor()
    cursor.execute('''SELECT * FROM Videojuegos''')
    for fila in cursor.fetchall():
        print(fila)
    conexion.close()

def mostrar_prestamos():
    conexion = conectar()
    conexion.execute('PRAGMA foreign_keys=ON')
    cursor = conexion.cursor()
    cursor.execute('''SELECT * FROM Prestamos''')
    for fila in cursor.fetchall():
        print(fila)
    conexion.close()
def eliminar_usuario(id_usuario):
    conexion = conectar()
    conexion.execute('PRAGMA foreign_keys=ON')
    cursor = conexion.cursor()
    cursor.execute('''DELETE FROM Usuarios WHERE id_usuario = ?''', (id_usuario,))
    print("Usuario eliminado correctamente")
    conexion.commit()
    conexion.close()

def eliminar_videojuego(id_videojuego):
    conexion = conectar()
    conexion.execute('PRAGMA foreign_keys=ON')
    cursor = conexion.cursor()
    cursor.execute('''DELETE FROM Videojuegos WHERE id_videojuego = ?''', (id_videojuego,))
    print("Videojuego eliminado correctamente")
    conexion.commit()
    conexion.close()

def eliminar_prestamo(id_prestamo):
    conexion = conectar()
    conexion.execute('PRAGMA foreign_keys=ON')
    cursor = conexion.cursor()
    cursor.execute('''DELETE FROM Prestamos WHERE id_prestamo = ?''', (id_prestamo,))
    print("Prestamo eliminado correctamente")
    conexion.commit()
    conexion.close()

def modificar_usuarios(id_usuario, nombre, email, telefono):
    conexion = conectar()
    conexion.execute('PRAGMA foreign_keys=ON')
    cursor = conexion.cursor()
    cursor.execute('''UPDATE Usuarios SET nombre = ? WHERE id_usuario = ? ''', (nombre, id_usuario))
    cursor.execute('''UPDATE Usuarios SET email = ? WHERE id_usuario = ? ''', (email, id_usuario))
    cursor.execute('''UPDATE Usuarios SET telefono = ? WHERE id_usuario = ? ''', (telefono, id_usuario))
    print("Usuario modificado correctamente")
    conexion.commit()
    conexion.close()

def modificar_videojuegos(id_videojuego, titulo, plataforma, stock):
    conexion = conectar()
    conexion.execute('PRAGMA foreign_keys=ON')
    cursor = conexion.cursor()
    cursor.execute('''UPDATE Videojuegos SET titulo = ? WHERE id_videojuego = ? ''', (titulo, id_videojuego))
    cursor.execute('''UPDATE Videojuegos SET plataforma = ? WHERE id_videojuego = ? ''', (plataforma, id_videojuego))
    cursor.execute('''UPDATE Videojuegos SET stock = ? WHERE id_videojuego = ? ''', (stock, id_videojuego))
    print("Videojuego modificado correctamente")
    conexion.commit()
    conexion.close()

def modificar_prestamos(id_prestamo, fecha_prestamo, fecha_devolucion):
    conexion = conectar()
    conexion.execute('PRAGMA foreign_keys=ON')
    cursor = conexion.cursor()
    cursor.execute('''UPDATE Prestamos SET fecha_prestamo = ? WHERE id_prestamo = ? ''', (fecha_prestamo, id_prestamo))
    cursor.execute('''UPDATE Prestamos SET fecha_devolucion = ? WHERE id_prestamo = ? ''', (fecha_devolucion, id_prestamo))
    print("Prestamo modificado correctamente")
    conexion.commit()
    conexion.close()


def menu():
    crear_tablas()
    print("Binevenido a la gestión de prestamos de videojuegos")
    while True:
        print("\n1. Insertar usuario\n2. Insertar videojuego\n3. Insertar préstamo\n4. Mostrar usuarios\n5. Mostrar videojuegos\n6. Mostrar préstamos\n7. Eliminar usuario\n8. Eliminar videojuego\n9. Eliminar prestamo\n10. Actualizar usuario\n11. Actualizar videojuego\n12. Actualizar prestamo\n13. Salir")
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
            mostrar_videojuegos()
        elif opcion == "6":
            mostrar_prestamos()
        elif opcion == "7":
            eliminar_usuario(int(input("ID Usuario a eliminar: ")))
        elif opcion == "8":
            eliminar_videojuego(int(input("ID Préstamo a eliminar: ")))
        elif opcion == "9":
            eliminar_prestamo(int(input("ID Préstamo a eliminar: ")))
        elif opcion == "10":
            modificar_usuarios(int(input("ID Usuario a modificar: ")), input("Nombre: "), input("Email: "), input("Teléfono: "))
        elif opcion == "11":
            modificar_videojuegos(int(input("ID Videojuego a modificar: ")), input("Título: "), input("Plataforma: "), int(input("Stock: ")))
        elif opcion == "12":
            modificar_prestamos(int(input("ID Prestamo a modificar: ")), input("Fecha préstamo: "), input("Fecha devolución: "))
        elif opcion == "13":
            print("Saliendo del programa")
            break
        else:
            print("Opción no válida")

if __name__ == "__main__":
    menu()
