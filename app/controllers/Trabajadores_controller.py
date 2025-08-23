
from flask import Blueprint, render_template, redirect, url_for, request

trabajadores_bp = Blueprint('trabajadores', __name__)


@trabajadores_bp.route('/Trabajadores', methods=['GET', 'POST'])
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
		if nombre and apellidop and apellidom and telefono and correo and direccion and rol and edad and sueldo:
			mensaje_succes = f"La persona {nombre}, {apellidop}, {apellidom} fue registrado correctamente en el area de {rol} con un sueldo mensual de {sueldo} pesos mexicanos mensuales"
			return render_template('trabajadores.html', mensaje_succes=mensaje_succes)
		else:
			mensaje_error = "No se pudo insertar un nuevo trabajador."
			return render_template('trabajadores.html', mensaje_error=mensaje_error)
	return render_template('trabajadores.html')
