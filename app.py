from playwright.sync_api import *

def test_users_api(page: Page):
    page.goto("https://trello.com")
    
   