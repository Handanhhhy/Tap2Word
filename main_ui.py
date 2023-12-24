import tkinter as tk
from tkinter import ttk
import keyboard
import pyperclip
import time
import logger

logger = logger.Logger()
#logger.log2console()
logger.log2file()

hotkey = "F8"


def write_to_file():
    keyboard.send("ctrl+c")
    time.sleep(0.01)  # 代码执行太快会粘贴到上一次复制的内容
    content = pyperclip.paste()
    logger.debug(content)
    with open("output.txt", "a", encoding="utf-8") as file:
        file.write(content + "\n")


def start_listening():
    keyboard.add_hotkey(hotkey, write_to_file)


def stop_listening():
    keyboard.clear_hotkey(hotkey)


def btn_click():
    if btn["text"] == "start":
        btn["text"] = "stop"
        logger.info("start")
        start_listening()
    else:
        btn["text"] = "start"
        logger.info("stop")
        stop_listening()


root = tk.Tk()
root.geometry("40x30")
root.attributes('-topmost', True)
root.title("Tap2Word")

btn = ttk.Button(root, text="start", command=btn_click)
btn.pack()

try:
    root.mainloop()
except KeyboardInterrupt:
    # 用户点击关闭按钮，执行退出操作
    stop_listening()
    root.destroy()
