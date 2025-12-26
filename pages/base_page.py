from playwright.sync_api import Page, expect

class BasePage:
    def __init__(self, page: Page):
        self.page = page
    
    def navigate_to(self, url: str):
        self.page.goto(url)
    
    def get_current_url(self) -> str:
        return self.page.url
    
    def is_element_visible(self, locator: str) -> bool:
        return self.page.locator(locator).is_visible()
