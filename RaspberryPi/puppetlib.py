import threading
import moterlib  # モーター制御用のライブラリをインポート


left_num=0
right_num=360

# モーターの初期化
MOTERS = {
    "left": moterlib.Servo("left", 26),
    "right": moterlib.Servo("right", 19),
    "head": moterlib.Servo("head", 13),
    "leg": moterlib.Servo("leg", 6),
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


@motor_control("leg")#右回転
def cw(moter: moterlib.Stepper28BYJ = MOTERS["leg"]):
    moter = MOTERS["leg"]
    right_num-=10
    moter.move(right_num, 0.5)



@motor_control("leg")#左回転
def ccw(moter: moterlib.Stepper28BYJ = MOTERS["leg"]):
    moter = MOTERS["leg"]
    left_num+=10
    moter.move(left_num, 0.5)

