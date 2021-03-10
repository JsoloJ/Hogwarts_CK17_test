from appium.webdriver.common.mobileby import MobileBy

from appium_test.app_po.page.base_page import BasePage
from appium_test.app_po.page.touchmenber_page import TouchMenber


class DelContactPage(BasePage):

    def click_contact_message(self):
        self.find_and_click(MobileBy.ID, "com.tencent.wework:id/iga")
        # element = self.driver.find_element_by_id("com.tencent.wework:id/iga")
        # element.click()
        return TouchMenber(self.driver)
