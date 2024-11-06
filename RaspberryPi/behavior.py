import RPi.GPIO as GPIO
import time
from settings import motor_config as servo_config, WAIT_TIME
from typing import Dict

GPIO.setmode(GPIO.BCM)
(GPIO.setup(servo['pin'], GPIO.OUT) for servo in servo_config.values())
    

servos: Dict[str, GPIO.PWM] = {}
for name, config in servo_config.items():
    servos[name] = GPIO.PWM(config['pin'], config['frequency'])
    servos[name].start(config['initial_duty'])


def cdc(servo: GPIO.PWM, dutycycle: float):
    servo.ChangeDutyCycle(dutycycle)


def leg(angle, servo=servos.get("left_servo"), wait=WAIT_TIME):
    duty = 12 - (angle / 18 + 2)
    cdc(servo, duty)
    time.sleep(wait)
    cdc(servo, 0)


def toggle(from_duty, to_duty, servo: GPIO.PWM, wait=WAIT_TIME):
    cdc(servo, to_duty)
    time.sleep(wait)
    cdc(servo, from_duty)
    time.sleep(wait)
    cdc(servo, 0)


def left(servo=servos.get("left_servo")):
    toggle(2, 12, servo)


def right(servo=servos.get("right_servo")):
    toggle(12, 2, servo)


def head(servo=servos.get("head_servo")):
    toggle(12, 2, servo)
