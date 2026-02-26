from tests.conftest import page
from .base_page import BasePage
from playwright.sync_api import expect

class CustomerPage(BasePage):
    """Cusromers' login page class"""

    def __init__(self, page):
        super().__init__(page)
        self.customer_label = page.locator("label", has_text="Your Name :")
        self.customer_selector = page.locator("select#userSelect")
        self.login_button = page.get_by_role("button", name="Login")

    def check_that_customer_page_is_opened(self):
        """Checks page elements"""
        expect(self.customer_label).to_be_visible()
        expect(self.customer_selector).to_be_visible()

    def select_customer(self, customer_name:str):
        """Selects customer from drop-down, prints error message if customer not found"""
        options = self.customer_selector.locator("option").all_inner_texts()
        if customer_name not in options:
            print(f"Customer '{customer_name}' not found in customers' list")
        else:
            self.customer_selector.select_option(customer_name)

    def click_login_button(self):
        """Clicks 'Login' in the top-left corner of the page"""
        self.login_button.click()

    def login_as_customer(self, customer_name:str):
        """Logs in into customer's account"""
        self.select_customer(customer_name)
        self.click_login_button()

    def get_customers_list(self):
        """Gets list of customer names from the drop-down"""
        customers_list = []
        all_rows_in_customers_drop_down = self.customer_selector.get_by_role("option").all()
        for row in all_rows_in_customers_drop_down[1:]:  # exclude first line, because this is header
            customers_list.append(row.inner_text())
        return customers_list