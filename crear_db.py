import sqlite3

# Crear o conectar a la base de datos
conexion = sqlite3.connect("biblioteca.db")

cursor = conexion.cursor()

# Crear tabla autores
cursor.execute("""
CREATE TABLE IF NOT EXISTS autores (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    pais TEXT
)
""")

# Crear tabla libros
cursor.execute("""
CREATE TABLE IF NOT EXISTS libros (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    titulo TEXT NOT NULL,
    anio INTEGER,
    autor_id INTEGER,
    FOREIGN KEY (autor_id) REFERENCES autores(id)
)
""")

# Crear tabla usuarios
cursor.execute("""
CREATE TABLE IF NOT EXISTS usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    email TEXT UNIQUE
)
""")

# Crear tabla prestamos
cursor.execute("""
CREATE TABLE IF NOT EXISTS prestamos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    usuario_id INTEGER,
    libro_id INTEGER,
    fecha_prestamo DATE,
    fecha_devolucion DATE,
    FOREIGN KEY (usuario_id) REFERENCES usuarios(id),
    FOREIGN KEY (libro_id) REFERENCES libros(id)
)
""")

conexion.commit()
conexion.close()

print("Base de datos creada correctamente")