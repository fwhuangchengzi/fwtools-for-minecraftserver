# 导入库
from function import interface
import tkinter as tk

# 设定初始窗口样式
w = interface.interface("700x300")
# 设定初始窗口内容
text1 = tk.Label(w, text='FW·可视化开服工具', font=('微软雅黑', 20, 'bold'))
text1.place(x=10, y=10, anchor='nw')
text2 = tk.Label(w, text='请一定要先绑定目录！\n请一定要先绑定目录！\n请一定要先绑定目录！', justify='left')
text2.place(x=10, y=80)
text2 = tk.Label(w, text='该作品正在高频率更新，并非最终品质')
text2.place(x=480, y=255)
statement = tk.Label(w, text='Powered By 皇橙籽 @ 2022')
statement.place(x=10, y=255)

w.mainloop()
