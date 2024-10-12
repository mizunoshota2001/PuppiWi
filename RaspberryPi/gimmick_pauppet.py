import threading
import time
import keyboardlib
import puppetlib

stop = True


def gigpapet():
    time.sleep(0.5)
    if not stop:
        puppetlib.cw()
        time.sleep(0.5)
        puppetlib.ccw()
    gigpapet()


def process_key(key: str):
    global stop
    """s
    キー押下時に実行する処理。
    各キーに応じた処理をここに実装します。
    この例では、キーごとに異なる処理をシミュレートしています。
    """
    print("process_key")
    if key == 's':
        print("下を向く")
        puppetlib.head()
    elif key == 'q':
        print("左旋回")
        puppetlib.ccw()
    elif key == 'e':
        print("右旋回")
        puppetlib.cw()
    elif key == "x":
        stop = not stop
    else:
        print(f"未定義のキー '{key.upper()}' が押されました。")


def listener():
    key = keyboardlib.listen()
    print("listener")
    process_key(key)
    listener()


if __name__ == "__main__":
    thread = threading.Thread(target=gigpapet, name='thread1', daemon=True)
    thread.start()
    listener()
    thread.join()
    print("---end---")
