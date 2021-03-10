import yaml

from appium_test.app_po.page.app import App


class TestContact:
    def setup_class(self):
        self.app = App()
        self.app.start()

    def setup(self):
        self.main = self.app.goto_main()


    def teardown_class(self):
        self.app.stop()

    def teardown(self):
        self.app.stop()

    def test_addcontact(self):
        name = 'huoge'
        phone = '13322222222'
        editpage = self.main.goto_addresslist().click_addcontact().addcontact_menual()
        editpage.edit_contact(name, phone)
        editpage.verify_ok()

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
        delpage=self.main.goto_delmenber().click_delcontact().click_contact_message().touch_contact_message()
        delpage.del_contact_message()
        # delpage.verify()
