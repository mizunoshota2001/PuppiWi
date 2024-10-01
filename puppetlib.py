import moters

MOTERS = {
    "left": moters.Servo("left", 17),
    "right": moters.Servo("right", 18),
    "head": moters.Servo("head", 27),
    "leg": moters.Stepper(22, 23),
}


def left():
    pass



try:
    # サーボのインスタンスを作成
    left_hand =
    right_hand = Servo("right", 18)
    head = Servo("head", 27)

    # ステッピングモーターのインスタンスを作成
    stepper_motor = Stepper(22, 23)

    # サーボを動かす例
    left_hand.move(90, 2)   # 左手を90度に動かして2秒間維持
    right_hand.move(45, 1)  # 右手を45度に動かして1秒間維持
    head.move(135, 3)       # 頭を135度に動かして3秒間維持

    # ステッピングモーターを動かす例
    stepper_motor.move('CW', 2)  # 時計回りに2秒間回転
    stepper_motor.move('CCW', 3)  # 反時計回りに3秒間回転

except KeyboardInterrupt:
    print("プログラムを終了します")

finally:
    # クリーンアップ
    left_hand.cleanup()
    right_hand.cleanup()
    head.cleanup()
    GPIO.cleanup()
