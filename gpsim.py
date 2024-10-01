import RPi.GPIO as GPIO
import time

# GPIOモードの設定
GPIO.setmode(GPIO.BCM)

# ピンの設定
LED_PIN = 18
GPIO.setup(LED_PIN, GPIO.OUT)

try:
    while True:
        GPIO.output(LED_PIN, GPIO.HIGH)  # LEDをオン
        print("LED ON")
        time.sleep(1)
        GPIO.output(LED_PIN, GPIO.LOW)  # LEDをオフ
        print("LED OFF")
        time.sleep(1)

except KeyboardInterrupt:
    print("プログラムを終了します")

finally:
    GPIO.cleanup()
