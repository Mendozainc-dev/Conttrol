from flask import Flask, render_template, request, redirect, url_for, session
from app.models.usuario import Usuario
from app.db.database import db
from app.controllers.menu_controller import menu_bp
from app.controllers.Trabajadores_controller import trabajadores_bp
from app.controllers.Contaduria_controller import contaduria_bp
from app.controllers.administracion_controller import administracion_bp

app = Flask(__name__)
app.secret_key = 'Mendozainc'
app.register_blueprint(menu_bp)
app.register_blueprint(trabajadores_bp)
app.register_blueprint(contaduria_bp)
app.register_blueprint(administracion_bp)

db.create_tables()

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/Login', methods=['POST'])
def login(): 
    usuario = request.form.get('Usuario')
    contraseña = request.form.get('Contraseña')
    
    if usuario and contraseña:
        user = Usuario.authenticate(usuario, contraseña)
        if user:
            session['user_id'] = user.id
            session['username'] = user.usuario
            session['user_role'] = user.rol
            session['is_authenticated'] = True
            
            return redirect(url_for('menu.menu'))
        else:
            return render_template('index.html', mensaje_error="Usuario o contraseña incorrectos")
    else:
        return render_template('index.html', mensaje_error="No se puede acceder no se han llenado los campos correctamente")

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))
    
if __name__=='__main__':
    app.run(debug=True, port=5000)