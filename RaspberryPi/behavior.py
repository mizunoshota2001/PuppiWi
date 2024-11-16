import RPi.GPIO as GPIO
import time
from config import servo_config, WAIT_TIME
from typing import Dict
from multiprocessing import Value
servos: Dict[str, GPIO.PWM] = {}

GPIO.setmode(GPIO.BCM)
[GPIO.setup(servo['pin'], GPIO.OUT) for servo in servo_config.values()]
for name, config in servo_config.items():
    servos[name] = GPIO.PWM(config['pin'], config['frequency'])
    servos[name].start(config['initial_duty'])


def cdc(servo: GPIO.PWM, dutycycle: float):
    servo.ChangeDutyCycle(dutycycle)


def toggle(servo_name: str, servo: GPIO.PWM, wait=WAIT_TIME):
    config = servo_config[servo_name]
    cdc(servo, config['duty_to'])
    time.sleep(wait)
    cdc(servo, config['duty_from'])
    time.sleep(wait)
    cdc(servo, 0)


LEG_DUTY = Value('f', 7.5)


def leg(angle, servo=servos.get("leg"), wait=WAIT_TIME):
    duty = 12 - (abs(float(angle)) / 18 + 2)
    global LEG_DUTY
    LEG_DUTY.value = duty
    cdc(servo, duty)
    time.sleep(wait)
    cdc(servo, 0)


def left(servo=servos.get("left")):
    toggle("left", servo)


def right(servo=servos.get("right")):
    toggle("right", servo)


def head(servo=servos.get("head")):
    toggle("head", servo)


JIGGLY_FLAG = Value('b', False)


def jiggly(servo=servos.get("leg"), wait=WAIT_TIME):
    global JIGGLY_FLAG, LEG_DUTY
    while 1:
        time.sleep(wait)
        print(JIGGLY_FLAG.value)
        if not JIGGLY_FLAG.value:
            continue
        cdc(servo, LEG_DUTY.value+0.5)
        time.sleep(wait)
        cdc(servo, LEG_DUTY.value-0.5)
