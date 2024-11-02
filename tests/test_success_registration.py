from selenium.webdriver.common.by import By
from Locators import TestLocatorsReg


class TestRegistry:
    def test_reg(self, driver):
        driver = driver
        driver.get("https://stellarburgers.nomoreparties.site/register")

        driver.find_element(By.XPATH, TestLocatorsReg.INPUT_REGISTRATION_NAME).send_keys("bezuglova")
        driver.find_element(By.XPATH, TestLocatorsReg.INPUT_REGISTRATION_EMAIL).send_keys(
            "anastasiia_bezuglova_15_111@ya.ru")
        driver.find_element(By.XPATH, TestLocatorsReg.INPUT_REGISTRATION_PSWD).send_keys("bezuglova")
        driver.find_element(By.XPATH, TestLocatorsReg.REG_BUTTON).click()

        driver.quit()
