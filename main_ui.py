import tkinter as tk
from tkinter import ttk
import keyboard
import pyperclip


def write_to_file(content):
    print(content)
    with open("output.txt", "a") as file:
        file.write(content + "\n")


def start_listening():
    keyboard.add_hotkey("ctrl+t", lambda: write_to_file(pyperclip.paste()))


def stop_listening():
    keyboard.clear_hotkey("ctrl+t")


def btn_click():
    if btn["text"] == "start":
        btn["text"] = "stop"
        print("start")
        start_listening()
    else:
        btn["text"] = "start"
        print("stop")
        stop_listening()


root = tk.Tk()
root.geometry("40x30")
root.attributes('-topmost', True)
root.title("Tap2Word")

btn = ttk.Button(root, text="start", command=btn_click)
btn.pack()

root.mainloop()
