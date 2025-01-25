import random
import time
from flask import Flask, render_template, request, jsonify # type: ignore
from flask_cors import CORS # type: ignore

import subprocess

from flask_socketio import SocketIO, join_room, leave_room, emit # type: ignore

app = Flask(__name__)
CORS(app)
socketio = SocketIO(app)

lobbies = {}
lobbyEndTimes = {}

@socketio.on('create_lobby')
def handle_create_lobby(data):
    username = data.get('username')

    lobbyCode = random.randint(1000, 9999)
    while lobbyCode in lobbies:
        lobbyCode = random.randint(1000, 9999)

    lobbies[lobbyCode] = []

    lobbies[lobbyCode].append(username)
    join_room(lobbyCode)
    emit('lobby_created', {'lobbyCode': lobbyCode}, room=lobbyCode)

@socketio.on('join_lobby')
def handle_join_lobby(data):
    lobbyCode = data.get('lobbyCode')
    username = data.get('username')

    if lobbyCode not in lobbies:
        emit('error', {'error': 'Lobby not found'})
        return

    lobbies[lobbyCode].append(username)
    join_room(lobbyCode)
    emit('joined_lobby', username + ' has entered the room.', room=lobbyCode)

@socketio.on('leave_lobby')
def handle_leave_lobby(data):
    lobbyCode = data.get('lobbyCode')
    username = data.get('username')

    if lobbyCode not in lobbies:
        emit('error', {'error': 'Lobby not found'})
        return
    
    if username not in lobbies[lobbyCode]:
        emit('error', {'error': 'User not in lobby'})
        return

    lobbies[lobbyCode].remove(username)
    leave_room(lobbyCode)
    emit('left_lobby', username + ' has left the room.', room=lobbyCode)

@socketio.on('get-lobby-player-count')
def get_lobby_info(data):
    lobbyCode = data.get('lobbyCode')

    if lobbyCode not in lobbies:
        emit('error', {'error': 'Lobby not found'})
        return

    emit('lobby_player_count', {'player-count': len(lobbies[lobbyCode])})

@socketio.on('delete-lobby')
def delete_lobby(data):
    lobbyCode = data.get('lobbyCode')

    if lobbyCode not in lobbies:
        emit('error', {'error': 'Lobby not found'})
        return

    del lobbies[lobbyCode]

    emit('lobby_deleted', 'Lobby #' + lobbyCode + ' has been deleted.')

@socketio.on('get-lobbies')
def get_lobbies():
    emit('lobbies', {'lobbies': list(lobbies.keys())})

@socketio.on('start-game')
def start_game(data):
    lobbyCode = data.get('lobbyCode')
    if lobbyCode not in lobbies:
        return jsonify({'error': 'Lobby not found'})
    
    # TODO: Grab code from database
    competitionCode = 'print("Hello World")'
    
    time = 5

    lobbyEndTimes[lobbyCode] = time.time() + time

    socketio.emit('start-game', {'code': competitionCode, 'time': time}, room=lobbyCode)

    return jsonify({'success': True, 'time': time})

# @app.route('/execute', methods=['POST'])
# def execute_code():
#     data = request.get_json()
#     code = data.get('code', '')

#     try:
#         result = subprocess.run(['python', '-c', code], capture_output=True, text=True, check=True)
#         output = result.stdout
#         error = result.stderr
#     except subprocess.CalledProcessError as e:
#         output = e.stdout
#         error = e.stderr

#     return jsonify({'output': output, 'error': error})

if __name__ == '__main__':
    app.run(debug=True)
    socketio.run(app, debug=True)
