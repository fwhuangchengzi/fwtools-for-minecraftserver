from . import interface, path
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk


def command_run(command):
    place = path.read_path()
    f = open(place + '/plugins/FWTool-Server/terminal-data.yml', 'r+', encoding='utf-8')
    try:
        f.truncate(0)
    except:
        pass
    f.write('dispatch-command: "' + command + '"')
    f.close()


def server_command():
    def run():
        command = command_input.get()
        command_run(command)
        messagebox.showinfo('Complete!', '命令已成功传输\n请自行查看控制台反馈')

    def save():
        command = command_save_entry.get()
        command_list.append(command)
        f = open('./assets/command_save.yml', 'r+', encoding='utf-8')
        f.truncate()
        f.writelines(command_list)
        f.close()
        command_save_entry['value'] = command_list

    def delete():
        command = command_save_entry.get()
        command_list.remove(command)
        f = open('./assets/command_save.yml', 'r+', encoding='utf-8')
        f.truncate()
        f.writelines(command_list)
        f.close()
        command_save_entry['value'] = command_list

    def runcommand():
        command = command_save_entry.get()
        command_run(command)
        messagebox.showinfo('Complete!', '命令已成功传输\n请自行查看控制台反馈')

    w = interface.interface("700x300")
    command_input_info = tk.Label(w, text='命令:')
    command_input = tk.Entry(w)
    command_run_button = tk.Button(w, text='执行', command=run)

    command_input_info.place(x=10, y=10)
    command_input.place(x=50, y=10, width=500)
    command_run_button.place(x=560, y=7, width=60)

    # 命令存储部分
    f = open('./assets/command_save.yml', 'r+', encoding='utf-8')
    command_list = f.readlines()
    f.close()
    command_save_title = tk.Label(w, text='常用命令:')
    command_save_entry = ttk.Combobox(w)
    command_save_entry['value'] = command_list
    command_save = tk.Button(w, text='保存', command=save)
    command_delete = tk.Button(w, text='删除', command=delete)
    Command_run_button = tk.Button(w, text='运行', command=runcommand)

    warning = tk.Label(w, text='请在命令前加入命令头\n控制台命令 <console>[命令]\n玩家命令 <player:[玩家名]>[命令]\n\n例:\n<cons'
                               'ole>time set day\n<player:huangchengzi>gamemode creative', justify='left')

    command_save_title.place(x=10, y=80)
    command_save_entry.place(x=70, y=80, width=400)
    command_save.place(x=500, y=72)
    command_delete.place(x=550, y=72)
    Command_run_button.place(x=600, y=72)
    warning.place(x=10, y=120)

    w.mainloop()
