import threading
import sys
import time

# 创建一个事件对象，用于通知子线程退出
exit_event = threading.Event()

def your_code_segment():
    # 你的代码段
    # 例如：一个长时间运行的循环
    while not exit_event.is_set():  # 检查事件是否被设置
        pass
    print("子线程退出")

# 创建一个线程来运行您的代码段
thread = threading.Thread(target=your_code_segment)
thread.start()

# 等待指定的时间（秒）
thread.join(timeout=5)

# 如果线程仍然活着，则设置事件通知子线程退出
if thread.is_alive():
    print("Timeout occurred!")
    exit_event.set()  # 设置事件
    thread.join()  # 等待子线程退出
    print("主线程退出")
    sys.exit("Program terminated due to timeout.")