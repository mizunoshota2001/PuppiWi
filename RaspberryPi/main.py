import threading
import time
import keyboardlib
import puppetlib

stop_body = True
stop_hands = True


def gig_body():
    global stop_body
    time.sleep(0.5)
    if not stop_body:
        try:
            puppetlib.cw()
            time.sleep(0.5)
            puppetlib.ccw()
        except Exception as e:
            print(e)
    gig_body()


def gig_hands():
    global stop_hands
    time.sleep(0.5)
    if not stop_hands:
        try:
            puppetlib.head()
            puppetlib.left()
            puppetlib.right()
        except Exception as e:
            print(e)
    gig_hands()


def process_key(key: str):
    global stop_body
    global stop_hands
    """
    キー押下時に実行する処理。
    各キーに応じた処理をここに実装します。
    この例では、キーごとに異なる処理をシミュレートしています。
    """
    if key == 's':
        print("手と頭")
        puppetlib.head()
        puppetlib.left()
        puppetlib.right()
    elif key == 'a':
        print("左旋回")
        puppetlib.cw()
    elif key == 'd':
        print("右旋回")
        puppetlib.ccw()
    elif key == "x":
        print("[%s]体" % ("停止" if stop_body else "再開"))
        stop_body = not stop_body
    elif key == "z":
        print("[%s]手と頭" % ("停止" if stop_hands else "再開"))
        stop_hands = not stop_hands
    else:
        print(f"未定義のキー '{key.upper()}' が押されました。")


def listener():
    key = keyboardlib.listen()
    process_key(key)
    listener()


if __name__ == "__main__":
    thread1 = threading.Thread(target=gig_body, name='thread1', daemon=True)
    thread2 = threading.Thread(target=gig_hands, name='thread2', daemon=True)
    thread1.start()
    thread2.start()
    listener()
    thread1.join()
    thread2.join()
