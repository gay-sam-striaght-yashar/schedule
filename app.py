from flask import Flask, session, request, url_for, redirect, render_template
from flask_cors import CORS
from flask_socketio import SocketIO, send, emit, join_room, leave_room
import uuid
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)
app.config['SESSION_TYPE'] = 'filesystem'
socketio = SocketIO(app)
CORS(app)



if __name__ == '__main__':
    app.run(port=4567, debug= True)