import pytest
from playwright.sync_api import Page
from ui.pom.login.login_elements import LoginElements

class LoginPage:

    def __init__(self, page: Page):
        self.page = page
        self.page.goto("http://trello.com")

        page.get_by_test_id("bignav").get_by_role("link", name="Log in").click()

        self.elements = LoginElements(page)

    def login(self, username, password):
        self.elements.username_input.fill(username)
        self.elements.continue_button.click()
        self.elements.password_input.fill(password)
        self.elements.login_button.click()

    def is_incorrect_email_message_displayed(self):
        return self.elements.incorrectEmail_label.is_visible()
