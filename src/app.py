from flask import Flask, jsonify
from datetime import datetime
import socket
app = Flask(__name__)


@app.route('/api/v1/info')

def info():
    return jsonify ({
        'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'hostname': socket.gethostname(),
        'message': 'You are doing great! !!Jaiojasdasdsdiodasdadasdsdajsd',
        'deployed_on': 'kubernetes'
    })

@app.route('/api/v1/healthz')

def health():
    return jsonify({
        'status': 'ok'
    }), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0')





#'/api/v1/details'
#'/api/v1/healthz'