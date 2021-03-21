import json

import pytest
import requests
from test_api.business import baseapi

def test_creatmen():
    #创建成员
    url = "https://qyapi.weixin.qq.com/cgi-bin/user/create"
    data ={
        'method':'post',
        'url': url,
        'json':{
            'userid': '116',
            'name': '1236',
            'department':[1],
            'mobile':'13322222226'},
        'params':{"access_token": baseapi.gettoken()}
    }
    r = baseapi.send(data)
    print(r.json())

print('---------------------------------------------------------')

def test_getmen(self):
#查询成员

    params={
        'access_token': baseapi.gettoken(),
        'userid': self.Userid
        }
    url = "https://qyapi.weixin.qq.com/cgi-bin/user/get"
    create_men = requests.get(url=url,params=params)
    print(create_men.json())
    print("--------------------------------------------------------")

def test_delmen(self):
    #删除成员

    data={
        'userid':self.Userid,
    }
    print(json.dumps(data))
    params={
        'access_token': self.ACCESS_TOKEN
        }
    print(self.Userid)
    url = "https://qyapi.weixin.qq.com/cgi-bin/user/delete"
    create_men = requests.post(url=url,data=data,params=params)
    print(create_men.json())


