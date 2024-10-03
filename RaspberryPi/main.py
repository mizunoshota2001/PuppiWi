import threading
import keyboardlib
import puppetlib


def process_key(key: str):
    """
    キー押下時に実行する処理。
    各キーに応じた処理をここに実装します。
    この例では、キーごとに異なる処理をシミュレートしています。
    """
    if key == 'a':
        print("左手")
        puppetlib.left()
    elif key == 's':
        print("下を向く")
        puppetlib.head()
    elif key == 'd':
        print("右手")
        puppetlib.right()
    elif key == 'q':
        print("左旋回")
        puppetlib.ccw()
    elif key == 'e':
        print("右旋回")
        puppetlib.cw()
    else:
        print(f"未定義のキー '{key.upper()}' が押されました。")


def listener():
    key = keyboardlib.listen()
    process_key(key)
    listener()


def main():
    listener()


if __name__ == "__main__":
    main()
