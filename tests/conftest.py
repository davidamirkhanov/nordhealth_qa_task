import pytest
from playwright.sync_api import sync_playwright
import os
from dotenv import load_dotenv
from .customers import Customer
load_dotenv()

# environment variables
@pytest.fixture
def login_page_url():
    return os.getenv("LOGIN_PAGE_URL")

# test data
@pytest.fixture
def existing_customer():
    return Customer(name="Hermoine", surname="Granger", postcode="E859AB")

@pytest.fixture
def customer_to_create():
    return Customer(name="Dolores Jane", surname="Umbridge", postcode="SW1A0PW")

# browser and pages
@pytest.fixture(scope="session")
def browser_instance():
    headless = bool(os.getenv("HEADLESS", False))
    browser_type = os.getenv("BROWSER", "chromium")

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=headless, channel=browser_type)
        yield browser
        browser.close()

@pytest.fixture(scope="function")
def page(browser_instance):
    context = browser_instance.new_context()
    context.set_default_timeout(5000)
    context.set_default_navigation_timeout(20000)
    page = browser_instance.new_page()
    yield page
    page.close()

@pytest.fixture
def go_to_login_page(page, login_page_url):
    page.goto(login_page_url)
    yield page

