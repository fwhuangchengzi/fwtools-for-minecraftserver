from . import interface, batcreater
import tkinter as tk


def first():
    def first_1():
        def first_2():
            def first_eula():
                def first_3():
                    def server():
                        def open_properties():
                            from . import properties
                            properties.properties()
                            step3_4 = tk.Label(w, text='[9] 您已经完成了服务器的初始化，您可以通过上方的菜单栏前往其他功能区')
                            step3_4.place(x=10, y=70)
                        step3_2_b.destroy()
                        step3_3 = tk.Label(w, text='[8] 请修改server.properties文件')
                        step3_3.place(x=10, y=50)
                        step3_3_b = tk.Button(w, text='打开可视化修改界面', command=open_properties)
                        step3_3_b.place(x=200, y=50)
                    step2_1.destroy()
                    step2_2.destroy()
                    step2_to_step3.destroy()
                    step3_1 = tk.Label(w, text='[6] 请再次运行启动脚本')
                    step3_1.place(x=10, y=10)
                    step3_2 = tk.Label(w, text='[7] 等待出现Done！字样，然后输入stop')
                    step3_2.place(x=10, y=30)
                    step3_2_b = tk.Button(w, text='下一步', command=server)
                    step3_2_b.place(x=250, y=30, width=80)
                step2_1_b.destroy()
                step2_2 = tk.Label(w, text='[5] eula已经修改完成')
                step2_2.place(x=10, y=30)
                step2_to_step3 = tk.Button(w, text='下一步', command=first_3)
                step2_to_step3.place(x=150, y=30, width=80)
            from . import eula
            eula.eula()
            step1_button.destroy()
            step1_1.destroy()
            step1_2.destroy()
            step1_3.destroy()
            step1_to_step2.destroy()

            step2_1 = tk.Label(w, text='[4] 修改eula文件')
            step2_1.place(x=10, y=10)
            step2_1_b = tk.Button(w, text='点击自动修改', command=first_eula)
            step2_1_b.place(x=150, y=10, width=140)

        step1_1 = tk.Label(w, text='[1] 请创建服务器启动脚本')
        step1_1.place(x=10, y=60)
        batcreater.batcreater()
        step1_2 = tk.Label(w, text='[2] 请运行生成的启动脚本(start.bat)')
        step1_2.place(x=10, y=80)
        step1_3 = tk.Label(w, text='[3] 提示出错后关闭bat')
        step1_3.place(x=10, y=100)
        step1_to_step2 = tk.Button(w, text='下一步', command=first_2)
        step1_to_step2.place(x=250, y=100, width=80)

    w = interface.interface("700x300")

    step1_button = tk.Button(w, text='开始初始化', command=first_1)

    step1_button.place(x=10, y=10, width=100)

    w.mainloop()
