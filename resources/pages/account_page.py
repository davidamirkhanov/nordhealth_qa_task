from tests.conftest import page
from .base_page import BasePage
from playwright.sync_api import expect

class AccountPage(BasePage):
    """Customer's account page"""

    def __init__(self, page):
        super().__init__(page)
        self.logout_button = page.get_by_role("button", name="Logout")
        self.welcome_message = page.locator(".borderM>div>strong").first

    def check_welcome_message(self, customer_name:str):
        """Checks welcome message, that is displayed on top of the page"""
        expect(self.welcome_message).to_have_text(f' Welcome {customer_name} !!')