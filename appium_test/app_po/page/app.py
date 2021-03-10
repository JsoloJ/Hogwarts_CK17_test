import yaml
from appium import webdriver

from appium_test.app_po.page.base_page import BasePage
from appium_test.app_po.page.main_page import MainPage

with open("../datas/caps.yml") as f:
    datas = yaml.safe_load(f)
    desires = datas['desirecaps']
    ip = datas['server']['ip']
    port = datas['server']['port']
    # for i in range(3):
    #     for b in range(2):
    #         name = datas['name_and_phone'][i][b]
    #         phone = datas['name_and_phone'][i][b]

class App(BasePage):
    def start(self):
        if self.driver == None:
            #启动app
            #客户端与appium服务器建立连接的代码
            self.driver = webdriver.Remote(f"http://{ip}:{port}/wd/hub",desires)
            self.driver.implicitly_wait(10)
        else:
            self.driver.launch_app()
        return self.driver
    def restart(self):
        #重启
        self.driver.close_app()
        self.driver.launch_app()
    def stop(self):
        #停止
        self.driver.quit()
    def goto_main(self):
        return MainPage(self.driver)