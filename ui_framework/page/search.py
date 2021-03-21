
from ui_framework.page.basepage import BasePage


class Search(BasePage):
    def search(self):
        # self.find_and_click(By.XPATH, '//*[@resource-id="com.xueqiu.android:id/action_search"]')
        self.parse("../page/search.yaml", "search")