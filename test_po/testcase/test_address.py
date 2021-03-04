from test_po.address_page.main_page import MainPage
from test_po.address_page.address_page import AddressPage


class Test_address():

    def test_address_menber(self):
        main1 = MainPage()
        main1.goto_address().add_member()

