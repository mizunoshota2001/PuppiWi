import sys
import threading
import time
import keyboardlib

# 押されたキーを保存するリスト
pressed_keys = []
exit_flag = False  # 終了フラグ

# ロックオブジェクト（スレッド間の競合を防ぐため）
lock = threading.Lock()


def process_key(key: str):
    """
    キー押下時に実行する処理。
    各キーに応じた処理をここに実装します。
    この例では、キーごとに異なる処理をシミュレートしています。
    """
    if key == 'a':
        print("左手")
    elif key == 's':
        print("下を向く")
    elif key == 'd':
        print("右手")
    elif key == 'q':
        print("右旋回")
    elif key == 'e':
        print("左旋回")
    else:
        print(f"未定義のキー '{key.upper()}' が押されました。")


def key_listener_windows():
    global exit_flag
    while not exit_flag:
        key = keyboardlib.listen()
        with lock:
            if key in ['w', 'a', 's', 'd', "q", "e"]:
                pressed_keys.append(key)
                # 処理を新しいスレッドで実行
                threading.Thread(target=process_key, args=(
                    key,), daemon=True).start()
        time.sleep(0.01)  # CPU使用率を下げるために少し待つ


def key_listener_unix():
    global exit_flag
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setcbreak(fd)
        while not exit_flag:
            dr, dw, de = select.select([sys.stdin], [], [], 0)
            if dr:
                key = sys.stdin.read(1).lower()
                with lock:
                    if key in ['w', 'a', 's', 'd']:
                        pressed_keys.append(key)
                        print(f"キー '{key.upper()}' が押されました。")
                        # 処理を新しいスレッドで実行
                        threading.Thread(target=process_key, args=(
                            key,), daemon=True).start()
                    elif key == 'q':
                        print("終了キー 'Q' が押されました。")
                        exit_flag = True
            time.sleep(0.01)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)


def key_listener():
    if sys.platform.startswith('win'):
        key_listener_windows()
    else:
        key_listener_unix()


def main():
    global exit_flag
    listener_thread = threading.Thread(target=key_listener, daemon=True)
    listener_thread.start()

    print("WASDキーを押してください。'Q'を押すと終了します。")

    # メインスレッドは終了フラグを待つ
    try:
        while not exit_flag:
            time.sleep(0.1)
    except KeyboardInterrupt:
        print("\nKeyboardInterruptにより終了します。")
        exit_flag = True

    print("押されたキー:", pressed_keys)


if __name__ == "__main__":
    main()
