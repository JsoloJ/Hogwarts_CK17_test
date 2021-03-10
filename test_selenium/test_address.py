import json
from time import sleep

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class TestAdd:
    def setup(self):
        # 声明 chrome 的参数
        chrome_arg = webdriver.ChromeOptions()
        # 加入调试地址
        chrome_arg.debugger_address = '127.0.0.1:9225'
        self.driver = webdriver.Chrome(options=chrome_arg)
        self.driver.implicitly_wait(10)
        self.driver.set_script_timeout(10)
        self.driver.set_page_load_timeout(10)

    def teardown(self):
        self.driver.quit()


    def test_add(self):
        # 存入 cookie
        # self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        # cookies = self.driver.get_cookies()
        # with open("tmp2.text", "w", encoding="utf-8") as f:
        #     json.dump(cookies, f)

        # 读取 cookie
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        # with open("tmp2.text", "r", encoding="utf-8") as f:
        #     # 序列化
        #     cookies = json.load(f)
        # for i in cookies:
        #     self.driver.add_cookie(i)
        # self.driver.refresh()

        self.driver.find_element(By.XPATH,"//*[@id='menu_contacts']").click()
        print("点击了菜单")
        sleep(3)
        def wait_name(driver):
            eles = driver.find_elements(By.XPATH, "//*[@class='qui_btn ww_btn js_add_member']")
            # print(eles)
            eles[-1].click()
            eles = driver.find_elements(By.XPATH, "//*[@class='qui_btn ww_btn ww_btn_Blue js_btn_continue']")
            return len(eles) > 0

        WebDriverWait(self.driver, 10).until(wait_name)
        print("点击成功")
        sleep(4)
