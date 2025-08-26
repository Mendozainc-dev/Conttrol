from flask import Flask, render_template, redirect,request,url_for, session, Blueprint

contaduria_bp = Blueprint('contaduria', __name__)

def login_required(f):
    def decorated_function(*args, **kwargs):
        if not session.get('is_authenticated'):
            return redirect(url_for('index'))
        return f(*args, **kwargs)
    decorated_function.__name__ = f.__name__
    return decorated_function

@contaduria_bp.route('/Contaduria', methods=['GET', 'POST'])
@login_required
def contaduria():
    if 'contaduria' not in session:
        session['contaduria'] = []
    contaduria_lista = session['contaduria']

    if request.method == 'POST':
        descripcion = request.form.get('Descripcion')
        producto_servicio = request.form.get('Producto_Servicio')
        monto = request.form.get('Monto')
        metodo_pago = request.form.get('Metodo_Pago')
        fecha = request.form.get('Fecha')
        cliente = request.form.get('Cliente')

        if descripcion and producto_servicio and monto and metodo_pago and fecha and cliente:
            registro = {
                'Descripcion': descripcion,
                'Producto_Servicio': producto_servicio,
                'Monto': monto,
                'Metodo_Pago': metodo_pago,
                'Fecha': fecha,
                'Cliente': cliente
            }
            contaduria_lista.append(registro)
            session['contaduria'] = contaduria_lista
            mensaje_succes = f"El registro de {descripcion} por un monto de {monto} pesos mexicanos a nombre de {cliente} fue registrado correctamente el día {fecha} con método de pago {metodo_pago}."
            return render_template('contaduria.html', mensaje_succes=mensaje_succes, ingresos=contaduria_lista)
        else:
            mensaje_error = "No se pudo insertar un nuevo registro en contaduría."
            return render_template('contaduria.html', mensaje_error=mensaje_error, ingresos=contaduria_lista)

    return render_template('contaduria.html', ingresos=contaduria_lista)