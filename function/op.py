import tkinter as tk
from tkinter import ttk, messagebox
from . import path, interface
import json


def op():
    def search_tag():
        uuid = info_uuid_2.get()
        name = info_name_2.get()
        level = info_level_2.get()
        bypassesPlayerLimit = info_bypassesPlayerLimit_2.get()
        try:
            tag = op_list_uuid.index(uuid)
        except:
            try:
                tag = op_list_name.index(name)
            except:
                try:
                    tag = op_list_level.index(level)
                except:
                    try:
                        tag = op_list_bypassesPlayerLimit.index(bypassesPlayerLimit)
                    except:
                        messagebox.showerror('提示', '请不要修改所有参数，该操作会导致无法编辑')
        try:
            return tag
        except:
            pass

    def search():
        try:
            name = choose_combobox.get()
            tag = op_list_name.index(name)
            uuid = op_list_uuid[tag]
            name = op_list_name[tag]
            level = op_list_level[tag]
            bypassesPlayerLimit = op_list_bypassesPlayerLimit[tag]

            info_uuid_2_value.set(uuid)
            info_name_2_value.set(name)
            info_level_2_value.set(level)
            info_bypassesPlayerLimit_2_value.set(bypassesPlayerLimit)
        except:
            messagebox.showerror('提示', '该OP已经从列表中移除')

    def edit():
        uuid = info_uuid_2.get()
        name = info_name_2.get()
        level = info_level_2.get()
        bypassesPlayerLimit = info_bypassesPlayerLimit_2.get()
        tag = search_tag()
        op_list_uuid[tag] = uuid
        op_list_name[tag] = name
        op_list_level[tag] = level
        op_list_bypassesPlayerLimit[tag] = bypassesPlayerLimit

    def delete():
        tag = search_tag()
        del op_list_uuid[tag]
        del op_list_name[tag]
        del op_list_level[tag]
        del op_list_bypassesPlayerLimit[tag]

    def save():
        for i in range(0, len(op_list_bypassesPlayerLimit)):
            if op_list_bypassesPlayerLimit[i] == '0':
                op_list_bypassesPlayerLimit[i] = False
            if op_list_bypassesPlayerLimit[i] == '1':
                op_list_bypassesPlayerLimit[i] = True
        final = []
        for i in range(0, len(op_list_uuid)):
            onepiece = {"uuid": op_list_uuid[i], "name": op_list_name[i], "level": op_list_level[i],
                        "bypassesPlayerLimit": op_list_bypassesPlayerLimit[i]}
            final.append(onepiece)
            json_new = json.dumps(final)
            f = open(place + '/ops.json', 'r+', encoding='utf-8')
            f.truncate()
            f.write(json_new)
            f.close()

    def new():
        uuid = info_uuid_2.get()
        name = info_name_2.get()
        level = info_level_2.get()
        bypassesPlayerLimit = info_bypassesPlayerLimit_2.get()

        op_list_uuid.append(uuid)
        op_list_name.append(name)
        op_list_level.append(level)
        op_list_bypassesPlayerLimit.append(bypassesPlayerLimit)

    place = path.read_path()
    w = interface.interface("700x300")

    # 读取op文件信息
    f = open(place + '/ops.json', 'r+', encoding='utf-8')
    op_list_json_old = f.read()
    f.close()
    op_list = json.loads(op_list_json_old)
    op_list_uuid = []
    op_list_name = []
    op_list_level = []
    op_list_bypassesPlayerLimit = []
    for i in op_list:
        op_list_uuid.append(i['uuid'])
        op_list_name.append(i['name'])
        op_list_level.append(i['level'])
        op_list_bypassesPlayerLimit.append(i['bypassesPlayerLimit'])

    choose_label = tk.Label(w, text='请选择')
    choose_combobox = ttk.Combobox(w)
    choose_combobox['value'] = op_list_name
    choose_button = tk.Button(w, text='调取数据', command=search)
    info_uuid_1 = tk.Label(w, text='UUID')
    info_uuid_2_value = tk.StringVar()
    info_uuid_2 = tk.Entry(w, textvariable=info_uuid_2_value)
    info_name_1 = tk.Label(w, text='玩家名')
    info_name_2_value = tk.StringVar()
    info_name_2 = tk.Entry(w, textvariable=info_name_2_value)
    info_level_1 = tk.Label(w, text='权限等级')
    info_level_2_value = tk.StringVar()
    info_level_2 = tk.Entry(w, textvariable=info_level_2_value)
    info_bypassesPlayerLimit_1 = tk.Label(w, text='强制进入')
    info_bypassesPlayerLimit_2_value = tk.StringVar()
    info_bypassesPlayerLimit_2 = tk.Entry(w, textvariable=info_bypassesPlayerLimit_2_value)
    edit_button = tk.Button(w, text='修改数据', command=edit)
    delete_button = tk.Button(w, text='删除数据', command=delete)
    new_button = tk.Button(w, text='新增管理', command=new)
    save_button = tk.Button(w, text='保存修改', command=save)

    choose_label.place(x=10, y=10)
    choose_combobox.place(x=80, y=10, width=200)
    choose_button.place(x=300, y=7)
    info_uuid_1.place(x=10, y=50)
    info_uuid_2.place(x=80, y=50, width=300)
    info_name_1.place(x=10, y=80)
    info_name_2.place(x=80, y=80, width=300)
    info_level_1.place(x=10, y=110)
    info_level_2.place(x=80, y=110, width=300)
    info_bypassesPlayerLimit_1.place(x=10, y=140)
    info_bypassesPlayerLimit_2.place(x=80, y=140, width=300)
    edit_button.place(x=370, y=7)
    delete_button.place(x=440, y=7)
    new_button.place(x=510, y=7)
    save_button.place(x=580, y=7)
