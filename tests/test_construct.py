from selenium.webdriver.common.by import By
from Locators import TestLocatorsElementsConstruct


class TestClickElements:
    def test_elements_in_construction(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site")

        driver.find_element(By.XPATH, TestLocatorsElementsConstruct.SAUCE_TAB).click()
        element_1 = driver.find_element(By.XPATH, TestLocatorsElementsConstruct.HEADER_SAUCE)
        driver.execute_script("arguments[0].scrollIntoView();", element_1)

        assert element_1.text == 'Соусы'

        driver.find_element(By.XPATH, TestLocatorsElementsConstruct.BULK_TAB).click()
        element_2 = driver.find_element(By.XPATH, TestLocatorsElementsConstruct.HEADER_BULK)
        driver.execute_script("arguments[0].scrollIntoView();", element_2)

        assert element_2.text == 'Булки'

        driver.find_element(By.XPATH, TestLocatorsElementsConstruct.TOPPING_TAB).click()
        element_3 = driver.find_element(By.XPATH, TestLocatorsElementsConstruct.HEADER_TOPPING)
        driver.execute_script("arguments[0].scrollIntoView();", element_3)

        assert element_3.text == 'Начинки'
