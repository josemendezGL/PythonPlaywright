import pytest
from ui.pom.login.login_page import LoginPage
from ui.pom.dashboard.dashboard_page import DashboardPage
from ui.pom.login.login_elements import LoginElements
from playwright.sync_api import Page, expect

@pytest.fixture(scope="session")
def browser_type_launch_args():
    return {
        "headless": False,
        "slow_mo": 500,
    }

def test_successful_login(page: Page):
    username = "josemendez.qaengineer@gmail.com"
    password = "123Queso!"

    login_page = LoginPage(page)

    login_page.login(username, password)

def test_failed_login(page: Page):
    username = "josemendez.qaengineer@gmail.not"
    password = "123Queso!"

    login_page = LoginPage(page)

    login_page.login(username, password)

    assert login_page.is_incorrect_email_message_displayed()