from playwright.sync_api import Page


class DashboardPage:

    def __init__(self, page: Page):
        self.page = page
        self.boards_label = self.page.locator("#content").get_by_role("navigation").get_by_role("link", name=" Boards")


    def login(self, username, password):
        self.username_input.fill(username)
        self.continue_button.click()
        self.password_input.fill(password)
        self.login_button.click()