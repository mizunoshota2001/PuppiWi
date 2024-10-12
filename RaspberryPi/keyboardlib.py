

import time
import sys


def key_listener_windows():
    import msvcrt
    while not msvcrt.kbhit():
        time.sleep(0)
    key = msvcrt.getch()
    return key.decode('utf-8').lower()

def key_listener_unix():
    import tty
    import select
    fd = sys.stdin.fileno()
    tty.setcbreak(fd)
    while True:
        dr, _, _ = select.select([sys.stdin], [], [], 0)
        if dr:
            return sys.stdin.read(1).lower()
        time.sleep(0)

def listen():
    if sys.platform.startswith('win'):
        return key_listener_windows()
    return key_listener_unix()


