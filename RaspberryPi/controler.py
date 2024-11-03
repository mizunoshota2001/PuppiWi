import keyboardlib
import os
import puppetlib

stop_body = True
stop_hands = True

# 操作説明を定義（キー配置に基づく視覚的レイアウト）
instructions = """
終了する際にはターミナルを閉じる
エラーが出た際には再実行( python main.py )
+-----+-----+-----+
|  q  |     |  e  |
| 左回|     | 右回|
+-----+-----+-----+
|  a  |  s  |  d  | 
| 左手| 頭  | 右手|
+-----+-----+-----+
"""


def clear_console():
    """コンソールをクリアする関数"""
    os.system('cls' if os.name == 'nt' else 'clear')


def print_instructions():
    """操作説明を表示する関数"""
    clear_console()
    print(instructions)


def process_key(key):
    try:
        """
        キー押下時に実行する処理。
        各キーに応じた処理をここに実装します。
        この例では、キーごとに異なる処理をシミュレートしています。
        """
        print_instructions()

        if key == 's':
            print(f"{key.upper()}: 頭")
            puppetlib.head()
        elif key == 'a':
            print(f"{key.upper()}: 左手")
            puppetlib.left()
        elif key == 'd':
            print(f"{key.upper()}: 右手")
            puppetlib.right()
        elif key == "q":
            print(f"{key.upper()}: 左旋回")
            puppetlib.cw()
        elif key == "e":
            print(f"{key.upper()}: 右旋回")
            puppetlib.ccw()
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
    listener()
