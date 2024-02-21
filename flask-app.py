#보안에 상당히 취약하다. 수정예정
from flask import Flask, request, jsonify
from flask_cors import CORS
import subprocess
import shlex

app = Flask(__name__)
CORS(app)

@app.route('/tts')
def run_tts():
    tts = request.args.get('tts', default='')
    ttsid = request.args.get('ttsid', default='')
    uid = request.args.get('uid', default='')
    vid = request.args.get('vid', default='')
    pitch = request.args.get('pitch', default='')

    script_path = '../tts_all.py'

    command = f'python {script_path} --tts "{tts}" --ttsid {ttsid} --uid {uid} --vid {vid} --pitch {pitch}'
    args = shlex.split(command)

    try:
        result = subprocess.run(args, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        response = {
            'status': 'success',
            'output': result.stdout,
            'exit_code': 0
        }
    except subprocess.CalledProcessError as e:
        response = {
            'status': 'error',
            'error': e.stderr,
            'exit_code': 1
        }

    return jsonify(response)

@app.route('/merge')
def run_merge():
    uid1 = request.args.get('uid1', default='')
    vid1 = request.args.get('vid1', default='')
    vid2 = request.args.get('vid2', default='')
    vid3 = request.args.get('vid3', default='')

    script_path = '../merge.py'

    command = f'python {script_path} {uid1} {vid1} {vid2} {vid3}'
    args = shlex.split(command)
    
    try:
        result = subprocess.run(args, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        response = {
            'status': 'success',
            'output': result.stdout,
            'exit_code': 0
        }
    except subprocess.CalledProcessError as e:
        response = {
            'status': 'error',
            'error': e.stderr,
            'exit_code': 1
        }
    
    return jsonify(response)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
