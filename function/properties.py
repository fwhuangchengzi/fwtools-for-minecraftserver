import tkinter as tk
from . import interface, path


def properties():
    place = path.read_path()
    def info_write():
        final_list1 = list1_1
        final_list2 = []
        final = [list0[0], list0[1]]
        for z in list_entry:
            info_k = z.get()
            final_list2.append(info_k)
        for i in range(len(final_list2)):
            final.append(final_list1[i] + '=' + final_list2[i] + '\n')
        open(place + '/server.properties', 'w').close()
        file = open(place + '/server.properties', 'r+', encoding='utf-8')
        file.writelines(final)
        file.close()
        print(final)

    global size_x_1, size_x_2, size_y
    size_x_1 = 10
    size_x_2 = 225
    size_y = 10

    def size():
        global size_x_1, size_x_2, size_y
        size_y += 25
        if size_y > 550:
            size_x_1 += 400
            size_x_2 += 400
            size_y = 10

    # 读取server.properties
    file = open(place + '/server.properties', 'r+', encoding='utf-8')
    list0 = file.readlines()
    list1 = []
    list2 = []
    for i in list0:
        middle = i
        middle = middle.strip('\n')
        middle = middle.split('=')
        try:
            list1.append(middle[0])
            list2.append(middle[1])
        except:
            pass
    del list1[0]
    del list1[0]
    properties_old = {}
    for i in range(len(list1)):
        properties_old[list1[i]] = list2[i]
    file.close()

    # 设定初始窗口样式
    w = interface.interface("1200x600")

    chinese0 = ['allow-flight', 'allow-nether', 'broadcast-console-to-ops', 'broadcast-rcon-to-ops', 'difficulty', 'enable-command-block', 'enable-jmx-monitoring', 'enable-query', 'enable-rcon', 'enable-status', 'enforce-whitelist', 'entity-broadcast-range-percentage', 'force-gamemode', 'function-permission-level', 'gamemode', 'generate-structures', 'generator-settings', 'hardcore', 'hide-online-players', 'level-name', 'level-seed', 'level-type', 'max-build-height', 'max-players', 'max-tick-time', 'max-world-size', 'motd', 'network-compression-threshold', 'online-mode', 'op-permission-level', 'player-idle-timeout', 'prevent-proxy-connections', 'pvp', 'query.port', 'rate-limit', 'rcon.password', 'rcon.port', 'require-resource-pack', 'resource-pack', 'resource-pack-prompt', 'resource-pack-sha1', 'server-ip', 'server-port', 'simulation-distance', 'spawn-animals', 'spawn-monsters', 'spawn-npcs', 'spawn-protection', 'sync-chunk-writes', 'text-filtering-config', 'view-distance', 'view-distance', 'white-list', 'server-name', 'debug', 'snooper-enabled']
    chinese1 = ['是否允许飞行(布尔值)', '是否开放地狱(布尔值)', '对OP输出执行的命令(布尔值)', '对OP输出RCON执行的命令(布尔值)', '游戏难度(字符串)', '是否启用命令方块(布尔值)', 'enable-jmx-monitoring(布尔值)', '是否允许GameSpy4的监听器(布尔值)', '是否允许远程访问控制台(布尔值)', '是否使服务器状态常在线(布尔值)', '是否强制执行白名单(布尔值)', '实体发送距离(10-1000)', '是否强制默认模式进入(布尔值)', '设定函数的默认权限等级(1-4)', '默认游戏模式(字符串)', '是否在游戏中生成结构(布尔值)', '自定义世界生成器(字符串)', '是否开启极限模式(布尔值)', '隐藏对外在线玩家列表(布尔值)', '默认世界名称(字符串)', '地图种子(字符串)', '地图类型(字符串)', '最大建造高度(1-256)', '最大人数(＞0)', '每tick最大毫秒数(0 – (2^63 - 1))', '世界边界最大半径(0-29999984)', '服务器列表中服务器信息(字符串)', '数据包压缩限制字节数(>64)', '是否开启正版验证(布尔值)', 'OP权限等级(1-4)', '玩家挂机踢出时间(分钟)', '是否禁用网络代理(布尔值)', '是否允许PVP(布尔值)', '监听服务器的端口号(0-65534)', '玩家被踢出前可发送的数据包数量(整数)', 'RCON远程访问密码(整数)', 'RCON远程访问端口号(1-65534)', '强制使用服务器资源包(字符串)', '资源包地址(字符串)', '资源包提示界面自定义文本(字符串)', '资源包的SHA-1值(字符串)', '绑定特定IP(字符串，建议留空)', '服务器端口(1-65534)', 'simulation-distance', '是否允许动物生成(布尔值)', '是否允许怪物生成(布尔值)', '是否允许村民生成(布尔值)', '出生点保护区域(整数)', '区块文件是否以同步模式写入(布尔值)', 'text-filtering-config', '是否启用linux平台优化(布尔值)','发送的可视区块半径(3-32)', '是否启用白名单(布尔值)', '服务器名称(字符串)', '是否启用DEBUG模式(布尔值)', 'snooper-enabled']
    list1_1 = list1.copy()

    for i in chinese0:
        if i in list1:
            where_chinese = chinese0.index(i)
            where_list = list1.index(i)
            list1[where_list] = chinese1[where_chinese]

    list_entry = []
    try:
        for i in range(0, 100):
            normal = tk.StringVar()
            text = properties_old[list1_1[i]]
            normal.set(text)
            i = tk.Label(w, text=list1[i])
            i.place(x=size_x_1, y=size_y)
            k = tk.Entry(w, textvariable=normal)
            k.place(x=size_x_2, y=size_y)
            list_entry.append(k)
            size()
    except:
        pass

    button = tk.Button(w, text='点击修改', command=info_write, font=('微软雅黑', 12, 'bold'))
    button.place(x=size_x_2-70, y=size_y+100, width=100, height=50)
