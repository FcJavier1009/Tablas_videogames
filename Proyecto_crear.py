import sqlite3

conexion = sqlite3.connect("videojuegos.db")
cursor = conexion.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS Usuarios (
        id_usuario INTERGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        email TEXT UNIQUE NOT NULL,
        telefono TEXT
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS Videojuegos (
        id_videjuego INTERGER PRIMARY KEY AUTOINCREMENT,
        titulo TEXT NOT NULL,
        plataforma TEXT UNIQUE NOT NULL,
        stock INTERGER NOT NULL
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS Prestamos (
        id_prestamo INTERGER PRIMARY KEY AUTOINCREMENT,
        id_usuario TEXT NOT NULL,
        email TEXT UNIQUE NOT NULL,
        telefono TEXT
    )
''')
