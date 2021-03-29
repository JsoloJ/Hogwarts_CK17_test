import json

import requests

# url = "http://192.168.1.188:9999/monitor/ne/treeObject"
#
# # payload = {}
# headers = {
#   'Cookie': 'session=.eJwljkEKwzAMwP7icw-OaydOP1MS26GDwqBdLxv7-wo7CiHQB9ZxxLnB8jqumGB9OCzAs2EvUcx9eOWo1CyXnpnVtYewh2hkKuRGlVCIq7JSoxwyp2IUpGaYEalak1v6SFZkFnNphgnvpoeqYaUYNcaQMBTP0pgyTLA_re1xv7y3m64zjv9agu8PP3cy-w.YEsDNw.MtClIb53A-wQEqpCGwpkh2UkOY8; SESSION=OGMzMjIxZjQtNDU4YS00ZTQ5LTlhZjMtN2YyY2Q0OThhOTEx'
# }
#
# response = requests.request("GET", url, headers=headers)
#
# print(response.text,type(response.text))#str
# print(json.dumps(response.json(),indent=2),type(json.dumps(response.json())))#str
# print(response.json(),type(response.json()))#dict
# print(json.dumps(response.text),type(json.dumps(response.text)))#str
# print(json.loads(response.text),type(json.loads(response.text)))#dict





# url = "http://192.168.1.188:9999/business/save?name=1234&iconId=6&liableUserId=1"
#
# payload = {"name":"12345","iconId":6,"liableUserId":1}
# headers = {
#   'Cookie': 'session=.eJwljkEKwzAMwP7icw-OaydOP1MS26GDwqBdLxv7-wo7CiHQB9ZxxLnB8jqumGB9OCzAs2EvUcx9eOWo1CyXnpnVtYewh2hkKuRGlVCIq7JSoxwyp2IUpGaYEalak1v6SFZkFnNphgnvpoeqYaUYNcaQMBTP0pgyTLA_re1xv7y3m64zjv9agu8PP3cy-w.YEsDNw.MtClIb53A-wQEqpCGwpkh2UkOY8; SESSION=OGMzMjIxZjQtNDU4YS00ZTQ5LTlhZjMtN2YyY2Q0OThhOTEx'
# }
#
# response = requests.request("POST", url, headers=headers, data = payload)
#
# print(response.json())
# print(json.dumps(response.json(),indent=2))


# li = [0, 1, 2, 3, 4, 5, 6, 7, 8]
# print("li[-1:]: ", li[-1:])
# print("li[:-1]: ", li[:-1])
# print("li[0:2]: ", li[0:2])
# N=[]

# with open('user', 'r', encoding='UTF-8') as file_user_read:
#     user_lines = file_user_read.readlines()
#     for user in user_lines:
#         print(len(user))
#         N.append(user[:-1])
# print(N)


# param1= {"corpid":"ww2c1a0eb1fbd34797",
# "corpsecret":"OU7KFYJJz4KoIjVH1Df8CEazo1jxbqUtBb7qFordshI"
# }
#
# r=requests.request(method="get",url="https://qyapi.weixin.qq.com/cgi-bin/gettoken",params=param1).json()
# print(json.dumps(r,indent=2),type(json.dumps(r)))
# # requests.post
# from string import Template
#
#
# def main():
#     cart = []
#     cart.append(dict(item='coke',price=11,qty= 1))
#     cart.append(dict(item='cake',price=12,qty=6))
#     cart.append(dict(item='fish',price = 1,qty =4))
#
#     t = Template("$qty * $item = $price")
#     total = 0
#     print("Cart")
#     for data in cart:
#         print(t.substitute(data))
#         total += data["price"]
#
#     print("Total: %s"%(total,))
#
#
# if __name__ == "__main__":
#     main()
# def test_getmen():
#     # 查询成员
#
#     url = "https://qyapi.weixin.qq.com/cgi-bin/user/get"
#     data = {
#         'params': {
#             'access_token': 'cpnRmpMP3xr8tTzAnpY97pJremsm3Jm_rT4eh58jVEveACUTCRGPFJdqp_S6hpKZE3FrRXjRr8mvnGIxLLA23ozwdmiGSSXVhRfYoDK6xPOawoFW9tpL-QMwibD787pA3YuVQcrl8GW7PV7OzaYDUQR74eCu23rPJYojhMiMFLxTJIdw-5tBURBPPqfm9BkbNiv3u3FiDvlUjNY4-M3u2g',
#             'userid': '12224'
#         },
#         'url': url,
#         'method': 'get',
#         'json':1,
#         'data':None}
#     create_men = send(data)
#
# def send(kwargs):
#     r = requests.request(**kwargs)
#     print(r.json())
#     return r
# requests.ge


# d = {'userid':'123','ddjj':'djjfj','test1':'djjj'}
#
# for i in d.keys():
#     print(i)
# for key,value in d.items():
#     print(key,value)

# k_d = {'data': None}
# print(k_d)
# print(len(k_d))
# if len(k_d) > 0:
#     for key, value in k_d.items():
#         print(key,value)
# else:
#     print("Empty suite")
# print(type(k_d['data']))
# if k_d['data'] is None:
#     print('123')
# #     k_d['data'] = json.loads(k_d['data'])
# params={'{"useridlist": ["zhangsan", "lisi"]'}

