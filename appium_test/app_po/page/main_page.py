from appium.webdriver.common.mobileby import MobileBy

from appium_test.app_po.page.addresslist_page import AddressListPage
from appium_test.app_po.page.base_page import BasePage
from appium_test.app_po.page.delmen_page import DelMenber


class MainPage(BasePage):
    addresslist_element = (MobileBy.XPATH, "//*[@text='通讯录']")

    def goto_addresslist(self):
        # 点击 通讯录
        self.find(*self.addresslist_element).click()
        # self.driver.find_element(MobileBy.XPATH, "//*[@text='通讯录']").click()
        return AddressListPage(self.driver)
    def goto_delmenber(self):
        self.find(*self.addresslist_element).click()
        return DelMenber(self.driver)