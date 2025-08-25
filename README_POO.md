# Conttrol - POO Básico

Implementación simple de **Programación Orientada a Objetos** en el proyecto Conttrol.

## 🏗️ Estructura POO Básica

```
app/
├── db/
│   └── database.py        # Clase Database básica
├── models/
│   ├── trabajador.py      # Clase Trabajador
│   ├── usuario.py         # Clase Usuario
│   └── __init__.py
└── controllers/           # Controladores actualizados
```

## 🔧 Clases Implementadas

### 1. **Clase Database**
```python
class Database:
    def __init__(self, db_name="conttrol.db"):
        self.db_name = db_name
    
    def connect(self):
        # Conecta a SQLite
    
    def execute(self, query, params=()):
        # Ejecuta consultas SQL
```

### 2. **Clase Trabajador**
```python
class Trabajador:
    def __init__(self, nombre, apellidop, apellidom, ...):
        # Constructor con atributos
    
    def save(self):
        # Guarda en base de datos
    
    def get_all():
        # Obtiene todos los trabajadores
    
    def get_nombre_completo(self):
        # Método de instancia
```

### 3. **Clase Usuario**
```python
class Usuario:
    def __init__(self, usuario, contraseña, rol):
        # Constructor
    
    def save(self):
        # Guarda usuario
    
    def authenticate(usuario, contraseña):
        # Método de clase para autenticación
```

## 🚀 Cómo usar

### 1. Crear usuarios de prueba
```bash
python crear_usuarios.py
```

### 2. Ejecutar la aplicación
```bash
python app/app.py
```

### 3. Acceder con:
- **admin/admin123** (Administrador)
- **usuario/usuario123** (Usuario)
- **contador/contador123** (Contador)

## 📊 Ejemplos de Uso POO

### Crear un trabajador
```python
trabajador = Trabajador(
    nombre="Juan",
    apellidop="Pérez",
    apellidom="García",
    telefono="555-0101",
    correo="juan@empresa.com",
    direccion="Av. Principal 123",
    rol="Desarrollador",
    sueldo=25000.00,
    edad=28
)
trabajador.save()
```

### Obtener todos los trabajadores
```python
trabajadores = Trabajador.get_all()
for t in trabajadores:
    print(t.get_nombre_completo())
```

### Autenticar usuario
```python
user = Usuario.authenticate("admin", "admin123")
if user:
    print(f"Bienvenido {user.usuario}")
```

## ✅ Ventajas del POO Básico

- **Organización**: Código estructurado en clases
- **Reutilización**: Métodos comunes en clases
- **Mantenimiento**: Fácil de modificar y extender
- **Base de datos**: Persistencia de datos real

## 🔄 Flujo de Datos

1. **Formulario** → Controlador
2. **Controlador** → Clase Modelo
3. **Modelo** → Base de datos
4. **Respuesta** → Vista

## 📈 Próximos pasos

- Agregar más métodos a las clases
- Implementar validaciones
- Crear más modelos (Contaduría, Administración)
- Agregar herencia entre clases
