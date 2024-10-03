import threading
import moterlib  # モーター制御用のライブラリをインポート


# モーターの初期化
MOTERS = {
    "left": moterlib.Servo("left", 21),
    "right": moterlib.Servo("right", 20),
    "head": moterlib.Servo("head", 16),
    "leg": moterlib.Stepper28BYJ(6, 13, 19, 26),
}

# 各モーター用のロックオブジェクトを作成
LOCKS = {
    "left": threading.Lock(),
    "right": threading.Lock(),
    "head": threading.Lock(),
    "leg": threading.Lock(),
}


def motor_control(motor_key):
    """
    モーター制御用のデコレータ。
    ロックの取得、スレッドの開始、エラーハンドリングを行う。
    """
    def decorator(func):
        def wrapper(*args, **kwargs):
            lock = LOCKS[motor_key]
            if not lock.acquire(blocking=False):
                return

            def run():
                try:
                    func(*args, **kwargs)
                except Exception as e:
                    pass
                finally:
                    lock.release()
            threading.Thread(target=run, daemon=True).start()
        return wrapper
    return decorator


@motor_control("left")
def left(moter: moterlib.Servo = MOTERS["left"]):
    moter.move(180, 0.5)
    moter.move(0, 0.5)


@motor_control("right")
def right(moter: moterlib.Servo = MOTERS["right"]):
    moter = MOTERS["right"]
    moter.move(180, 0.5)
    moter.move(0, 0.5)


@motor_control("head")
def head(moter: moterlib.Servo = MOTERS["head"]):
    moter = MOTERS["head"]
    moter.move(180, 0.5)
    moter.move(0, 0.5)


@motor_control("leg")
def cw(moter: moterlib.Stepper28BYJ = MOTERS["leg"]):
    moter = MOTERS["leg"]
    moter.move('CW', 0.5)


@motor_control("leg")
def ccw(moter: moterlib.Stepper28BYJ = MOTERS["leg"]):
    moter = MOTERS["leg"]
    moter.move('CCW', 0.5)
