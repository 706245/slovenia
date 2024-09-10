from flask import render_template
from app import app
import  requests

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/history')
def history():
    return render_template('history.html')

@app.route('/player')
def player():
    return render_template('player.html')

@app.route('/fixtures')
def fixtures():
    return render_template('fixtures.html')


@app.route('/group')
def group():
    return render_template('group.html')
