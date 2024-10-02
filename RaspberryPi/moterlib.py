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

    def __duty(self, angle):
        return (angle / 18) + 2  # 角度をデューティサイクルに変換 (0°=2%, 180°=12%)

    def move(self, angle: int, duration: int):
        self.pwm.ChangeDutyCycle(self.__duty(angle))
        time.sleep(duration)
        self.pwm.ChangeDutyCycle(0)  # サーボを停止

    def cleanup(self):
        self.pwm.stop()

class Stepper28BYJ:
    # フルステップモードのシーケンス
    STEP_SEQUENCE = [
        [1, 0, 0, 0],
        [0, 1, 0, 0],
        [0, 0, 1, 0],
        [0, 0, 0, 1]
    ]

    def __init__(self, pin1, pin2, pin3, pin4):
        self.pins = [pin1, pin2, pin3, pin4]
        GPIO.setmode(GPIO.BCM)
        for pin in self.pins:
            GPIO.setup(pin, GPIO.OUT)
            GPIO.output(pin, GPIO.LOW)
        self.step_count = len(self.STEP_SEQUENCE)
        self.current_step = 0

    def __set_step(self, step):
        for pin, value in zip(self.pins, step):
            GPIO.output(pin, value)

    def move(self, direction, duration, delay=0.002):
        # 回転方向を設定
        if direction == 'CW':
            step_direction = 1  # 時計回り
        elif direction == 'CCW':
            step_direction = -1  # 反時計回り
        else:
            print("回転方向は 'CW' または 'CCW' を指定してください。")
            return

        # 回転させるステップ数を計算（例: 1秒あたりのステップ数を仮定）
        # 28BYJ-48のステップ数は約2048ステップ/回転
        # 回転速度を決めるためにステップ数を調整
        steps_per_second = 100  # 必要に応じて調整
        total_steps = int(steps_per_second * duration)

        start_time = time.time()
        for _ in range(total_steps):
            self.current_step = (self.current_step + step_direction) % self.step_count
            self.__set_step(self.STEP_SEQUENCE[self.current_step])
            time.sleep(delay)
            # 実際の経過時間をチェックして終了
            if time.time() - start_time >= duration:
                break

    def cleanup(self):
        GPIO.cleanup()
