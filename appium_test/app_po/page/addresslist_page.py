from appium_test.app_po.page.addcontace_page import AddContactPage
from appium_test.app_po.page.base_page import BasePage


class AddressListPage(BasePage):

    def click_addcontact(self):
        element = self.swipe_find("添加成员")
        element.click()
        return AddContactPage(self.driver)
