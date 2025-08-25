from flask import Flask, render_template, redirect, request, url_for, session, Blueprint

administracion_bp = Blueprint('administracion', __name__)

@administracion_bp.route('/Administracion' , methods=['GET', 'POST'])

def administracion():
    if 'administracion' not in session:
        session['administracion'] = []
    administracion_lista = session['administracion']

    if request.method == 'POST':
        gestion = request.form.get('Gestion')
        roles = request.form.get('Roles')
        empresa = request.form.get('Empresa')
        informes = request.form.get('Informes')
        usuarios = request.form.get('Usuarios')
        if gestion and roles and empresa and informes and usuarios:
            administracion = {
                'gestion': gestion,
                'roles': roles,
                'empresa': empresa,
                'informes': informes,
                'usuarios': usuarios
            }
            administracion_lista.append(administracion)
            session['administracion'] = administracion_lista
            mensaje_succes = f'El tipo de gestión {gestion}, roles {roles} y empresa {empresa} se registraron correctamente, además los informes {informes} y el usuario {usuarios} están definidos correctamente.'
            return render_template('administrador.html', mensaje_succes=mensaje_succes, administracion=administracion_lista)
        else:
            mensaje_error = "No se pudo insertar el registro en administración."
            return render_template('administrador.html', mensaje_error=mensaje_error, administracion=administracion_lista)

    return render_template('administrador.html', administracion=administracion_lista)
        
