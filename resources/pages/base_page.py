class BasePage:
    def __init__(self, page):
        self.page = page
        self.home_button = page.get_by_role("button", name="Home")

    def return_home(self):
        self.home_button.click()

    def check_and_accept_alert(self, expected_text):
        def handle(dialog):
            if expected_text:
                assert expected_text in dialog.message
            dialog.accept()
        self.page.on("dialog", handle)