from time import sleep

import yaml
import sys
import os

from appium_test.app_po.page.app import App

sys.path.append(os.path.abspath('../..'))



class TestContact:
    def setup_class(self):
        self.app = App()
        self.app.start()

    def setup(self):
        self.main = self.app.goto_main()


    def teardown(self):
        self.app.stop()

    def test_addcontact(self):

        editpage = self.main.goto_addresslist()
        for i in range(2):
            name = 'huoge41'+ str(i)
            phone = "1332222241" + str(i)
            editpage1 = editpage.click_addcontact().addcontact_menual()
            editpage1.edit_contact(name, phone)
            editpage1.verify_ok()

    # def test_yaml(self):
    #     # pyyaml
    #     with open("../datas/caps.yml") as f:
    #         datas = yaml.safe_load(f)

            # print(datas)
            # desires = datas['desirecaps']
            # ip = datas['server']['ip']
            # port = datas['server']['port']
            # for i in range(3):
            #     for b in range(2):
            #         name = datas['name_and_phone'][i][b]
            #         phone = datas['name_and_phone'][i][b]
                    # print(name,phone)
    def test_delcontact(self):
        delpage=self.main.goto_delmenber()
        for i in range(5):
            delpage2=delpage.click_delcontact().click_contact_message().touch_contact_message()
            delpage2.del_contact_message()
            sleep(3)
            # delpage.verify()
