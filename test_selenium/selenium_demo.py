import json
from time import sleep

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestTmp():
    @pytest.fixture(autouse=True)
    def setup_and_teardown(self):
        chrome_arg = webdriver.ChromeOptions()
        chrome_arg.debugger_address = '127.0.0.1:9222'
        #使用本地打开的浏览器进行调试，前提是必须先登录企业微信
        self.driver = webdriver.Chrome(options=chrome_arg)
        # self.driver = webdriver.Chrome()
        yield
        self.driver.quit()


    def test_cookie_login(self):
        """
        利用 cookie 进行登陆
        :return:
        """
        # 存入 cookie
        cookies = self.driver.get_cookies()
        with open("tmp2.text","w", encoding="utf-8") as f:
            json.dump(cookies, f)

        # 读取 cookie
        # self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        # with open("tmp2.text", "r", encoding="utf-8") as f:
        #     # 序列化
        #     cookies = json.load(f)
        # for i in cookies:
        #     self.driver.add_cookie(i)
        # self.driver.refresh()
        # sleep(6)

    #浏览器复用时使用
    def test_login_tmp(self):
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
        self.driver.find_element(By.XPATH,'//*[@id="menu_apps"]/span').click()

if __name__ == "__main__":
    pytest.main(["-v","-s"])