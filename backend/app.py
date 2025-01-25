from flask import Flask, request, jsonify
import subprocess

app = Flask(__name__)

@app.route('/execute', methods=['POST'])
def execute_code():
    data = request.get_json()
    code = data.get('code', '')

    try:
        result = subprocess.run(['python', '-c', code], capture_output=True, text=True, check=True)
        output = result.stdout
        error = result.stderr
    except subprocess.CalledProcessError as e:
        output = e.stdout
        error = e.stderr

    return jsonify({'output': output, 'error': error})

if __name__ == '__main__':
    app.run(debug=True)
