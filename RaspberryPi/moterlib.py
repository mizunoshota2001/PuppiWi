import RPi.GPIO as GPIO
import time

# GPIOモードの設定
GPIO.setmode(GPIO.BCM)


class Servo:
    def __init__(self, name, pin):
        self.name = name
        self.pin = pin
        GPIO.setup(self.pin, GPIO.OUT)
        self.pwm = GPIO.PWM(self.pin, 50)  # 50Hzで初期化
        self.pwm.start(0)  # 初期デューティーサイクルは0

    def move(self, angle, duration):
        """
        サーボを指定角度に動かし、指定時間その状態を維持します。

        :param angle: サーボを動かす角度 (0-180)
        :param duration: 指定角度に維持する秒数
        """
        duty_cycle = (angle / 18) + 2  # 角度をデューティサイクルに変換 (0°=2%, 180°=12%)
        self.pwm.ChangeDutyCycle(duty_cycle)
        time.sleep(duration)
        self.pwm.ChangeDutyCycle(0)  # サーボを停止

    def cleanup(self):
        self.pwm.stop()


class Stepper:
    def __init__(self, step_pin, dir_pin):
        self.step_pin = step_pin
        self.dir_pin = dir_pin
        GPIO.setup(self.step_pin, GPIO.OUT)
        GPIO.setup(self.dir_pin, GPIO.OUT)

    def move(self, direction, duration):
        """
        ステッピングモーターを指定された方向に指定時間回転させます。

        :param direction: 回転方向 ('CW'または'CCW')
        :param duration: モーターを回転させる秒数
        """
        # 回転方向を設定
        if direction == 'CW':
            GPIO.output(self.dir_pin, GPIO.HIGH)  # 時計回り
        elif direction == 'CCW':
            GPIO.output(self.dir_pin, GPIO.LOW)   # 反時計回り
        else:
            print("回転方向は 'CW' または 'CCW' を指定してください。")
            return

        # モーターを回転させる
        start_time = time.time()
        while time.time() - start_time < duration:
            GPIO.output(self.step_pin, GPIO.HIGH)
            time.sleep(0.001)  # ステップ間の遅延 (調整可能)
            GPIO.output(self.step_pin, GPIO.LOW)
            time.sleep(0.001)
