from app.db.database import db

class Trabajador:
    
    def __init__(self, nombre="", apellidop="", apellidom="", telefono="", 
                 correo="", direccion="", rol="", sueldo=0, edad=0, id=None):
        self.id = id
        self.nombre = nombre
        self.apellidop = apellidop
        self.apellidom = apellidom
        self.telefono = telefono
        self.correo = correo
        self.direccion = direccion
        self.rol = rol
        self.sueldo = sueldo
        self.edad = edad
    
    def save(self):
        query = """
            INSERT INTO trabajadores 
            (nombre, apellidop, apellidom, telefono, correo, direccion, rol, sueldo, edad)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        """
        params = (self.nombre, self.apellidop, self.apellidom, self.telefono,
                 self.correo, self.direccion, self.rol, self.sueldo, self.edad)
        
        result = db.execute(query, params)
        if result is not None:
            # Obtener el ID asignado
            self.id = db.execute("SELECT last_insert_rowid()")[0][0]
            return True
        return False
    
    def get_all():
        query = "SELECT * FROM trabajadores"
        result = db.execute(query)
        
        if result:
            trabajadores = []
            for row in result:
                trabajador = Trabajador(
                    id=row[0],
                    nombre=row[1],
                    apellidop=row[2],
                    apellidom=row[3],
                    telefono=row[4],
                    correo=row[5],
                    direccion=row[6],
                    rol=row[7],
                    sueldo=row[8],
                    edad=row[9]
                )
                trabajadores.append(trabajador)
            return trabajadores
        return []
    
    def get_nombre_completo(self):
        return f"{self.nombre} {self.apellidop} {self.apellidom}"
    
    def to_dict(self):
        return {
            'id': self.id,
            'nombre': self.nombre,
            'apellidop': self.apellidop,
            'apellidom': self.apellidom,
            'telefono': self.telefono,
            'correo': self.correo,
            'direccion': self.direccion,
            'rol': self.rol,
            'sueldo': self.sueldo,
            'edad': self.edad,
            'nombre_completo': self.get_nombre_completo()
        }
