from resources.pages.login_page import LoginPage
from resources.pages.account_page import AccountPage
from resources.utils import check_that_lists_are_equal

def test_login_page_layout(go_to_login_page):
    login_page = LoginPage(go_to_login_page)
    login_page.check_login_page_layout()

def test_customer_login_successful(go_to_login_page, page, existing_customer):
    login_page = LoginPage(go_to_login_page)
    customer_page = login_page.open_customer_page()
    customer_page.login_as_customer(existing_customer.full_name())
    account_page = AccountPage(page)
    account_page.check_welcome_message(existing_customer.full_name())
    account_page.return_home()

def test_bank_manager_login_successful(go_to_login_page):
    login_page = LoginPage(go_to_login_page)
    manager_page = login_page.open_manager_page()
    manager_page.return_home()

def test_that_all_customers_are_available_on_customers_page(go_to_login_page):
    login_page = LoginPage(go_to_login_page)
    manager_page = login_page.open_manager_page()
    customers_list_from_manager_page = manager_page.get_customers_list()
    manager_page.return_home()
    customer_page = login_page.open_manager_page()
    customers_list_from_customer_page = customer_page.get_customers_list()
    check_that_lists_are_equal(customers_list_from_manager_page, customers_list_from_customer_page)
