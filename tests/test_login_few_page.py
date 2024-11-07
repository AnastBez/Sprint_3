from selenium.webdriver.common.by import By
from Locators import TestLocatorsLogin
from Locators import TestLocatorsLoginInput


class TestLoginMainPage:
    def test_auth_for_button_on_main_page(self, driver):
        url_main = "https://stellarburgers.nomoreparties.site"
        driver.get(url_main)

        driver.find_element(By.XPATH, TestLocatorsLogin.LOGIN_BUTTON_ON_MAIN_PAGE).click()  # Кнопка Войти
        assert '/login' in driver.current_url

        driver.find_element(By.XPATH, TestLocatorsLogin.PERSONAL_ACCOUNT_BUTTON).click()  # Личный кабинет
        assert '/login' in driver.current_url


class TestLoginRegPage:
    def test_auth_for_button_on_reg_page(self, driver):
        url_reg = "https://stellarburgers.nomoreparties.site/register"
        driver.get(url_reg)

        driver.find_element(By.XPATH, TestLocatorsLogin.LOGIN_BUTTON_ON_REG).click()  # регистрация
        assert '/login' in driver.current_url


class TestLoginReturnPage:
    def test_auth_for_button_on_return_page(self, driver):
        url_pswd = 'https://stellarburgers.nomoreparties.site/forgot-password'
        driver.get(url_pswd)

        driver.find_element(By.XPATH, TestLocatorsLogin.LOGIN_BUTTON_ON_RETURN).click()  # регистрация Восстановление

        driver.find_element(By.XPATH, TestLocatorsLoginInput.INPUT_LOGIN_EMAIL).send_keys(
            "anastasiia_bezuglova_15_111@ya.ru")
        driver.find_element(By.XPATH, TestLocatorsLoginInput.INPUT_LOGIN_PSWD).send_keys(
            "bezuglova")
        driver.find_element(By.XPATH, TestLocatorsLoginInput.LOGIN_BUTTON).click()
