from flask import Flask, render_template, redirect,request,url_for, session, Blueprint

contaduria_bp = Blueprint('contaduria', __name__)

@contaduria_bp.route('/contaduria', methods=['GET', 'POST'])
def contaduria():
    if 'contaduria' not in session:
        session['Contaduria'] = []
    contaduria_lista = session['Contaduria']

    if request.method == 'POST':
        descripcion = request.form.get('Descripcion')
        producto_servicio = request.form.get('Producto_Servicio')
        monto = request.form.get('Monto')
        metodo_pago = request.form.get('Metodo_Pago')
        fecha = request.form.get('Fecha')
        cliente = request.form.get('Cliente')

        if descripcion and producto_servicio and monto and metodo_pago and fecha and cliente:
            contaduria = {
                'descripcion': descripcion,
                'producto_servicio': producto_servicio,
                'monto': monto,
                'metodo_pago': metodo_pago,
                'fecha': fecha,
                'cliente': cliente
            }
            contaduria_lista.append(contaduria)
            session['Contaduria'] = contaduria_lista
            mensaje_succes = f"El registro de {descripcion} por un monto de {monto} pesos mexicanos a nombre de {cliente} fue registrado correctamente el dia {fecha} con metodo de pago {metodo_pago}"
            return render_template('Contaduria.html', mensaje_succes=mensaje_succes, contaduria=contaduria_lista)
        else:
            mensaje_error = "No se pudo insertar un nuevo registro en contaduria favor de revisar que todos los campos esten llenos"
            return render_template('Contaduria.html', mensaje_error=mensaje_error, contaduria=contaduria_lista)

    return render_template('Contaduria.html', contaduria=contaduria_lista)