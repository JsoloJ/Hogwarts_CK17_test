from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from test_po.address_page.address_page import AddressPage


class MainPage():
    def __init__(self):
        chrome_arg = webdriver.ChromeOptions()
        # 加入调试地址
        chrome_arg.debugger_address = '127.0.0.1:9225'
        self.driver = webdriver.Chrome(options=chrome_arg)
        self.driver.implicitly_wait(10)
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
    def goto_address(self):
        # 点击通讯录
        self.driver.find_element(By.XPATH, "//*[@id='menu_contacts']").click()
        sleep(3)
        return AddressPage(self.driver)