from flask import Flask, render_template, request, jsonify
import RPi.GPIO as GPIO
import behavior 

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/move_leg', methods=['POST'])
def move_leg():
    data = request.get_json()
    angle = data.get('angle')
    if angle is not None:
        behavior.move_leg(angle)
    return jsonify(status='OK')


@app.route('/move_other', methods=['POST'])
def move_other():
    data = request.get_json()
    direction = data.get('direction')
    if direction is not None:
        if direction == 'left':
            behavior.left()
        elif direction == 'right':
            behavior.right()
        elif direction == 'head':
            behavior.head()
    return jsonify(status='OK')


if __name__ == '__main__':
    try:
        app.run(host='0.0.0.0', port=5000)
    finally:
        GPIO.cleanup()
