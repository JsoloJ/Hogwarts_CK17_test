import allure
import pytest
from test_api.business.baseapi import BaseApi
from test_api.util.deal_data import read_data
from test_api.util.read_file import config_func
from test_api.util.log import logger


path = config_func('config','path')



"""
执行测试命令：pytest -vs --alluredir="../result_report/result" test_user.py
生成报告命令：allure generate ../result_report/result -o ../result_report/report --clean
"""
"""
按照该测试框架执行测试，需要注意如下几点：
1、需要修改传入参数的sheet名称
2、测试报告中的用例标题及allure.story中的文本信息
3、配置文件和测试用例中对应得信息
4、接口用例函数名称及  def test_creatuser
5、写入函数的位置需要和传入信息一致
"""


logger.info("用户模块测试开始")
@allure.feature('用户模块')
class TestUser:
    def setup_class(self):
        self.base = BaseApi()
        print('我是类初始化，我更先调用')

    def setup(self):
        print("必须先调用我")


    def teardown(self):
        print("用例结束必须执行")

    def teardown_class(self):
        print("类结束执行")



    @pytest.mark.parametrize('data',read_data(path=path,sheetname=config_func('case_sheet','create_sheet')))
    @allure.story('创建用户')
    def test_creatuser(self,data):
        logger.info(f'测试用例名称：{data["case_name"]}---------------------------------------------')
        #创建用户
        """
        :param data: 这里传入的数据是原始数据没有经过处理的数据，这里用来传入对应得api
        :return:
        返回接收的r是响应结果
        返回接收的expected_results是用例里面的期望结果
        返回的nrow是用例里面的对应得实际结果的行和执行结果的行，为了方便写入返回数据设置的
        返回的test_data是发送请求的数据，方便断言使用
        """
        with allure.step("将输入传入对应方法中，返回处理的数据"):
            r,expected_results,nrow,test_data = self.base.api_func(kwargs=data)
        with allure.step("获取返回的请求结果的文本信息用作断言"):
            actual_results = r.text
            logger.debug(f"返回的实际结果的文本信息：{actual_results}，预期结果：{expected_results}"
                         f"输入的测试数据信息：{test_data}")
        with allure.step("进行断言，这里做了一个异常处理，如果断言出错也不会退出,最后将结果数据和断言结果写入文件"):
            msg = self.base.assert_func(expected_results, actual_results, path, nrow, sheetname=config_func('case_sheet','create_sheet'))
            # try:
            #     assert expected_results in actual_results
            #     #还可以继续断言
            # except AssertionError as result:
            #     msg = str(result)+"快检查一下  你这断言有毛病啊"
            #     raise result
            # else:
            #     msg = "断言成功，这用例没毛病"
            #     print(f"{msg}")
            # finally:
            #     sheetname = 'data'
            #     write_data(path=path, sheetname=sheetname, nrow=nrow, actual_results=actual_results, msg=msg)






    @pytest.mark.parametrize('data', read_data(path=path, sheetname=config_func('case_sheet', 'search_sheet')))
    @allure.story('查询用户')
    def test_getmen(self,data):
        #查询成员
        logger.info(f'测试用例名称：{data["case_name"]}----------------------------------------------')
        """
        :param data: 这里传入的数据是原始数据没有经过处理的数据，这里用来传入对应得api
        :return:
        返回接收的r是响应结果
        返回接收的expected_results是用例里面的期望结果
        返回的nrow是用例里面的对应得实际结果的行和执行结果的行，为了方便写入返回数据设置的
        返回的test_data是发送请求的数据，方便断言使用
        """
        with allure.step("将输入传入对应方法中，返回处理的数据"):
            r,expected_results,nrow,test_data = self.base.api_func(kwargs=data)
        with allure.step("获取返回的请求结果的文本信息用作断言"):
            actual_results = r.text
            logger.debug(f"返回的实际结果的文本信息：{actual_results}，预期结果：{expected_results}"
                         f"输入的测试数据信息：{test_data}")
        with allure.step("进行断言，这里做了一个异常处理，如果断言出错也不会退出"):
            msg = self.base.assert_func(expected_results, actual_results, path, nrow, sheetname=config_func('case_sheet', 'search_sheet'))

        #     try:
        #         assert expected_results in actual_results
        #         # 还可以继续断言
        #     except AssertionError as result:
        #         msg = str(result)+"快检查一下  你这断言有毛病啊"
        #     else:
        #         msg = "断言成功，这用例没毛病"
        #     print(f"{msg}")
        # with allure.step("将结果数据和断言结果写入excel"):
        #     sheetname='data1'
        #     write_data(path=path,sheetname=sheetname,nrow=nrow,actual_results=actual_results,msg=msg)


    # sheetname = 'data2'
    # data = read_data(path=path, sheetname=sheetname)
    # @pytest.mark.parametrize('data', data)
    @pytest.mark.parametrize('data', read_data(path=path, sheetname=config_func('case_sheet', 'del_sheet')))
    @allure.story('删除用户')
    def test_delmen(self, data):
        """
        :param data: 这里传入的数据是原始数据没有经过处理的数据，这里用来传入对应得api
        :return:
        返回接收的r是响应结果
        返回接收的expected_results是用例里面的期望结果
        返回的nrow是用例里面的对应得实际结果的行和执行结果的行，为了方便写入返回数据设置的
        返回的test_data是发送请求的数据，方便断言使用
        """
        logger.info(f'测试用例名称：{data["case_name"]}----------------------------------------------')
        # 删除成员
        with allure.step("获取返回的请求结果的文本信息用作断言"):
            r,expected_results,nrow,test_data = self.base.api_func(kwargs=data)
        with allure.step("获取返回的请求结果的文本信息用作断言"):
            actual_results = r.text
            logger.debug(f"返回的实际结果的文本信息：{actual_results}，预期结果：{expected_results}"
                         f"输入的测试数据信息：{test_data}")
        with allure.step("进行断言，这里做了一个异常处理，如果断言出错也不会退出"):
            msg = self.base.assert_func(expected_results, actual_results, path, nrow, sheetname=config_func('case_sheet', 'del_sheet'))

        #     try:
        #         assert expected_results in actual_results
        #         # 还可以继续断言
        #     except AssertionError as result:
        #         msg = str(result)+"快检查一下  你这断言有毛病啊"
        #     else:
        #         msg = "断言成功，这用例没毛病"
        #     print(f"{msg}")
        # with allure.step("将结果数据和断言结果写入excel"):
        #     sheetname='data2'
        #     write_data(path=path,sheetname=sheetname,nrow=nrow,actual_results=actual_results,msg=msg)



    @pytest.mark.parametrize('data', read_data(path=path, sheetname=config_func('case_sheet', 'batchdelete')))
    @allure.story('批量删除用户')
    def test_batchdelete(self, data):
        """
        :param data: 这里传入的数据是原始数据没有经过处理的数据，这里用来传入对应得api
        :return:
        返回接收的r是响应结果
        返回接收的expected_results是用例里面的期望结果
        返回的nrow是用例里面的对应得实际结果的行和执行结果的行，为了方便写入返回数据设置的
        返回的test_data是发送请求的数据，方便断言使用
        """
        logger.info(f'测试用例名称：{data["case_name"]}----------------------------------------------')
        # 删除成员
        with allure.step("获取返回的请求结果的文本信息用作断言"):
            r, expected_results, nrow, test_data = self.base.api_func(kwargs=data)
        with allure.step("获取返回的请求结果的文本信息用作断言"):
            actual_results = r.text
            logger.debug(f"返回的实际结果的文本信息：{actual_results}，预期结果：{expected_results}"
                         f"输入的测试数据信息：{test_data}")
        with allure.step("进行断言，这里做了一个异常处理，如果断言出错也不会退出"):
            msg = self.base.assert_func(expected_results, actual_results, path, nrow,sheetname=config_func('case_sheet', 'batchdelete'))




    @pytest.mark.parametrize('data', read_data(path=path, sheetname=config_func('case_sheet', 'simplelist')))
    @allure.story('查看部门成员')
    def test_simplelist(self, data):
        """
        :param data: 这里传入的数据是原始数据没有经过处理的数据，这里用来传入对应得api
        :return:
        返回接收的r是响应结果
        返回接收的expected_results是用例里面的期望结果
        返回的nrow是用例里面的对应得实际结果的行和执行结果的行，为了方便写入返回数据设置的
        返回的test_data是发送请求的数据，方便断言使用
        """
        logger.info(f'测试用例名称：{data["case_name"]}----------------------------------------------')
        # 删除成员
        with allure.step("获取返回的请求结果的文本信息用作断言"):
            r, expected_results, nrow, test_data = self.base.api_func(kwargs=data)
        with allure.step("获取返回的请求结果的文本信息用作断言"):
            actual_results = r.text
            logger.debug(f"返回的实际结果的文本信息：{actual_results}，预期结果：{expected_results}"
                         f"输入的测试数据信息：{test_data}")
        with allure.step("进行断言，这里做了一个异常处理，如果断言出错也不会退出"):
            msg = self.base.assert_func(expected_results, actual_results, path, nrow,
                                        sheetname=config_func('case_sheet', 'simplelist'))






