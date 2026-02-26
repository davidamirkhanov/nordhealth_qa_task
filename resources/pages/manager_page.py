from .base_page import BasePage
from .customer_page import CustomerPage
from playwright.sync_api import expect

class ManagerPage(BasePage):
    """Manager's page class"""
    def __init__(self, page):
        super().__init__(page)
        self.add_customer_button = page.get_by_role("button", name="Add Customer").first
        self.open_account_button = page.get_by_role("button", name="Open Account")
        self.customers_button = page.get_by_role("button", name="Customers")
        self.first_name_input_field = page.get_by_role("textbox", name="First Name")
        self.last_name_input_field = page.get_by_role("textbox", name="Last Name")
        self.postcode_input_field = page.get_by_role("textbox", name="Post Code")
        self.add_customer_button_customer_creation = page.get_by_role("form").get_by_role("button", name="Add Customer")
        self.customers_search_input_field = page.get_by_placeholder("Search Customer")
        self.customers_list_table = page.get_by_role("table")
        self.customer_delete_button = page.get_by_role("button", name="Delete")

    def check_that_manager_page_is_opened(self):
        """Checks page elements"""
        expect(self.add_customer_button).to_be_visible()
        expect(self.open_account_button).to_be_visible()
        expect(self.customers_button).to_be_visible()

    def open_add_customer_tab(self):
        """Opens 'Add Customer' tab"""
        self.add_customer_button.click()
        expect(self.customers_search_input_field).to_be_visible()
        expect(self.customers_list_table).to_be_visible()

    def open_customer_list_tab(self):
        """Opens 'Customer List' tab"""
        self.customers_button.click()
        expect(self.customers_search_input_field).to_be_visible()
        expect(self.customers_list_table).to_be_visible()

    def get_customers_list(self):
        """Gets list of customer names (firls and last name) from the table"""
        customers_list = []
        self.open_customer_list_tab()
        all_table_rows = self.customers_list_table.get_by_role("row").all()
        for row in all_table_rows[1:]:  # exclude first line, because this is table header
            first_name = row.locator("td").nth(0).inner_text()
            last_name = row.locator("td").nth(1).inner_text()
            customers_list.append(f"{first_name} {last_name}")
        return customers_list

    def check_if_customer_exists(self, customer_name:str, expected_result:bool):
        """Checks if customer exists. Accepts 'expected_result' boolean. Compares existance of customer name with expected result
        If customer exists and expected_result is True, returns True
        If customer doesn't exist and expected_result is False, returns True
        In other cases returns False"""
        all_customers = self.get_customers_list()
        if expected_result and customer_name in all_customers:
            return True
        elif not expected_result and customer_name not in all_customers:
            return True
        else:
            return False

    def get_customer_place_in_the_list(self, customer_name:str):
        """Gets index of customer place in customer list"""
        all_customers = self.get_customers_list()
        return all_customers.index(customer_name)

    def create_customer(self, customer_data:list):
        """Creates customer, requires name, last name and postal code as list
        Checks if customer is created"""
        self.open_add_customer_tab()
        self.first_name_input_field.fill(customer_data.as_list()[0])
        self.last_name_input_field.fill(customer_data.as_list()[1])
        self.postcode_input_field.fill(customer_data.as_list()[2])
        self.check_and_accept_alert(expected_text="Customer added successfully with customer id :")
        self.add_customer_button_customer_creation.click()
        self.check_if_customer_exists(customer_name=customer_data.full_name(), expected_result=True)

    def delete_customer(self, customer_name:str):
        """Deletes customer. Checks if customer is deleted"""
        self.open_customer_list_tab()
        customer_place = self.get_customer_place_in_the_list(customer_name)
        self.customer_delete_button.nth(customer_place).click()
        self.check_if_customer_exists(customer_name, expected_result=False)