from appium.webdriver.common.mobileby import MobileBy

from appium_test.app_po.page.base_page import BasePage



class DelContact(BasePage):

    def del_contact_message(self):
        self.find_and_click(MobileBy.ID, "com.tencent.wework:id/esd")
        # element = self.driver.find_element_by_id("com.tencent.wework:id/esd")
        # element.click()
        # check_text1 = self.find_and_click(MobileBy.ID, "com.tencent.wework:id/bp_")

        self.find_and_click(MobileBy.ID, "com.tencent.wework:id/bpc")
        # element1 = self.driver.find_element_by_id("com.tencent.wework:id/bpc")
        # element1.click()

    # def verify(self):
    #     check_text1 = self.find(MobileBy.XPATH,"(//*[@resource-id='com.tencent.wework:id/e0l'])[2]/android.widget.LinearLayout//android.widget.TextView")
    #     assert check_text1 != check_text2

