from time import sleep

from appium import webdriver

class TestDemo():
    def setup(self):
        desired_caps={}
        desired_caps["platformName"]="Android"
        desired_caps["platformVersion"]="6.0.1"
        desired_caps["deviceName"]="127.0.0.1:7555"
        desired_caps["appPackage"]="com.xueqiu.android"
        desired_caps["appActivity"]="com.xueqiu.android.business.MainActivity"
        self.driver=webdriver.Remote("http://localhost:4723/wd/hub",desired_caps)
        self.driver.implicitly_wait(10)
    def test_xueqiu(self):
        el1 = self.driver.find_element_by_id("com.xueqiu.android:id/tv_search")
        el1.click()
        el2 = self.driver.find_element_by_id("com.xueqiu.android:id/search_input_text")
        el2.send_keys("alibaba")
        # driver.set_page_load_timeout(5)
        el3 =self.driver.find_element_by_id("com.xueqiu.android:id/stockName")
        el3.click()
        sleep(15)
    def teardown(self):
        self.driver.quit()

