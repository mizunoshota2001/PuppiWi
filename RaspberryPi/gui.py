from flask import Flask, render_template, request, jsonify
import RPi.GPIO as GPIO
import time  # 追加

app = Flask(__name__)

# モータ設定の辞書
motor_config = {
    'left_motor': {'pin': 19, 'frequency': 50, 'initial_duty': 0},
    'right_motor': {'pin': 26, 'frequency': 50, 'initial_duty': 0},
    'head_motor': {'pin': 13, 'frequency': 50, 'initial_duty': 0},
    'leg_motor': {'pin': 6, 'frequency': 50, 'initial_duty': 0}
}

# モータの負荷軽減のための待機時間（秒）
WAIT_TIME = 0.5

# GPIO設定
GPIO.setmode(GPIO.BCM)
for motor in motor_config.values():
    GPIO.setup(motor['pin'], GPIO.OUT)

# PWM初期化と開始
motors = {}
for name, config in motor_config.items():
    motors[name] = GPIO.PWM(config['pin'], config['frequency'])
    motors[name].start(config['initial_duty'])

# 例: leg_motorを使用する場合
leg_motor = motors['leg_motor']


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/move_leg', methods=['POST'])
def move_leg():
    data = request.get_json()
    angle = data.get('angle')
    if angle is not None:
        duty = 12-(angle / 18 + 2)
        # dutyサイクルの範囲は2（0度）から12（180度）
        leg_motor.ChangeDutyCycle(duty)
        time.sleep(WAIT_TIME)  # 数秒待機
        leg_motor.ChangeDutyCycle(0)      # dutyサイクルを0に設定
    return jsonify(status='OK')


@app.route('/move_other', methods=['POST'])
def move_other():
    data = request.get_json()
    direction = data.get('direction')
    if direction == 'left':
        motors['left_motor'].ChangeDutyCycle(2)   # 左モーター180度, dutyサイクルの最大値
        time.sleep(WAIT_TIME)  # 数秒待機
        motors['left_motor'].ChangeDutyCycle(12)      # dutyサイクルを0に設定
        time.sleep(WAIT_TIME)  # 数秒待機
        motors['left_motor'].ChangeDutyCycle(0)      # dutyサイクルを0に設定

    elif direction == 'right':
        motors['right_motor'].ChangeDutyCycle(12)      # 右モーター0度, dutyサイクルの最小値
        time.sleep(WAIT_TIME)  # 数秒待機
        motors['right_motor'].ChangeDutyCycle(2)      # dutyサイクルを0に設定
        time.sleep(WAIT_TIME)  # 数秒待機
        motors['right_motor'].ChangeDutyCycle(0)      # dutyサイクルを0に設定

    elif direction == 'head':
        motors['head_motor'].ChangeDutyCycle(12)   # 頭モーター180度, dutyサイクルの最大値
        time.sleep(WAIT_TIME)  # 数秒待機
        motors['head_motor'].ChangeDutyCycle(2)      # dutyサイクルを0に設定
        time.sleep(WAIT_TIME)  # 数秒待機
        motors['head_motor'].ChangeDutyCycle(0)      # dutyサイクルを0に設定

    return jsonify(status='OK')


if __name__ == '__main__':
    try:
        app.run(host='0.0.0.0', port=5000)
    finally:
        GPIO.cleanup()
