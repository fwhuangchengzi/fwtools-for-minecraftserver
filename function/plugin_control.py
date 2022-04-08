import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import os
from . import interface, path


def plugin_control():
    place = path.read_path()
    def load():
        plugin = choice.get()
        try:
            os.rename(place + '/plugins/' + plugin + '.jar.off', place + '/plugins/' + plugin + '.jar')
        except:
            messagebox.showwarning('警告', '请不要在服务器运行时 或 插件已经启用时再次启用插件')
    def unload():
        plugin = choice.get()
        try:
            os.rename(place + '/plugins/' + plugin + '.jar', place + '/plugins/' + plugin + '.jar.off')
        except:
            messagebox.showwarning('警告', '请不要在服务器运行时 或 插件已经停用时再次停用插件')
    plugin_name = []
    w = interface.interface("700x325")

    # 插件列表读取及处理
    plugin_dir = os.listdir(place + "/plugins")
    for i in plugin_dir:
        if '.jar' in i and '.off' not in i:
            i = i.strip('.jar')
            plugin_name.append(i)
        elif '.jar.off' in i:
            i = i.strip('.jar.off')
            plugin_name.append(i)
        else:
            pass
    # UI实现
    word = tk.Label(w, text='插件：')
    choice = ttk.Combobox(w, width=80)
    choice['value'] = plugin_name
    word.place(x=10, y=10)
    choice.place(x=50, y=10)
    button_on = tk.Button(w, text='启用该插件', command=load)
    button_off = tk.Button(w, text='停用该插件', command=unload)
    button_on.place(x=200, y=70, width=100)
    button_off.place(x=340, y=70, width=100)
    w.mainloop()
