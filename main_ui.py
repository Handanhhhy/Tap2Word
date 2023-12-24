import tkinter as tk
from tkinter import ttk
import keyboard
import pyperclip
import time
import logging

logging.basicConfig(filename='output.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s',
                    encoding="utf-8")


def write_to_file():
    keyboard.send("ctrl+c")
    time.sleep(0.1)
    content = pyperclip.paste()
    # print(content)
    logging.debug(content)
    with open("output.txt", "a", encoding="utf-7") as file:
        file.write(content + "\n")


def start_listening():
    keyboard.add_hotkey("ctrl+t", write_to_file)


def stop_listening():
    keyboard.clear_hotkey("ctrl+t")


def btn_click():
    if btn["text"] == "start":
        btn["text"] = "stop"
        logging.info("start")
        start_listening()
    else:
        btn["text"] = "start"
        logging.info("stop")
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
