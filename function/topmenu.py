import tkinter as tk


def topmenuall(window):
    def error():
        from tkinter import messagebox
        messagebox.showinfo('提示', '该功能暂未开发完毕')
    
    def first():
        from . import first
        window.destroy()
        first.first()

    def proper():
        from . import properties
        window.destroy()
        properties.properties()

    def plugin():
        from . import plugin_control
        window.destroy()
        plugin_control.plugin_control()

    def mod():
        from . import mod_control
        window.destroy()
        mod_control.mod_control()

    def path():
        from . import path
        path.set_path()

    def command():
        from . import server_command
        window.destroy()
        server_command.server_command()

    def op_control():
        from . import op
        window.destroy()
        op.op()

    def d_JDK():
        from . import r_JDK
        window.destroy()
        r_JDK.r_JDK()

    menu = tk.Menu(window, bg='gray')
    window['menu'] = menu

    menu1 = tk.Menu(menu, tearoff=False)

    choice1 = tk.Menu(menu1, tearoff=False)
    choice1.add_command(label='[1] 服务器初始化', command=first)
    choice1.add_command(label='[2] server.properties修改', command=proper)
    choice1.add_command(label='[3] OP列表管理', command=op_control)
    choice1.add_command(label='[4] start.bat修改', command=error)
    menu1.add_cascade(label='服务器基础配置', menu=choice1)

    choice2 = tk.Menu(menu1, tearoff=False)
    choice2.add_command(label='[1] 服务器插件开关', command=plugin)
    menu1.add_cascade(label='插件操作', menu=choice2)

    choice3 = tk.Menu(menu1, tearoff=False)
    choice3.add_command(label='[1] 服务器模组开关', command=mod)
    menu1.add_cascade(label='模组操作', menu=choice3)

    choice4 = tk.Menu(menu1, tearoff=False)
    menu1.add_cascade(label='指令生成器', menu=choice4)

    choice5 = tk.Menu(menu1, tearoff=False)
    choice5.add_command(label='[1] 执行指令(Bukkit、Bungee)', command=command)
    menu1.add_cascade(label='服务器操作', menu=choice5)

    choice6 = tk.Menu(menu1, tearoff=False)
    choice6.add_command(label='[1] JDK下载', command=d_JDK)
    choice6.add_command(label='[2] 服务器核心下载', command=command)
    menu1.add_cascade(label='资源获取', menu=choice6)

    updatemenu = tk.Menu(menu, tearoff=False)
    updatemenu.add_command(label='检查更新', command=error)
    updatemenu.add_command(label='更新日志', command=error)

    menu.add_cascade(label='操作', menu=menu1)
    menu.add_cascade(label='更新', menu=updatemenu)
    menu.add_command(label='选择目录', command=path)

