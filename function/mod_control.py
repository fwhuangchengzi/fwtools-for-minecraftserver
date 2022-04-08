import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import os
from . import interface, path


def mod_control():
    place = path.read_path()
    def load():
        mod = choice.get()
        try:
            os.rename(place + '/mods/' + mod + '.jar.off', './mods/' + mod + '.jar')
        except:
            messagebox.showwarning('警告', '请不要在服务器运行时 或 模组已经启用时再次启用模组')
    def unload():
        mod = choice.get()
        try:
            os.rename(place + '/mods/' + mod + '.jar', place + '/mods/' + mod + '.jar.off')
        except:
            messagebox.showwarning('警告', '请不要在服务器运行时 或 模组已经停用时再次停用模组')
    mod_name = []
    w = interface.interface("700x325")

    # 插件列表读取及处理
    mod_dir = os.listdir(place + "/mods")
    for i in mod_dir:
        if '.jar' in i and '.off' not in i:
            i = i.strip('.jar')
            mod_name.append(i)
        elif '.jar.off' in i:
            i = i.strip('.jar.off')
            mod_name.append(i)
        else:
            pass
    # UI实现
    word = tk.Label(w, text='模组：')
    choice = ttk.Combobox(w, width=80)
    choice['value'] = mod_name
    word.place(x=10, y=10)
    choice.place(x=50, y=10)
    button_on = tk.Button(w, text='启用该模组', command=load)
    button_off = tk.Button(w, text='停用该模组', command=unload)
    button_on.place(x=200, y=70, width=100)
    button_off.place(x=340, y=70, width=100)
    w.mainloop()