from pathlib import Path
import keyboard
import subprocess
import threading

# サブプロセスを起動し、標準入力にデータを送信する例
process = subprocess.Popen(['ssh', 'gctest@gctest.local'],
                           stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

def read_output():
    """プロセスの標準出力を非同期で読み取る"""
    while True:
        output = process.stdout.readline()
        if output:
            print(output.strip())
        else:
            break

# 標準出力の読み取りを別スレッドで実行
threading.Thread(target=read_output, daemon=True).start()

def on_key_event(e):
    """キーが押された際のイベント処理"""
    if e.name == 'esc':  # 'esc'キーが押されたら終了
        process.terminate()
        print("終了します...")
        return
    # 入力を送信
    process.stdin.write(f'{e.name}\n')
    process.stdin.flush()

# すべてのキー押下イベントを監視
keyboard.on_press(on_key_event)

# プログラムが終了しないように待機
keyboard.wait('esc')  # 'esc'キーが押されるまで動作を継続
