import sqlite3

conexion = sqlite3.connect("videojuegos.db")
cursor = conexion.cursor()


cursor.execute('''
    CREATE TABLE IF NOT EXISTS Usuarios (
        id_usuario INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        email TEXT UNIQUE NOT NULL,
        telefono TEXT
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS Videojuegos (
        id_videjuego INTEGER PRIMARY KEY AUTOINCREMENT,
        titulo TEXT NOT NULL,
        plataforma TEXT UNIQUE NOT NULL,
        stock INTEGER NOT NULL
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS Prestamos (
        id_prestamo INTEGER PRIMARY KEY AUTOINCREMENT,
        id_usuario INTEGER NOT NULL,
        id_videojuego INTEGER NOT NULL,
        fecha_prestamo TEXT NOT NULL,
        fecha_devolucion TEXT NOT NULL,
        FOREIGN KEY (id_usuario) REFERENCES Usuarios(id_usuario),
        FOREIGN KEY (id_videojuego) REFERENCES Videojuegos(id_videojuego)
    )
''')

conexion.commit()
conexion.close()