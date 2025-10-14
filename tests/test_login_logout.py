import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import *


class TestLoginLogout:

    def test_login_user(self, driver):
        driver.get("https://qa-desk.stand.praktikum-services.ru/")
        driver.find_element(*BUTTON_LOGIN_SIGNUP).click()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located(MODAL))
        driver.find_element(*INPUT_EMAIL).send_keys("test@example.com")
        driver.find_element(*INPUT_PASSWORD).send_keys("password123")
        driver.find_element(*BUTTON_LOGIN_IN_MODAL).click()

        WebDriverWait(driver, 15).until(EC.presence_of_element_located(USER_NAME))
        name = driver.find_element(*USER_NAME)
        assert name.text == "User."

    def test_logout_user(self, driver):
        driver.get("https://qa-desk.stand.praktikum-services.ru/")
        driver.find_element(*BUTTON_LOGIN_SIGNUP).click()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located(MODAL))
        driver.find_element(*INPUT_EMAIL).send_keys("test@example.com")
        driver.find_element(*INPUT_PASSWORD).send_keys("password123")
        driver.find_element(*BUTTON_LOGIN_IN_MODAL).click()

        WebDriverWait(driver, 15).until(EC.presence_of_element_located(USER_NAME))
        driver.find_element(*BUTTON_LOGOUT).click()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located(BUTTON_LOGIN_SIGNUP))
        assert True