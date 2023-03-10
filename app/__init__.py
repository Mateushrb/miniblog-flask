from flask import Flask, render_template
app = Flask(__name__, template_folder='static')
app.config['SECRET_KEY'] = 'SECRET'
from app import routes