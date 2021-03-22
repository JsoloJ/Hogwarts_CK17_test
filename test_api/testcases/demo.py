import json

import pytest
import requests
from test_api.business import baseapi

L=baseapi.BaseApi()


def test_creatmen():
    #创建成员
    url = "https://qyapi.weixin.qq.com/cgi-bin/user/create"
    access_token='F6dTuF7C6nG3Ixiv0-g0yDRccy-5Wh4kT0V28e-d_Az4zuigoSgdeZ15iMqj-8bKjnKnOk08oFulzNZZMODtl-aOvpkvp4ONt0zRWbdrHsCMOpR9Fac3hbOIjmGkz3OXxbKU5Po6cm2fvKn9XFbTBNfCHQBLOBigOdhwavmGKxatepP6F-_8ZKS02GyOEyMYpJEcJaKn2D_rCJXmXE-MxA'
    data={
        'json':{
            'userid': '16',
            'name': '1231',
            'department':[1],
            'mobile':'13322222221'},
        'params':{"access_token":access_token}
    }
    print(type(data))
    r = L.send(url=url,method='post',kwargs=data)
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


