from app.db.database import db

class Usuario:
    def __init__(self, usuario="", contraseña="", rol="usuario", id=None):
        self.id = id
        self.usuario = usuario
        self.contraseña = contraseña
        self.rol = rol

    def save(self):
        query = "INSERT INTO usuarios (usuario, contraseña, rol) VALUES (?, ?, ?)"
        params = (self.usuario, self.contraseña, self.rol)
        
        result = db.execute(query, params)
        if result is not None:
            self.id = db.execute("SELECT last_insert_rowid()")[0][0]
            return True
        return False
    
    def authenticate(usuario, contraseña):
        query = "SELECT * FROM usuarios WHERE usuario=? AND contraseña=?"
        result = db.execute(query, (usuario, contraseña))
        
        if result and result[0]:
            row = result[0]
            return Usuario(
                id=row[0],
                usuario=row[1],
                contraseña=row[2],
                rol=row[3]
            )
        return None
    
    def get_all():
        query = "SELECT * FROM usuarios"
        result = db.execute(query)
        
        if result:
            usuarios = []
            for row in result:
                usuario = Usuario(
                    id=row[0],
                    usuario=row[1],
                    contraseña=row[2],
                    rol=row[3]
                )
                usuarios.append(usuario)
            return usuarios
        return []
    
    def is_admin(self):
        return self.rol.lower() == "administrador"
    
    def to_dict(self):
        return {
            'id': self.id,
            'usuario': self.usuario,
            'rol': self.rol,
            'es_admin': self.is_admin()
        }
