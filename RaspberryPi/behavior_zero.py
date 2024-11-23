from gpiozero import PWMOutputDevice
import time
from config import servo_config, WAIT_TIME
from typing import Dict
from multiprocessing import Value
servos: Dict[str, PWMOutputDevice] = {}

for name, config in servo_config.items():
    servos[name] = PWMOutputDevice(config['pin'], frequency=config['frequency'])
    servos[name].value = config['initial_duty'] / 100.0

def cdc(servo: PWMOutputDevice, dutycycle: float):
    servo.value = dutycycle / 100.0

def toggle(servo_name: str, servo: PWMOutputDevice, wait=WAIT_TIME):
    config = servo_config[servo_name]
    cdc(servo, config['duty_to'])
    time.sleep(wait)
    cdc(servo, config['duty_from'])
    time.sleep(wait)
    cdc(servo, 0)

LEG_DUTY = Value('f', 7.5)

def _duty(angle, original_min=0, original_max=180, target_min=2, target_max=12.5, invert=True):
    angle = abs(angle)
    if angle < original_min:
        angle = original_min
    elif angle > original_max:
        angle = original_max
    if invert:
        angle = original_max - angle
    duty = target_min + (angle - original_min) * \
        (target_max - target_min) / (original_max - original_min)
    return duty

def leg(angle, servo=servos.get("leg"), wait=WAIT_TIME):
    duty = _duty(angle)
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
    while True:
        time.sleep(wait)
        if not JIGGLY_FLAG.value:
            continue
        cdc(servo, LEG_DUTY.value + 0.005)
        time.sleep(wait)
        cdc(servo, LEG_DUTY.value - 0.005)
