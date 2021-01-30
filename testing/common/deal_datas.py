# -*- coding: utf-8 -*-
import yaml

def get_datas():
    with open("./datas/calc.yml") as f:
        datas = yaml.safe_load(f)
        # print(datas)
    return (datas)
# print(get_datas())