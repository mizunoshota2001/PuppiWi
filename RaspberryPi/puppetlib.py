import moterlib

MOTERS = {
    "left": moterlib.Servo("left", 17),
    "right": moterlib.Servo("right", 18),
    "head": moterlib.Servo("head", 27),
    "leg": moterlib.Stepper(22, 23),
}


def left(moter: moterlib.Servo = MOTERS["left"]):
    moter.move(90,1)


def right(moter: moterlib.Servo = MOTERS["right"]):
    moter.move()


def head(moter: moterlib.Servo = MOTERS["head"]):
    moter.move()


def cc(moter: moterlib.Stepper = MOTERS["leg"]):
    moter.move('CW', 2)  # 時計回りに2秒間回転


def ccw(moter: moterlib.Stepper = MOTERS["leg"]):
    moter.move('CCW', 3)  # 反時計回りに3秒間回転


