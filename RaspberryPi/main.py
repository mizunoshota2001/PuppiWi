import threading
import keyboardlib
import puppetlib

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
        puppetlib.left()
    elif key == 's':
        print("下を向く")
    elif key == 'd':
        print("右手")
    elif key == 'q':
        print("左旋回")
    elif key == 'e':
        print("右旋回")
    else:
        print(f"未定義のキー '{key.upper()}' が押されました。")


def listener():
    key = keyboardlib.listen()
    with lock:
        pressed_keys.append(key)
        # 処理を新しいスレッドで実行
        threading.Thread(target=process_key, args=(
            key,), daemon=True).start()
    listener()


def main():
    listener()


if __name__ == "__main__":
    main()
