from flask import Flask, session, request, url_for, redirect, render_template
from flask_cors import CORS
from flask_socketio import SocketIO, send, emit, join_room, leave_room
import uuid
import os
from data import *

# Get the current Jalali date




app = Flask(__name__)
app.secret_key = os.urandom(24)
app.config['SESSION_TYPE'] = 'filesystem'
socketio = SocketIO(app)
CORS(app)

@app.route('/checkLogin', methods=['POST'])
def checkLogin():
    name = request.form.get('name')
    password = request.form.get('password')
    if read_user_by_id(name, password):
        session['user'] = name
        return redirect(url_for('home'))
    return redirect(url_for('login'))
@app.route('/')
def home():
    user = session.get('user', '')
    return render_template('index.html', user=user)
@app.route('/login')
def login():
    return render_template('login.html')

@socketio.on('update')
def update():
    pass

if __name__ == '__main__':
    app.run(port=4567, debug= True)