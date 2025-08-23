from flask import Blueprint, render_template

menu_bp = Blueprint('menu', __name__)

@menu_bp.route('/menu')
def menu():
    return render_template('menu.html')

@menu_bp.route('/administrador')
def administrador():
    return render_template ('administrador.html')

@menu_bp.route('/trabajadores')
def trabajadores():
    return render_template('trabajadores.html')

@menu_bp.route('/contaduria')
def contaduria():
    return render_template('contaduria.html')

