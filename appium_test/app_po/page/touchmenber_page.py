from appium.webdriver.common.mobileby import MobileBy

from appium_test.app_po.page.base_page import BasePage
from appium_test.app_po.page.delcontact import DelContact


class TouchMenber(BasePage):

    def touch_contact_message(self):
        self.find_and_click(MobileBy.XPATH,"//*[@text='编辑成员']")
        # element = self.driver.find_element_by_xpath("//*[@text='编辑成员']")
        # element.click()
        return DelContact(self.driver)