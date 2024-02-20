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
            'output': result.stdout
        }
    except subprocess.CalledProcessError as e:
        response = {
            'status': 'error',
            'error': e.stderr
        }

    return jsonify(response)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
