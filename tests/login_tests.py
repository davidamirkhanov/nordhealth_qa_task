from resources.pages.login_page import LoginPage
from resources.pages.account_page import AccountPage
from resources.utils import check_that_lists_are_equal

def test_login_page_layout(go_to_login_page):
    """Test Case 1: Login Page Layout
    Steps:
    1. Open Login Page
    2. Check page elements"""

    login_page = LoginPage(go_to_login_page)
    login_page.check_login_page_layout()

def test_customer_login_successful(go_to_login_page, page, existing_customer):
    """Test Case 2: Login as Customer
    Steps:
    1. Open Login Page
    2. Login as Customer  -- > Login should be successful"""

    login_page = LoginPage(go_to_login_page)
    customer_page = login_page.open_customer_page()
    customer_page.login_as_customer(existing_customer.full_name())
    account_page = AccountPage(page)
    account_page.check_welcome_message(existing_customer.full_name())
    account_page.return_home()

def test_bank_manager_login_successful(go_to_login_page):
    """Test Case 3: Login as Manager
    Steps:
    1. Open Login Page
    2. Login as Manager  -- > Login should be successful"""

    login_page = LoginPage(go_to_login_page)
    manager_page = login_page.open_manager_page()
    manager_page.return_home()

def test_that_all_customers_are_available_on_customers_page(go_to_login_page):
    """Test Case 4: Check That All Customers Are Available on  Customers Page
    Steps:
    1. Open Login Page
    2. Login as Manager  -- > Login should be successful
    3. Get list of all customers available on Managers' Page
    4. Return to Login Page
    5. Open Customer's Login Page
    6. Get list of all customers available on Customers' Page
    7. Both list of customers should be equal"""

    login_page = LoginPage(go_to_login_page)
    manager_page = login_page.open_manager_page()
    customers_list_from_manager_page = manager_page.get_customers_list()
    manager_page.return_home()
    customer_page = login_page.open_manager_page()
    customers_list_from_customer_page = customer_page.get_customers_list()
    check_that_lists_are_equal(customers_list_from_manager_page, customers_list_from_customer_page)
