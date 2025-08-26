
from flask import Blueprint, render_template, redirect, url_for, request, session
from app.models.trabajador import Trabajador

trabajadores_bp = Blueprint('trabajadores', __name__)

def login_required(f):
    def decorated_function(*args, **kwargs):
        if not session.get('is_authenticated'):
            return redirect(url_for('index'))
        return f(*args, **kwargs)
    decorated_function.__name__ = f.__name__
    return decorated_function

@trabajadores_bp.route('/Trabajadores', methods=['GET', 'POST'])
@login_required
def trabajadores():
    if request.method == 'POST':
        nombre = request.form.get('Nombre')
        apellidop = request.form.get('Apellidop')
        apellidom = request.form.get('Apellidom')
        telefono = request.form.get('Telefono')
        correo = request.form.get('Correo')
        direccion = request.form.get('Direccion')
        rol = request.form.get('Rol')
        sueldo = request.form.get('Sueldo')
        edad = request.form.get('Edad')
        if all([nombre, apellidop, apellidom, telefono, correo, direccion, rol, edad, sueldo]):
            trabajador = Trabajador(
                nombre=nombre,
                apellidop=apellidop,
                apellidom=apellidom,
                telefono=telefono,
                correo=correo,
                direccion=direccion,
                rol=rol,
                sueldo=float(sueldo),
                edad=int(edad)
            )
            
            if trabajador.save():
                mensaje_succes = f"La persona {trabajador.get_nombre_completo()} fue registrado correctamente en el área de {rol} con un sueldo mensual de {sueldo} pesos mexicanos mensuales"
            else:
                mensaje_error = "Error al guardar el trabajador en la base de datos"
                return render_template('trabajadores.html', mensaje_error=mensaje_error, trabajadores=Trabajador.get_all())
        else:
            mensaje_error = "No se pudo insertar un nuevo trabajador"
            return render_template('trabajadores.html', mensaje_error=mensaje_error, trabajadores=Trabajador.get_all())
    
    trabajadores_lista = Trabajador.get_all()
    
    return render_template('trabajadores.html', trabajadores=trabajadores_lista)
