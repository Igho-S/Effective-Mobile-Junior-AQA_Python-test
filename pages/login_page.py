from playwright.sync_api import Page, expect
from pages.base_page import BasePage
import allure

class LoginPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.url = "https://www.saucedemo.com/"
        
        self.username_input = page.locator("#user-name")
        self.password_input = page.locator("#password")
        self.login_button = page.locator("#login-button")
        self.error_message = page.locator("[data-test='error']")
        self.inventory_container = page.locator(".inventory_container")
        
    @allure.step("Переход на страницу авторизации")
    def navigate(self):
        self.navigate_to(self.url)
    
    @allure.step("Вход с именем пользователя: {username}")
    def login(self, username: str, password: str):
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()
    
    @allure.step("Проверка отображения сообщения об ошибке")
    def is_error_displayed(self) -> bool:
        return self.error_message.is_visible()
    
    @allure.step("Получение текста сообщения об ошибке")
    def get_error_message(self) -> str:
        return self.error_message.text_content()
    
    @allure.step("Проверка отображения страницы inventory")
    def is_inventory_displayed(self) -> bool:
        return self.inventory_container.is_visible(timeout=10000)
