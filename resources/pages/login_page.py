from .base_page import BasePage
from .customer_page import CustomerPage
from .manager_page import ManagerPage
from playwright.sync_api import expect

class LoginPage(BasePage):

    def __init__(self, page):
        super().__init__(page)
        self.customer_login_button = page.get_by_role("button",name="Customer Login")
        self.manager_login_button = page.get_by_role("button", name="Bank Manager Login")

    def check_login_page_layout(self):
        expect(self.customer_login_button).to_be_visible()
        expect(self.manager_login_button).to_be_visible()

    def open_customer_page(self) -> CustomerPage:
        self.customer_login_button.click()
        customer_page = CustomerPage(self.page)
        customer_page.check_that_customer_page_is_opened()
        return customer_page

    def open_manager_page(self) -> ManagerPage:
        self.manager_login_button.click()
        manager_page = ManagerPage(self.page)
        manager_page.check_that_manager_page_is_opened()
        return manager_page