from flask import Flask, render_template, request, redirect, url_for

app=Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/Login', methods=['POST'])
def login(): 
    usuario = request.form.get('Usuario')
    contraseña = request.form.get('Contraseña')
    if usuario and contraseña:
        return redirect(url_for('menu'))
    else:
        return render_template('index.html', mensaje_error="No se puede acceder no se han llenado los campos correctamente")
    
@app.route('/menu')
def menu():
    return render_template('menu.html')

if __name__=='__main__':
    app.run(debug=True, port=5000) 