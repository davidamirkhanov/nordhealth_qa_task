from resources.pages.login_page import LoginPage

def test_e2e_customer_creation_and_deletion(go_to_login_page, page, customer_to_create):
    login_page = LoginPage(go_to_login_page)
    manager_page =  login_page.open_manager_page()
    manager_page.check_if_customer_exists(customer_name=customer_to_create, expected_result=False)
    manager_page.create_customer(customer_to_create)
    manager_page.return_home()
    customer_page = login_page.open_customer_page()
    customer_page.login_as_customer(customer_to_create.full_name())
    customer_page.return_home()
    manager_page = login_page.open_manager_page()
    manager_page.delete_customer(customer_to_create.full_name())
