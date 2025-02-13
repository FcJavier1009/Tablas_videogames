import sqlite3

def conectar():
    return sqlite3.connect("videojuegos.db")

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
    print("Usuario agregado correctamente")
    conexion.commit()
    conexion.close()
    
def mostrar_usuarios():
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM Usuarios")
    for fila in cursor.fetchall():
        print(fila)
    conexion.close()
    
def eliminar_usuario(id_usuario):
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("DELETE FROM Usuarios WHERE id_usuario = ?", (id_usuario,))
    print("Usuario eliminado correctamente")
    conexion.commit()
    conexion.close()

def menu():
    crear_tablas()
    while True:
        print("\n1. Insertar usuario\n2. Insertar videojuego\n3. Insertar préstamo\n4. Mostrar usuarios\n5. Eliminar usuario\n6. Eliminar préstamo\n7. Salir")
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