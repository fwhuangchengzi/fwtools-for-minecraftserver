import re
from . import path


def eula():
    place = path.read_path()
    f = open(place + '/eula.txt', 'r', encoding='utf-8')
    lines = f.readlines()
    f.close()
    f = open(place + '/eula.txt', 'w', encoding='utf-8')
    for each in lines:
        a = re.sub('false', 'true', each)
        f.write(a)
    f.close()
