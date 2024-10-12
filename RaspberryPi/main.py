import keyboardlib
import threading
import time
import os
import puppetlib

stop_body = True
stop_hands = True

# 操作説明を定義（キー配置に基づく視覚的レイアウト）
instructions = """
終了する際にはターミナルを閉じてください。
+-----+-----+-----+
|  a  |  s  |  d  |
|  左 | 手頭|  右 |
+-----+-----+-----+
|  z  |  x  |←自動|
| 手頭|  体 |←切替|
+-----+-----+-----+
"""


def clear_console():
    """コンソールをクリアする関数"""
    os.system('cls' if os.name == 'nt' else 'clear')


def print_instructions():
    """操作説明を表示する関数"""
    clear_console()
    print(instructions)


def gig_body():
    global stop_body
    while True:
        try:
            time.sleep(0.5)
            if not stop_body:
                puppetlib.cw()
                time.sleep(0.5)
                puppetlib.ccw()
        except Exception as e:
            print(e)
            print("終了する際にはターミナルを閉じてください。")


def gig_hands():
    global stop_hands
    while True:
        try:
            time.sleep(0.5)
            if not stop_hands:
                puppetlib.head()
                puppetlib.left()
                puppetlib.right()
        except Exception as e:
            print(e)
            print("終了する際にはターミナルを閉じてください。")


def process_key(key):
    try:
        global stop_body
        global stop_hands
        """
        キー押下時に実行する処理。
        各キーに応じた処理をここに実装します。
        この例では、キーごとに異なる処理をシミュレートしています。
        """
        print_instructions()

        if key == 's':
            print(f"{key.upper()}: 手と頭")
            puppetlib.head()
            puppetlib.left()
            puppetlib.right()
        elif key == 'a':
            print(f"{key.upper()}: 左旋回")
            puppetlib.cw()
        elif key == 'd':
            print(f"{key.upper()}: 右旋回")
            puppetlib.ccw()
        elif key == "x":
            stop_body = not stop_body
            print(f"{key.upper()}: 体の動作[{'停止' if stop_body else '再開'}]")
        elif key == "z":
            stop_hands = not stop_hands
            print(f"{key.upper()}: 手と頭[{'停止' if stop_hands else '再開'}]")
        else:
            print(f"未定義のキー '{key.upper()}' が押されました。")
    except Exception as e:
        print(e)
        print("終了する際にはターミナルを閉じてください。")


def listener():
    while True:
        try:
            key = keyboardlib.listen()
            process_key(key)
        except Exception as e:
            print(e)
            print("終了する際にはターミナルを閉じてください。")


if __name__ == "__main__":
    print_instructions()  # プログラム開始時に操作説明を表示

    # スレッドの設定
    thread1 = threading.Thread(target=gig_body, name='thread1', daemon=True)
    thread2 = threading.Thread(target=gig_hands, name='thread2', daemon=True)

    # スレッドの開始
    thread1.start()
    thread2.start()

    listener()
