from settings import PINS
WAIT_TIME = 0.5
servo_config = {
    'left': {
        'pin': PINS['left'],
        'frequency': 50,
        'initial_duty': 0,
        'duty_from': 12,
        'duty_to': 2
    },
    'right': {
        'pin': PINS['right'],
        'frequency': 50,
        'initial_duty': 0,
        'duty_from': 2,
        'duty_to': 12
    },
    'head': {
        'pin': PINS['head'],
        'frequency': 50,
        'initial_duty': 0,
        'duty_from': 2,
        'duty_to': 12
    },
    'leg': {
        'pin': PINS['leg'],
        'frequency': 50,
        'initial_duty': 0,
        'duty_from': 0,
        'duty_to': 0
    }
}
