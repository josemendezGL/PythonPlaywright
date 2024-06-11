import re
from playwright.sync_api import Page, expect

def test_has_title(page: Page):
    
    page.goto("https://trello.com")
    page.get_by_test_id("bignav").get_by_role("link", name="Log in").click()


    