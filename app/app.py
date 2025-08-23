from flask import Flask, render_template, request, redirect, url_for

from app.controllers.menu_controller import menu_bp
from app.controllers.Trabajadores_controller import trabajadores_bp


app = Flask(__name__)
app.register_blueprint(menu_bp)
app.register_blueprint(trabajadores_bp)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/Login', methods=['POST'])
def login(): 
    usuario = request.form.get('Usuario')
    contraseña = request.form.get('Contraseña')
    if usuario and contraseña:
        return redirect(url_for('menu.menu'))
    else:
        return render_template('index.html', mensaje_error="No se puede acceder no se han llenado los campos correctamente")
    
if __name__=='__main__':
    app.run(debug=True, port=5000)