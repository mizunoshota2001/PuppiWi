from .settings import PINS
WAIT_TIME = 0.5
servo_config = {
    'left': {'pin': PINS['left'], 'frequency': 50, 'initial_duty': 0},
    'right': {'pin': PINS['right'], 'frequency': 50, 'initial_duty': 0},
    'head': {'pin': PINS['head'], 'frequency': 50, 'initial_duty': 0},
    'leg': {'pin': PINS['leg'], 'frequency': 50, 'initial_duty': 0}
}
