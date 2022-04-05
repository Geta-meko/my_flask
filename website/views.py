from flask import Blueprint, request, render_template
from graphviz import view
from sympy import viete

views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template('home.html')
