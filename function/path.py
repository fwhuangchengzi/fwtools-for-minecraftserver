from . import info, topmenu
import tkinter as tk
from tkinter.filedialog import askdirectory
from tkinter import messagebox


def set_path():
    def openpath():
        path = askdirectory()
        f = open('./assets/path.yml', 'w', encoding='utf-8')
        f.close()
        f = open('./assets/path.yml', 'r+', encoding='utf-8')
        f.write(path)
        f.close()
        messagebox.showinfo('成功！', '您已经成功绑定服务器目录，请重新打开您要使用的模块')
    title = info.global_title()
    w = tk.Tk()
    w.title(title)
    w.geometry("700x300")
    w.iconbitmap(r".\assets\logo.ico")
    topmenu.topmenuall(w)

    button = tk.Button(w, text='点击设置路径', command=openpath)
    button.place(x=10, y=10)


def read_path():
    f = open('./assets/path.yml', 'r', encoding='utf-8')
    path = f.read()
    return path
