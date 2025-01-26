import random
import time
from flask import Flask, render_template, request, jsonify # type: ignore
from flask_cors import CORS # type: ignore
from check_code import check_code, parse_testcode_data
from vetted_problem import problems
import os

from gumloop import GumloopClient # type: ignore

import subprocess

from flask_socketio import SocketIO, join_room, leave_room, emit, send # type: ignore
from dotenv import load_dotenv # type: ignore
from supabase import Client, create_client # type: ignore
import os

load_dotenv()

client = GumloopClient(
    api_key=os.environ.get("GUMLOOP_API_KEY"),
    user_id=os.environ.get("GUMLOOP_USER_ID")
)

url: str = os.environ.get("SUPABASE_URL")
key: str = os.environ.get("SUPABASE_KEY")
supabase: Client = create_client(url, key)

app = Flask(__name__)
CORS(app)
socketio = SocketIO(app, cors_allowed_origins="*")

lobbies = {}
lobbyEndTimes = {}
lobbyProblemIndices = {}
lobbyRawData = {}

sample = {'code': "def find_winner(board):\n    for i in range(3):\n        if board[i][0] == board[i][1] == board[i][2] != '-':\n            return board[i][0]\n        elif board[0][i] == board[1][i] == board[2][i] != '-':\n            return board[0][i]\n    if board[0][0] == board[1][1] == board[2][2] != '-':\n        return board[0][0]\n    elif board[0][2] == board[1][1] == board[2][0] != '-':\n        return board[2][0]\n    if '-' not in board:\n        return 'Draw'\n    return 'No Winner'", 'description': 'The code block determines the winner (or a draw) of a tic-tac-toe game based on the given board.', 'testCases': ['[', "[['X', 'X', 'X', '-', '-', '-', '-', '-', '-'], 'X'],", "[['O', 'O', 'O', '-', '-', '-', '-', '-', '-'], 'O'],", "[['X', 'O', 'X', 'O', 'X', 'O', 'O', 'X', 'X'], 'Draw'],", "[['-', '-', '-', '-', '-', '-', '-', '-', '-'], 'No Winner'],", "[['X', 'O', '-', 'O', 'X', '-', 'X', '-', '-'], 'X']", ']']}

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
    print(data)
    print("Hello World!")

    #join_room(lobbyCode)
    emit('joined_lobby', username + ' has entered the room.', to=lobbyCode)
    if lobbyCode not in lobbies:
        emit('error', {'error': 'Lobby not found'})
        return
    
    join_room(str(lobbyCode))
    
    if username in lobbies[lobbyCode]:
        emit('error', {'error': 'User already in lobby'})
        return

    lobbies[lobbyCode].append(username)
    emit('joined_lobby', username, to=str(lobbyCode))

@socketio.on('leave_lobby')
def handle_leave_lobby(data):
    lobbyCode = data.get('lobbyCode')
    username = data.get('username')
    #print(data)

    if lobbyCode not in lobbies:
        emit('error', {'error': 'Lobby not found'})
        return
    
    if username not in lobbies[lobbyCode]:
        emit('error', {'error': 'User not in lobby'})
        return

    lobbies[lobbyCode].remove(username)

    if len(lobbies[lobbyCode]) == 0:
        del lobbies[lobbyCode]
        del lobbyEndTimes[lobbyCode]
        del lobbyProblemIndices[lobbyCode]
        del lobbyRawData[lobbyCode]

    leave_room(lobbyCode)
    emit('left_lobby', username, to=str(lobbyCode))

@app.route('/get-lobby-player-count/<int:lobbyCode>', methods=['GET'])
def get_lobby_info(lobbyCode):
    if lobbyCode not in lobbies:
        return jsonify({'error': 'Lobby not found'})

    return jsonify({'player-count': len(lobbies[lobbyCode])})

@app.route('/get-lobby-players/<int:lobbyCode>', methods=['GET'])
def get_lobby_players(lobbyCode):
    print(lobbyCode)
    print(lobbies)
    if lobbyCode not in lobbies:
        return jsonify({'error': 'Lobby not found'})
    if lobbyCode in lobbyEndTimes:
        return jsonify({'players': lobbies[lobbyCode], 'started': True, 'time': round(lobbyEndTimes[lobbyCode] - time.time()), 'code': problems[lobbyProblemIndices[lobbyCode]]["code"]})

    return jsonify({'players': lobbies[lobbyCode], 'started': False})

@app.route('/delete-lobby/<int:lobbyCode>', methods=['POST'])
def delete_lobby(lobbyCode):
    if lobbyCode not in lobbies:
        return jsonify({'error': 'Lobby not found'})

    del lobbies[lobbyCode]
    del lobbyEndTimes[lobbyCode]
    del lobbyProblemIndices[lobbyCode]
    del lobbyRawData[lobbyCode]
    return jsonify({'success': True})

@app.route('/get-lobbies', methods=['GET'])
def get_lobbies():
    return jsonify({'lobbies': [key for key in lobbies.keys() if key not in lobbyEndTimes]})

