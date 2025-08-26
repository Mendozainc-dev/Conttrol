
from app.db.database import db
from app.models.usuario import Usuario

def crear_usuarios_prueba():
    print("Creando usuarios de prueba...")
    
    db.create_tables()
    
    usuarios = [
        {"usuario": "admin", "contraseña": "admin123", "rol": "administrador"},
 
    ]
    
    for user_data in usuarios:
        existing = Usuario.authenticate(user_data["usuario"], user_data["contraseña"])
        if not existing:
            user = Usuario(**user_data)
            if user.save():
                print(f" Usuario {user_data['usuario']} creado")
            else:
                print(f" Error al crear {user_data['usuario']}")
        else:
            print(f"- Usuario {user_data['usuario']} ya existe")
    
    print("\nUsuarios de prueba creados!")
    print("Credenciales:")
    print("admin/admin123 (Administrador)")

if __name__ == "__main__":
    crear_usuarios_prueba()
