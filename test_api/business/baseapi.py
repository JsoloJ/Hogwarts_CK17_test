import json
import requests
from test_api.util.log import logger
from test_api.util.read_file import config_func
from test_api.util.deal_data import write_data


corpid = config_func(section="wwork",option="my_corpid")

class BaseApi:

    def gettoken(self,corpsecret):
        data = {
            "params":{"corpid":corpid,"corpsecret":corpsecret},
            }
        r = self.send(method=config_func(section="wwork",option="method"),url=config_func(section="wwork",option="url"),kwargs=data)
        ACCESS_TOKEN = r.json()['access_token']
        logger.debug(f"获取token: {ACCESS_TOKEN}")
        return ACCESS_TOKEN


    def send(self,method,url,kwargs):
        logger.debug(f"发送请求")
        r = requests.request(method,url,**kwargs)
        return r

    def datafun(self,**kwargs):
        logger.debug(f"数据处理传入的参数{kwargs}")
        expected_results = kwargs['kwargs']['kwargs']['expected_results']
        nrow = kwargs['kwargs']['kwargs']['nrow']
        method = kwargs['kwargs']['kwargs']['method']
        url = kwargs['kwargs']['kwargs']['url']
        # corpsecret = "OU7KFYJJz4KoIjVH1Df8CHwt50KwGv7fo6uTV3C8oG8"
        corpsecret = kwargs['kwargs']['kwargs']['corpsecret']
        logger.debug(f"查看token生成参数获取{corpsecret}")

        logger.debug(f"提取了预期结果、用例对应行号、url和请求方法")

        data1 = {}
        if method == 'get':
            params={"access_token":self.gettoken(corpsecret)}
            data={}
            p_d = kwargs['kwargs']['kwargs']['params']
            d_d = kwargs['kwargs']['kwargs']['data']
            if p_d is not None:
                try:
                    p_d = json.loads(p_d)
                except BaseException as err_msg:
                    logger.error(f"报错信息： {err_msg}，你的测试数据格式有问题啊，快检查一下")
                for key,value in p_d.items():
                    params[key] = value
            data1['params'] = params
            if d_d is not None:
                logger.error(f"这是get请求，没有data参数: {d_d}，请检查数据")
                try:
                    d_d = json.loads(d_d)
                except BaseException as err_msg:
                    logger.error(f"报错信息： {err_msg}，你的测试数据格式有问题啊，快检查一下")
                for key, value in d_d.items():
                    data[key] = value
            data1['data'] = data
        else:
            data ={
                'json': kwargs['kwargs']['kwargs'],
                'params':{"access_token":self.gettoken(corpsecret)}
            }
            #将传入的参数转换成字典
            logger.debug(f'这里看下传入的数据是否有问题 {data}')
            if not data["json"]["data"] is None:
                try:
                    data1["json"] = json.loads(data["json"]["data"])
                except BaseException as err_msg:
                    logger.error(f"报错信息： {err_msg}，你的测试数据格式有问题啊，快检查一下")
            else:
                logger.error("post请求中没有data数据，请检查测试用例")
                data1["json"] = None
            d_p = data["json"]["params"]
            if d_p is not None:
                try:
                    d_p = json.loads(d_p)
                except BaseException as err_msg:
                    logger.error(f"报错信息： {err_msg}，你的测试数据格式有问题啊，快检查一下")
                for key,value in d_p.items():
                    data["params"][key] = value
            data1["params"] = data["params"]
        logger.debug(f"请求方法为{method},处理后的数据为{data1}")
        return data1,expected_results,nrow,method,url

    def api_func(self,**kwargs):
        logger.info(f"这里是接口方法，接收参数、处理参数")
        data, expected_results, nrow,method,url = self.datafun(kwargs=kwargs)
        # print(data, expected_results, nrow)
        logger.info(f"这里是接口方法，发送请求")
        r = self.send(method=method, url=url, kwargs=data)
        logger.info(f"这里是接口方法，返回结果")
        return r, expected_results, nrow, data

    def assert_func(self,expected_results,actual_results,path,nrow,sheetname):
        logger.info(f"断言期望结果 {expected_results} 是否在实际结果 {actual_results} 中")
        try:
            assert expected_results in actual_results
            # 还可以继续断言
        except AssertionError as result:
            msg = str(result) + "快检查一下  你这断言有毛病啊"
            logger.error(f"断言有误，错误信息:AssertionError")
            raise result
        else:
            msg = "断言成功，这用例没毛病"
            logger.info(f"{msg}")
        finally:
            logger.info(f"将断言的结果和返回的信息写入excel")
            write_data(path=path, sheetname=sheetname, nrow=nrow, actual_results=actual_results, msg=msg)
        return msg





if __name__=="__main__":
    L = BaseApi()
    print(L.gettoken())


