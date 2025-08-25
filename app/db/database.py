import sqlite3
import os

class Database:   
    def __init__(self, db_name="conttrol.db"):
        self.db_name = db_name
        self.connection = None
        self.cursor = None
    
    def connect(self):
        try:
            self.connection = sqlite3.connect(self.db_name)
            self.cursor = self.connection.cursor()
            return True
        except Exception as e:
            print(f"Error de conexión: {e}")
            return False
    
    def disconnect(self):
        if self.connection:
            self.connection.close()
    
    def create_tables(self):
        if self.connect():
            # Tabla de trabajadores
            self.cursor.execute('''
                CREATE TABLE IF NOT EXISTS trabajadores (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nombre TEXT NOT NULL,
                    apellidop TEXT NOT NULL,
                    apellidom TEXT NOT NULL,
                    telefono TEXT NOT NULL,
                    correo TEXT NOT NULL,
                    direccion TEXT NOT NULL,
                    rol TEXT NOT NULL,
                    sueldo REAL NOT NULL,
                    edad INTEGER NOT NULL
                )
            ''')
            self.cursor.execute('''
                CREATE TABLE IF NOT EXISTS usuarios (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    usuario TEXT UNIQUE NOT NULL,
                    contraseña TEXT NOT NULL,
                    rol TEXT NOT NULL
                )
            ''')
            
            self.connection.commit()
            self.disconnect()
    
    def execute(self, query, params=()):
        try:
            if self.connect():
                self.cursor.execute(query, params)
                if query.strip().upper().startswith('SELECT'):
                    result = self.cursor.fetchall()
                else:
                    self.connection.commit()
                    result = None
                self.disconnect()
                return result
        except Exception as e:
            print(f"Error en query: {e}")
            return None

# Instancia global
db = Database()
