from flask import Flask, render_template, redirect, request, url_for, session, Blueprint

administracion_bp = Blueprint('administracion', __name__)

@administracion_bp.route('/Administracion' , methods=['GET', 'POST'])
def administracion():

