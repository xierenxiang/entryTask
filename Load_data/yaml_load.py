import os
import sys

import yaml


# yaml格式内容的数据读取
def load(path):
    file = open(path, 'r', encoding='utf-8')
    data = yaml.load(file, Loader=yaml.FullLoader)
    # if path not in sys.path:
    #     path = os.path.dirname(sys.path[0])
    #     sys.path.append(path)
    return data

