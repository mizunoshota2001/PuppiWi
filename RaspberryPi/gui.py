from flask import Flask, render_template, request, jsonify
import RPi.GPIO as GPIO
import behavior

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


if __name__ == '__main__':
    try:
        app.run(host='0.0.0.0', port=5000)
    finally:
        GPIO.cleanup()
