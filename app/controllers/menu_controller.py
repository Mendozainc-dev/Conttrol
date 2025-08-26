from flask import Blueprint, render_template, session, redirect, url_for

menu_bp = Blueprint('menu', __name__)

def login_required(f):
    def decorated_function(*args, **kwargs):
        if not session.get('is_authenticated'):
            return redirect(url_for('index'))
        return f(*args, **kwargs)
    decorated_function.__name__ = f.__name__
    return decorated_function

@menu_bp.route('/menu')
@login_required
def menu():
    return render_template('menu.html')

@menu_bp.route('/administrador')
@login_required
def administrador():
    return render_template ('administrador.html')

@menu_bp.route('/trabajadores')
@login_required
def trabajadores():
    return render_template('trabajadores.html')

@menu_bp.route('/contaduria')
@login_required
def contaduria():
    return render_template('contaduria.html')

