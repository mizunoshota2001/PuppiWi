from gpiozero import PWMOutputDevice
from time import sleep

# tester
PIN = 6
WAIT = 0.5
servo = PWMOutputDevice(PIN, frequency=50)
servo.value = 0
sleep(WAIT)
servo.value = 2 / 100.0
sleep(WAIT)
servo.value = 12 / 100.0
sleep(WAIT)
servo.value = 0