@app.route('/start-game/<int:lobbyCode>', methods=['POST'])
def start_game(lobbyCode):
    # print(lobbyCode, lobbies)
    if lobbyCode not in lobbies:
        return jsonify({'error': 'Lobby not found'})
    
    # TODO: Grab code from database
    # outputCode = client.run_flow(
    #     flow_id="jyTN43gYcSfcSJxJ4Y8cdn",
    #     inputs={
    #         "prompt": "Largest Triangle Area"
    #     }
    # )

    # while(parse_testcode_data(outputCode)[2]):
    #     outputCode = client.run_flow(
    #         flow_id="jyTN43gYcSfcSJxJ4Y8cdn",
    #         inputs={
    #             "prompt": "Largest Triangle Area"
    #         }
    #     )

    outputCode = problems[random.randint(0, len(problems) - 1)]
    
    competitionCode = outputCode["code"] + "\n# " + outputCode["description"]
    lobbyRawData[lobbyCode] = outputCode
    
    duration = 240 # 300

    lobbyEndTimes[lobbyCode] = time.time() + duration
    lobbyProblemIndices[lobbyCode] = random.randint(0, len(problems) - 1)
    # competitionCode = problems[lobbyProblemIndices[lobbyCode]]["code"]

    socketio.emit('start-game', {'code': competitionCode, 'time': duration}, to=str(lobbyCode))

    return jsonify({'success': True, 'time': duration})

@app.route('/end-game/<int:lobbyCode>', methods=['POST'])
def end_game(lobbyCode):
    if lobbyCode not in lobbies:
        return jsonify({'error': 'Lobby not found'})
    
    if lobbyCode not in lobbyEndTimes:
        return jsonify({'error': 'Game not started'})

    lobbyEndTimes[lobbyCode] = 0
    socketio.emit('end-game', to=str(lobbyCode))

    return jsonify({'success': True})

@app.route('/submission/<int:lobbyCode>', methods=['POST'])
def submission(lobbyCode):
    data = request.get_json()
    username = data.get('username', '')
    submission = data.get('submission', '')

    if lobbyCode not in lobbies:
        return jsonify({'error': 'Lobby not found'})
    
    if username not in lobbies[lobbyCode]:
        return jsonify({'error': 'User not in lobby'})

    if time.time() > lobbyEndTimes[lobbyCode] + 500:
        return jsonify({'error': 'Time is up!'})
    

    
    #========================================================================================================
    # TODO: Check submission
    code = submission
    #raw_data = {'code': 'def find_missing_number(numbers):\n    expected_sum = sum(range(1, len(numbers) + 1))\n    actual_sum = sum(numbers)\n    return expected_sum - actual_sum', 'description': 'The function finds the missing number in a list of consecutive integers.', 'testCases': ['[[1, 2, 3, 4, 6], [10, 11, 12, 13, 14, 15, 16, 17, 18, 19], [1, 2, 3, 4, 5], [100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]]', '[5, 10, 6, 55, 12]']}
    # raw_data = {'code': 'def find_missing_number(numbers):\n    expected_sum = sum(range(1, len(numbers) + 1))\n    actual_sum = sum(numbers)\n    return expected_sum - actual_sum', 'description': 'The function finds the missing number in a list of consecutive integers.', 'testCases': ['[[1, 2, 3, 4, 6], [9, 11, 12, 13, 14, 15, 16, 17, 18, 19], [1, 2, 3, 4, 5, 7]]', '[5, 10, 6]']}
    # raw_data = problems[lobbyProblemIndices[lobbyCode]]
    raw_data = lobbyRawData[lobbyCode]

    given_input, given_output, parse_error = parse_testcode_data(raw_data)
    result = check_code(code, given_input, given_output)
    if (parse_error):
        result.errors = 1
    
    supabase.table("scores").insert({ "name": username, "seconds": round(lobbyEndTimes[lobbyCode] - time.time()) }).execute()
    
    #try:
    #    result = subprocess.run(['python', '-c', code], capture_output=True, text=True, check=True)
    #    output = result.stdout
    #    error = result.stderr
    #except subprocess.CalledProcessError as e:
    #    output = e.stdout
    #    error = e.stderr

    # TODO: Compare output with test cases from sample
    if (result.errors == 1):
        print("CRITICAL SERVER ERROR")
    elif (result.errors == 2):
        print("UNABLE TO FIND FUNCTION DEFINITION")
    score = result.get_overall_state()
    print(result.get_dump())
    #========================================================================================================

    socketio.emit('submission', {'username': username, 'score': score}, to=str(lobbyCode))

    return jsonify({'success': score[0] == score[1]})

@app.route('/leaderboard', methods=['GET'])
def leaderboard():
    response = supabase.table("scores").select("*").limit(10).order("seconds", desc=True).execute().data
    return jsonify({'scores': [{"name": row["name"], "seconds": row["seconds"]} for row in response]})

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
    socketio.run(app, host=os.environ.get("HOST"), debug=True, port=3001, allow_unsafe_werkzeug=True)
