import random
import time
from flask import Flask, render_template, request, jsonify # type: ignore
from flask_cors import CORS # type: ignore

import subprocess

from flask_socketio import SocketIO, join_room, leave_room, emit, send # type: ignore

app = Flask(__name__)
CORS(app)
socketio = SocketIO(app, cors_allowed_origins="*")

lobbies = {}
lobbyEndTimes = {}

@app.route('/create-lobby', methods=['POST'])
def create_lobby():
    lobbyCode = random.randint(1000, 9999)
    while lobbyCode in lobbies:
        lobbyCode = random.randint(1000, 9999)

    lobbies[lobbyCode] = []
    return jsonify({'lobbyCode': lobbyCode})

@socketio.on('join_lobby')
def handle_join_lobby(data):
    lobbyCode = data.get('lobbyCode')
    username = data.get('username')

    # join_room(lobbyCode)
    # emit('joined_lobby', username + ' has entered the room.', to=lobbyCode)

    if lobbyCode not in lobbies:
        emit('error', {'error': 'Lobby not found'})
        return

    lobbies[lobbyCode].append(username)
    join_room(lobbyCode)
    emit('joined_lobby', username + ' has entered the room.', to=lobbyCode)

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

    if len(lobbies[lobbyCode]) == 0:
        del lobbies[lobbyCode]

    leave_room(lobbyCode)
    emit('left_lobby', username + ' has left the room.', room=lobbyCode)

@app.route('/get-lobby-player-count/<int:lobbyCode>', methods=['GET'])
def get_lobby_info(lobbyCode):
    if lobbyCode not in lobbies:
        return jsonify({'error': 'Lobby not found'})

    return jsonify({'player-count': len(lobbies[lobbyCode])})

@app.route('/get-lobby-players/<int:lobbyCode>', methods=['GET'])
def get_lobby_players(lobbyCode):
    if lobbyCode not in lobbies:
        return jsonify({'error': 'Lobby not found'})

    return jsonify({'players': lobbies[lobbyCode]})

@app.route('/delete-lobby/<int:lobbyCode>', methods=['POST'])
def delete_lobby(lobbyCode):
    if lobbyCode not in lobbies:
        return jsonify({'error': 'Lobby not found'})

    del lobbies[lobbyCode]
    return jsonify({'success': True})

@app.route('/get-lobbies', methods=['GET'])
def get_lobbies():
    return jsonify({'lobbies': list(lobbies.keys())})

@app.route('/start-game/<int:lobbyCode>', methods=['POST'])
def start_game(lobbyCode):
    if lobbyCode not in lobbies:
        return jsonify({'error': 'Lobby not found'})
    
    # TODO: Grab code from database
    competitionCode = 'print("Hello World")'
    
    time = 300

    lobbyEndTimes[lobbyCode] = time.time() + time

    socketio.emit('start-game', {'code': competitionCode, 'time': time}, room=lobbyCode)

    return jsonify({'success': True, 'time': time})

@app.route('/submission/<int:lobbyCode>', methods=['POST'])
def submission(lobbyCode):
    data = request.get_json()
    username = data.get('username', '')
    submission = data.get('submission', '')

    if lobbyCode not in lobbies:
        return jsonify({'error': 'Lobby not found'})
    
    if username not in lobbies[lobbyCode]:
        return jsonify({'error': 'User not in lobby'})

    if time.time() > lobbyEndTimes[lobbyCode] + 30:
        return jsonify({'error': 'Time is up!'})
    
    # TODO: Check submission
    sampleResult = (5, 7)

    socketio.emit('submission', {'username': username, 'result': sampleResult}, room=lobbyCode)

    return jsonify({'success': True})

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
    # app.run(debug=True)
    socketio.run(app, debug=True, port=3001)
