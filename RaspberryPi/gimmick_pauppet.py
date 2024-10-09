import threading
import keyboardlib

import time
import keyboard

def process_key(key: str):
    """s
    キー押下時に実行する処理。
    各キーに応じた処理をここに実装します。
    この例では、キーごとに異なる処理をシミュレートしています。
    """
    print("process_key")
    if key == 'a':
        print("左手")
        #puppetlib.left()
    elif key == 's':
        print("下を向く")
        #puppetlib.head()
    elif key == 'd':
        print("右手")
        #puppetlib.right()
    elif key == 'q':
        print("左旋回")
        #puppetlib.ccw()
    elif key == 'e':
        print("右旋回")
        #puppetlib.cw()
    elif key=="p":
        gigpapet()
    else:
        print(f"未定義のキー '{key.upper()}' が押されました。")


def gigpapet():
    if keyboard.is_pressed('o'):
        listener()
    else:
        print("lis右")
        #puppetlib.cw()
        time.sleep(3)
        print("lis左")
        #puppetlib.ccw()
    gigpapet()
    



def listener():
    key = keyboardlib.listen()
    print("listener")
    process_key(key)
    listener()



def main():
    gigpapet()


if __name__ == "__main__":
    main()

