
from time import sleep

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait


class TestContact1():
    def setup(self):
        caps = {
            "platformName": "Android",
            "deviceName": "127.0.0.1:7555",
            "appPackage": "com.tencent.wework",
            "appActivity": ".launch.LaunchSplashActivity",
            # 跳过安装uiautomator2server等 服务
            "skipServerInstallation":"true",
            # 跳过设备的初始化
            "skipDeviceInitialization":"true",
            "noReset":"true"
        }
        self.driver=webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)
        self.driver.implicitly_wait(15)


    def teardown(self):
        self.driver.quit()

    def swipe_find(self):
        pass

    def swipe_find(self, text, num=3):
        for i in range(num):
            if i == num - 1:
                self.driver.implicitly_wait(5)
                raise NoSuchElementException(f"找到{num}次， 未找到。")

            self.driver.implicitly_wait(1)
            try:
                element = self.driver.find_element(MobileBy.XPATH, f"//*[@text='{text}']")
                self.driver.implicitly_wait(5)
                return element
            except:
                print("未找到")
                size = self.driver.get_window_size()
                width = size.get('width')
                height = size.get("height")

                start_x = width / 2
                start_y = height * 0.8

                end_x = start_x
                end_y = height * 0.3

                self.driver.swipe(start_x, start_y, end_x, end_y, 1000)

    def test_addcontact1(self):

        self.driver.find_element_by_xpath("//*[@text='通讯录']").click()
        # for i in range(6,10):
        name = "chengdu13"
        phone = 13300001124
        phone = int(phone)
        #找添加成员
        element = self.swipe_find("添加成员")
        element.click()
        # self.driver.find_element_by_xpath("//*[@text='添加成员']").click()
        self.driver.find_element_by_xpath("//*[@text='手动输入添加']").click()

        self.driver.find_element_by_xpath("//*[contains(@text,'姓名')]/../android.widget.EditText").send_keys(name)
        # self.driver.find_element_by_xpath("//*[@text='姓名' and @class='android.widget.TextView']").send_keys(name)

        self.driver.find_element_by_xpath("//*[contains(@text,'手机')]/..//*[@text='必填']").send_keys(phone)
        # self.driver.find_element_by_xpath("//*[@text='手机' and @class = 'android.widget.TextView']").send_keys(phone)
        self.driver.find_element_by_xpath(("//*[@text='保存']")).click()
        sleep(5)

    def test_daka(self):
        self.driver.find_element_by_xpath("//*[@text='工作台']").click()
        element = self.swipe_find("打卡")
        element.click()
        self.driver.find_element_by_xpath("//*[@text='外出打卡']").click()

        self.driver.find_element_by_xpath("//*[contains(@text,'次外出')]").click()
        print(self.driver.page_source)


