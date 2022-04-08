import tkinter as tk
from tkinter import ttk, messagebox
from . import interface
from tkinter.filedialog import askdirectory
import wget

def r_JDK():
    def download():
        path = askdirectory()
        version = choice.get()
        if version == 'Zulu OpenJDK 7':
            url = 'https://cdn.azul.com/zulu/bin/zulu7.52.0.11-ca-jdk7.0.332-win_x64.msi'
        elif version == 'Zulu OpenJDK 8':
            url = 'https://cdn.azul.com/zulu/bin/zulu8.60.0.21-ca-jdk8.0.322-win_x64.msi'
        elif version == 'Zulu OpenJDK 11':
            url = 'https://cdn.azul.com/zulu/bin/zulu11.54.25-ca-jdk11.0.14.1-win_x64.msi'
        elif version == 'Zulu OpenJDK 16':
            url = 'https://cdn.azul.com/zulu/bin/zulu16.32.15-ca-jdk16.0.2-win_x64.msi'
        elif version == 'Zulu OpenJDK 17':
            url = 'https://cdn.azul.com/zulu/bin/zulu17.32.13-ca-jdk17.0.2-win_x64.msi'
        messagebox.showinfo('Start!', 'JDK已经开始下载，程序将会未响应')
        wget.download(url, path)
        messagebox.showinfo('Complete!', 'JDK已下载到你指定的目录')
    w = interface.interface("700x300")

    info = tk.Label(w, text='JDK：')
    choice = ttk.Combobox(w)
    choice['value'] = ['Zulu OpenJDK 7', 'Zulu OpenJDK 8', 'Zulu OpenJDK 11', 'Zulu OpenJDK 16', 'Zulu OpenJDK 17']
    download_button = tk.Button(w, text='点击下载', command=download)

    info.place(x=10, y=10)
    choice.place(x=70, y=10)
    download_button.place(x=250, y=7)
    w.mainloop()
