from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class AddressPage:
    def __init__(self,driver):
        self.driver = driver

    def add_member(self):
        # 不可交互
        # 1. 元素被遮挡：元素前面还有其它不可见元素
        # 2. 元素有多个，需要人工挑选中合适的元素
        def wait_name(driver):
            eles = driver.find_elements(By.XPATH, "//*[@class='qui_btn ww_btn js_add_member']")
            print(eles)
            eles[-1].click()
            eles = driver.find_elements(By.XPATH, "//*[@class='qui_btn ww_btn ww_btn_Blue js_btn_continue']")
            return len(eles) > 0

        WebDriverWait(self.driver, 15).until(wait_name)
        # 输入姓名
        name="今天是星期日"
        self.driver.find_element(By.XPATH, "//*[@id='username']").send_keys(name)
        # 输入账号
        self.driver.find_element(By.XPATH, "//*[@id='memberAdd_acctid']").send_keys("happer0123")
        # 输入手机号
        self.driver.find_element(By.XPATH, "//*[@id='memberAdd_phone']").send_keys("13910844999")
        # 点击保存
        self.driver.find_element(By.XPATH, "//*[@class='qui_btn ww_btn js_btn_save']").click()
        sleep(5)

        elements = self.driver.find_elements(By.XPATH, "//*[@class='member_colRight_memberTable_tr  member_colRight_memberTable_tr_Inactive']/td[2]/span")
        L = []
        for i in elements:
            L.append(i.text)
        assert name in L
        print(L)
