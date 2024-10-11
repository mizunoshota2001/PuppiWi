import threading
import keyboardlib
import puppetlib
import time


def process_key(key: str):
    """
    キー押下時に実行する処理。
    各キーに応じた処理をここに実装します。
    この例では、キーごとに異なる処理をシミュレートしています。
    """
    print("process_key")
    if key == 'a':
        print("はなす")
        puppetlib.left()
        puppetlib.right()
    elif key == 's':
        print("否定")
        puppetlib.ccw()
        time.sleep(1)
        puppetlib.cw()
    elif key == 'd':
        print("肯定")
        puppetlib.head()
        puppetlib.left()
        puppetlib.right()
    elif key == 'q':
        print("待機1")
        puppetlib.ccw()
        time.sleep(1)
        puppetlib.cw()
    elif key == 'e':
        print("待機2")
        puppetlib.left()
        puppetlib.right()
    else:
        print(f"未定義のキー '{key.upper()}' が押されました。")


def listener():
    print("listener")
    key = keyboardlib.listen()
    process_key(key)
    listener()


def main():
    listener()


if __name__ == "__main__":
    main()
