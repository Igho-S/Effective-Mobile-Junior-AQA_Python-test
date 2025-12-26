import pytest
import allure
from playwright.sync_api import Page, expect
from pages.login_page import LoginPage

@allure.feature("Авторизация")
@allure.suite("Тесты аутентификации")
class TestLogin:
    
    @pytest.fixture(autouse=True)
    def setup(self, page: Page):
        self.login_page = LoginPage(page)
        self.login_page.navigate()
        yield
    
    @allure.story("Успешный вход")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_successful_login(self, page: Page):
        # To test successful login with valid credentials
        with allure.step("Вход с учетной записью standard_user"):
            self.login_page.login("standard_user", "secret_sauce")
        
        with allure.step("Проверка URL содержит inventory"):
            expect(page).to_have_url("https://www.saucedemo.com/inventory.html")
        
        with allure.step("Проверка отображения контейнера inventory"):
            assert self.login_page.is_inventory_displayed(), "Страница inventory не отображается"
    
    @allure.story("Неверный пароль")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_login_with_incorrect_password(self, page: Page):
        # To test login with incorrect password
        with allure.step("Вход с неверным паролем"):
            self.login_page.login("standard_user", "wrong_password")
        
        with allure.step("Проверка отображения сообщения об ошибке"):
            assert self.login_page.is_error_displayed(), "Сообщение об ошибке не отображается"
        
        with allure.step("Проверка текста сообщения об ошибке"):
            error_text = self.login_page.get_error_message()
            assert "Username and password do not match" in error_text
    
    @allure.story("Заблокированный пользователь")
    @allure.severity(allure.severity_level.BLOCKER)
    def test_locked_out_user(self, page: Page):
        #To test login with locked out user
        with allure.step("Вход с учетной записью locked_out_user"):
            self.login_page.login("locked_out_user", "secret_sauce")
        
        with allure.step("Проверка сообщения об ошибке для заблокированного пользователя"):
            assert self.login_page.is_error_displayed(), "Сообщение об ошибке не отображается"
            error_text = self.login_page.get_error_message()
            assert "locked out" in error_text.lower()
    
    @allure.story("Пустые поля")
    @allure.severity(allure.severity_level.NORMAL)
    def test_login_with_empty_fields(self, page: Page):
        #To test login with empty username and password
        with allure.step("Нажатие кнопки входа с пустыми полями"):
            self.login_page.login("", "")
        
        with allure.step("Проверка отображения сообщения об ошибке"):
            assert self.login_page.is_error_displayed(), "Сообщение об ошибке не отображается"
            error_text = self.login_page.get_error_message()
            assert "Username is required" in error_text
    
    @allure.story("Пользователь с задержкой производительности")
    @allure.severity(allure.severity_level.NORMAL)
    def test_performance_glitch_user(self, page: Page):
        #To test login with performance_glitch_user and handle delays
        with allure.step("Вход с учетной записью performance_glitch_user"):
            self.login_page.login("performance_glitch_user", "secret_sauce")
        
        with allure.step("Ожидание загрузки страницы inventory несмотря на задержки"):
            page.wait_for_url("https://www.saucedemo.com/inventory.html", timeout=30000)
        
        with allure.step("Проверка корректности URL"):
            expect(page).to_have_url("https://www.saucedemo.com/inventory.html")
        
        with allure.step("Проверка отображения контейнера inventory"):
            assert self.login_page.is_inventory_displayed(), "Inventory не загружен"
