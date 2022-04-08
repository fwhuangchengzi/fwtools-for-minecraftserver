from . import interface, path
import tkinter as tk
import tkinter.ttk as ttk
from tkinter import messagebox


def batcreater():
    place = path.read_path()
    def choice():
        choice = choosebox.get()
        input1 = input1_txt.get()
        input2 = input2_txt.get()
        input3 = input3_txt.get()
        input4 = input4_txt.get()
        if choice != '' and input1 != '' and input2 != '' and input3 != '' and input4 != '':
            if choice == '[1] 纯启动文件':
                f = open(place + '/start.bat', 'w', encoding='utf-8')
                f.close
                f = open(place + '/start.bat', 'w', encoding='utf-8')
                f.write('@echo off\n\ntitle {input1}\njava -Xms{input2}M -Xmx{input3}M -jar {input4}.jar nogui'
                        '\n\npause\n'.format(input1=input1, input2=input2, input3=input3, input4=input4))
                tk.messagebox.showinfo('成功！', '文件生成完毕\n文件生成位置与本程序处于同一目录')
            else:
                tk.messagebox.showinfo('提示', '该功能暂未开发完毕')
        if choice == '' or input1 == '' or input2 == '' or input3 == '' or input4 == '':
                tk.messagebox.showinfo('提示', '参数缺失，请输入参数')
    def choice_normal():
        choice = choosebox.get()
        input1 = input1_txt.get()
        input4 = input4_txt.get()
        if choice != '' and input1 != '' and input4 != '':
            if choice == '[1] 纯启动文件':
                f = open(place + 'start.bat', 'w', encoding='utf-8')
                f.close
                f = open(place + 'start.bat', 'w', encoding='utf-8')
                f.write('@echo off\n\ntitle {input1}\njava -Xms4096M -Xmx4096M -jar {input4}.jar nogui'
                        '\n\npause\n'.format(input1=input1, input4=input4))
                tk.messagebox.showinfo('成功！', '文件生成完毕\n文件生成位置与本程序处于同一目录')
            else:
                tk.messagebox.showinfo('提示', '该功能暂未开发完毕')
        if choice == '' or input1 == '' or input4 == '':
                tk.messagebox.showinfo('提示', '参数缺失，请输入参数')
    w = interface.interface('600x300')

    choosebox = ttk.Combobox(window)
    choosebox['values'] = ['[1] 纯启动文件', '[2] 带优化启动文件 (java8)', '[3] 带优化启动文件 (java16)']
    btn1 = tk.Button(window, text='生成', command=choice)
    btn2 = tk.Button(window, text='生成推荐文件', command=choice_normal)
    input2_normal = tk.StringVar()
    input2_normal.set('(建议) 4096')
    input3_normal = tk.StringVar()
    input3_normal.set('(建议) 4096')
    input1_text = tk.Label(window, text='控制台标题')
    input2_text = tk.Label(window, text='最小内存(MB)')
    input3_text = tk.Label(window, text='最大内存(MB)')
    input4_text = tk.Label(window, text='核心文件名')
    input1_txt = tk.Entry(window)
    input2_txt = tk.Entry(window, textvariable=input2_normal)
    input3_txt = tk.Entry(window, textvariable=input3_normal)
    input4_txt = tk.Entry(window)

    choosebox.place(x=10, y=10)
    btn1.place(x=10, y=200, width=60, height=40)
    btn2.place(x=80, y=200, width=100, height=40)
    input1_text.place(x=10, y=100)
    input2_text.place(x=10, y=120)
    input3_text.place(x=10, y=140)
    input4_text.place(x=10, y=160)
    input1_txt.place(x=95, y=100)
    input2_txt.place(x=95, y=120)
    input3_txt.place(x=95, y=140)
    input4_txt.place(x=95, y=160)

    return True
