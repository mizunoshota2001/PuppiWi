import threading
import time
import keyboardlib
import puppetlib


def gigpapet():
    time.sleep(2)
    print("右手")
    puppetlib.right()
    print("左手")
    puppetlib.left()
    gigpapet()

def process_key(key: str):
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
    elif key=="p":
        gigpapet()
    else:
        print(f"未定義のキー '{key.upper()}' が押されました。")


def listener():
    key = keyboardlib.listen()
    print("listener")
    process_key(key)
    listener()


if __name__ == "__main__":
    thread = threading.Thread(target=gigpapet, name='thread1',daemon=True)
    thread.start()
    listener()
    thread.join()
    print("---end---")
