from threading import Thread
from flask import Flask, render_template, request, jsonify, send_from_directory
import behavior_zero as behavior

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/leg', methods=['POST'])
def leg():
    data: dict = request.get_json()
    angle = data.get('angle')
    behavior.leg(angle)
    return jsonify(status='OK')


@app.route('/left', methods=['POST'])
def left():
    behavior.left()
    return jsonify(status='OK')


@app.route('/right', methods=['POST'])
def right():
    behavior.right()
    return jsonify(status='OK')


@app.route('/head', methods=['POST'])
def head():
    behavior.head()
    return jsonify(status='OK')


@app.route('/jiggly', methods=['POST', 'GET'])
def jiggly():
    behavior.JIGGLY_FLAG.value = not behavior.JIGGLY_FLAG.value
    return jsonify(status='OK')


@app.route('/_next/<path:filename>')
def _next_static(filename):
    return send_from_directory('./templates/_next', filename)


if __name__ == '__main__':
    Thread(target=behavior.jiggly).start()
    app.run(host='0.0.0.0', port=5000)
