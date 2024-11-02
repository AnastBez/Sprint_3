from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from Locators import *
from time import sleep


class TestCaseLoginAcc:
    def test_login_account_into_personal_cabinet(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site/login")

        driver.find_element(By.XPATH, TestLocatorsLoginInput.INPUT_LOGIN_EMAIL).send_keys(
            "anastasiia_bezuglova_15_111@ya.ru")
        driver.find_element(By.XPATH, TestLocatorsLoginInput.INPUT_LOGIN_PSWD).send_keys("bezuglova")
        driver.find_element(By.XPATH, TestLocatorsLoginInput.LOGIN_BUTTON).click()

        WebDriverWait(driver, 10).until(
            expected_conditions.element_to_be_clickable((By.XPATH, TestLocatorsLogin.PERSONAL_ACCOUNT_BUTTON)))

        driver.find_element(By.XPATH, TestLocatorsLogin.PERSONAL_ACCOUNT_BUTTON).click()
        sleep(5)

        assert '/profile' in driver.current_url

        driver.find_element(By.XPATH, TestLocatorsOnAuthAcc.CONSTRUCTOR_BUTTON).click()

        assert driver.find_element(By.XPATH, '//*[@id="root"]/div/main/section[1]/h1').text == 'Соберите бургер'

        driver.find_element(By.XPATH, TestLocatorsOnAuthAcc.LOGO_BANNER).click()

        assert 'https://stellarburgers.nomoreparties.site/' == driver.current_url

        driver.find_element(By.XPATH, TestLocatorsLogin.PERSONAL_ACCOUNT_BUTTON).click()

        WebDriverWait(driver, 10).until(
            expected_conditions.visibility_of_element_located((By.XPATH, TestLocatorsOnAuthAcc.LOGOUT_BUTTON)))

        driver.find_element(By.XPATH, TestLocatorsOnAuthAcc.LOGOUT_BUTTON).click()
        sleep(5)

        assert '/login' in driver.current_url

        driver.quit()
