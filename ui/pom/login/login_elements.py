from playwright.sync_api import Page

class LoginElements:

    def __init__(self, page: Page):
        self.page = page

        self.username_input = self.page.get_by_test_id("username")
        self.continue_button = self.page.get_by_role("button", name="Continue")
        self.password_input = self.page.get_by_test_id("password")
        self.login_button = self.page.get_by_role("button", name="Log in")
        self.incorrectEmail_label = self.page.get_by_text("Incorrect email address and")
        self.boards_label = self.page.get_by_role("navigation").get_by_role("link", name="Boards")
