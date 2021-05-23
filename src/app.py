import os
from flask import Flask, jsonify, request

app = Flask(__name__)


def get_audio_files(full_path=False):
    """Returns a list of available audio files"""
    audio_dir = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'audio')
    files = [x for x in os.listdir(audio_dir) if str(x).endswith('.mp3')]
    if full_path:
        return [os.path.join(audio_dir, x) for x in files]
    return files


def play_audio_file(path):
    """Plays the audio file"""
    base = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'audio')
    path = path.replace(' ', '')
    path = os.path.join(base, path)
    cmd = f'mpg321 {path}'
    print(f'Playing {path}')
    os.system(cmd)


@app.route('/')
def index():
    """Index route"""
    routes = ['/play/' + x for x  in get_audio_files()]
    context = {
        'status': 'ok',
        'routes': routes
    }
    return jsonify(context)


@app.route('/play/<file>')
def play(file):
    """Play a file"""
    if file in get_audio_files():
        play_audio_file(file)
        return jsonify({'status': 'ok'})
    return jsonify({'status': 'error'})


if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=int(os.environ.get('PORT', '8000')))
