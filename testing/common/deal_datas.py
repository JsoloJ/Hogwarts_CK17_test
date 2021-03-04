# -*- coding: utf-8 -*-
import yaml
import json

def get_datas(name,type):
    with open("./datas/calc.yml") as f:
        datas = yaml.safe_load(f)
        # print(datas)
        data1 = datas[name][type]['datas']
        data2 = datas[name][type]['ids']
    return (data1,data2)
# print(get_datas())

# p=get_datas('add','int')[0]
# print(p)

# p=get_datas
# print(p("add","int"))

