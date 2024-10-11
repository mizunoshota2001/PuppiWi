import keyboard
import playsound
from pathlib import Path
import threading

__parent = Path(__file__).resolve().parent

def play_sound():
    playsound.playsound(__parent / "move.mp3")

def on_key_event(e):
    print(f"キーが押されました: {e.name}")
    threading.Thread(target=play_sound).start()

# すべてのキー押下イベントを監視
keyboard.on_press(on_key_event)

# プログラムが終了しないように待機
keyboard.wait('esc')  # 'esc'キーが押されるまで動作を継続
