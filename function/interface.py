import tkinter as tk
from . import info, topmenu

def interface(size):
    title = info.global_title()
    w = tk.Tk()
    w.title(title)
    w.geometry(size)
    w.iconbitmap(r".\assets\logo.ico")
    topmenu.topmenuall(w)

    return w