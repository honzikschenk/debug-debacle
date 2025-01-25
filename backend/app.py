import random
from flask import Flask, request, jsonify
import subprocess

app = Flask(__name__)

lobbies = {}

@app.route('/create-lobby', methods=['POST'])
def create_lobby():
    code = random.randint(1000, 9999)
    while code in lobbies:
        code = random.randint(1000, 9999)

    lobbies[code] = []
    return jsonify({'lobby-code': code})

@app.route('/join-lobby/<int:code>', methods=['POST'])
def join_lobby(code):
    data = request.get_json()
    username = data.get('username', '')

    if code not in lobbies:
        return jsonify({'error': 'Lobby not found'})

    lobbies[code].append(username)
    return jsonify({'success': True})

@app.route('/get-lobby-info/<int:code>', methods=['GET'])
def get_lobby_info(code):
    if code not in lobbies:
        return jsonify({'error': 'Lobby not found'})

    return jsonify({'players': lobbies[code]})

@app.route('/delete-lobby/<int:code>', methods=['POST'])
def delete_lobby(code):
    if code not in lobbies:
        return jsonify({'error': 'Lobby not found'})

    del lobbies[code]
    return jsonify({'success': True})

@app.route('/start-game/<int:code>', methods=['POST'])
def start_game(code):
    if code not in lobbies:
        return jsonify({'error': 'Lobby not found'})
    
    # Start the game

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
    app.run(debug=True)
