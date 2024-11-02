from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from Locators import TestLocatorsReg


class TestErrRegistry:
    def test_reg_password_less_six(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site/register")

        driver.find_element(By.XPATH, TestLocatorsReg.INPUT_REGISTRATION_NAME).send_keys("bezuglova")
        driver.find_element(By.XPATH, TestLocatorsReg.INPUT_REGISTRATION_EMAIL).send_keys(
            "anastasiia_bezuglova_15_111@ya.ru")
        driver.find_element(By.XPATH, TestLocatorsReg.INPUT_REGISTRATION_PSWD).send_keys("bez")
        driver.find_element(By.XPATH, TestLocatorsReg.REG_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(
            (By.XPATH, TestLocatorsReg.ERROR_PSWD)))
        assert driver.find_element(By.XPATH,
                                   "/html/body/div/div/main/div/form/fieldset[3]/div/p").text == 'Некорректный пароль'

        driver.quit()
