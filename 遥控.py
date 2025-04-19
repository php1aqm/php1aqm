import sys
import threading

from pynput.mouse import Listener
from pynput.keyboard import Controller, Key

Keyboards = {
    "常规": [
        "keyboard.press(Key.space)",
        "keyboard.press(Key.up)",
        "keyboard.press(Key.down)",
        "keyboard.press(Key.left)",
        "keyboard.press(Key.right)",
        ""
    ],
    "PotPlayer": [
        "keyboard.press(Key.space)",
        "global last_key\nlast_key = 'up'",
        "global last_key\nlast_key = 'down'",
        "keyboard.press(Key.right)\nkeyboard.press(Key.right)",
        "keyboard.press(Key.left)\nkeyboard.press(Key.left)",
        '''if last_key == 'up':\n\tkeyboard.press(Key.page_up)\nelse:\n\tkeyboard.press(Key.page_down)'''
    ],
    "音乐": [
        "keyboard.press(Key.media_play_pause)",
        "keyboard.press(Key.media_volume_up)",
        "keyboard.press(Key.media_volume_down)",
        "keyboard.press(Key.media_previous)",
        "keyboard.press(Key.media_next)",
        ""
    ]
}


def on_move(x, y):
    # print('鼠标移动到 ({0}, {1})'.format(x, y))
    pass


def on_click(x, y, button, pressed):
    global pressed_pos
    global released_pos
    if exit_event.is_set():
        return False
    if pressed:
        print(f"Mouse pressed at ({x}, {y})")
        pressed_pos = (x, y)
    else:
        print(f"Mouse released at ({x}, {y})")
        released_pos = (x, y)
        if pressed_pos == (575, 539) and released_pos == (575, 539):
            print("中键：在(575, 539)点一下，长按是在开始点一下")
            exec(Keyboard[0])
        elif pressed_pos == (575, 492) and released_pos == (556, 971):
            print("上键：从(575, 492)向下滑到(556, 971)，长按加音量")
            exec(Keyboard[1])
        elif pressed_pos == (575, 863) and released_pos == (537, 324):
            print("下键：从(575, 863)向上滑到(537, 324)，然后在(537, 108)点一下，长按键音量")
            exec(Keyboard[2])
        elif pressed_pos == (288, 421) and released_pos == (863, 421):
            print("左键：从(288, 421)向右滑到(863, 421)，不可长按")
            exec(Keyboard[3])
        elif pressed_pos == (767, 421) and released_pos == (96, 421):
            print("右键：从(767, 421)向左滑到(96, 421)，不可长按")
            exec(Keyboard[4])
        elif pressed_pos == (430, 917) and released_pos == (430, 917):
            print("音键：在(430, 917)点一下，然后音量加或减2，不可长按")
            exec(Keyboard[5])


def your_code_segment():
    with Listener(on_move=on_move, on_click=on_click, suppress=False) as listener:
        listener.join()
    print("子线程退出")


def can_convert_to_int(s):
    try:
        int(s)
        return True
    except ValueError:
        return False


keyboard = Controller()
last_key = "down"
pressed_pos = (0, 0)
released_pos = (0, 0)
a = ''
while True:
    if can_convert_to_int(a):
        keys = list(Keyboards.keys())
        n = len(keys)
        if int(a) <= n:
            Keyboard = Keyboards[keys[int(a) - 1]]
            break
    a = input("请输入模式（1：常规、2：PotPlayer、3：音乐）：")


# 创建一个事件对象
# timeout_event = threading.Event()
# 创建一个事件对象，用于通知子线程退出
exit_event = threading.Event()

# 创建一个线程来运行您的代码段
thread = threading.Thread(target=your_code_segment)
thread.start()

# 等待指定的时间（秒）
# thread.join(timeout=30)
thread.join()

# 如果线程仍然活着，则标记为超时
if thread.is_alive():
    print("Timeout occurred!")
    exit_event.set()  # 设置事件
    thread.join()  # 等待子线程退出
    print("主线程退出")
    sys.exit("Program terminated due to timeout.")
