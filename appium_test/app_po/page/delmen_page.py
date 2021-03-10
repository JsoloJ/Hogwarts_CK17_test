from appium.webdriver.common.mobileby import MobileBy

from appium_test.app_po.page.base_page import BasePage
from appium_test.app_po.page.delcontact_page import DelContactPage


class DelMenber(BasePage):

    def click_delcontact(self):
        self.find_and_click(MobileBy.XPATH, "(//*[@resource-id='com.tencent.wework:id/e0l'])[2]/android.widget.ImageView")
        # element = self.driver.find_element_by_xpath("(//*[@resource-id='com.tencent.wework:id/e0l'])[2]/android.widget.ImageView")
        # element.click()
        #断言字段
        # check_text2 = self.find(MobileBy.XPATH, "(//*[@resource-id='com.tencent.wework:id/e0l'])[2]/android.widget.LinearLayout//android.widget.TextView")
        # print(check_text2)
        return DelContactPage(self.driver)