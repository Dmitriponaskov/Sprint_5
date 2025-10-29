import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import *
from faker import Faker

fake = Faker()


class TestRegistration:

    def test_register_new_user(self, driver):
        driver.get("https://qa-desk.stand.praktikum-services.ru/")
        driver.find_element(*BUTTON_LOGIN_SIGNUP).click()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located(MODAL))
        driver.find_element(*BUTTON_NO_ACCOUNT).click()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located(INPUT_EMAIL))

        email = fake.email()
        password = "Qwerty123!"

        driver.find_element(*INPUT_EMAIL).send_keys(email)
        driver.find_element(*INPUT_PASSWORD).send_keys(password)
        driver.find_element(*INPUT_REPEAT_PASSWORD).send_keys(password)
        driver.find_element(*BUTTON_REGISTER).click()

        WebDriverWait(driver, 15).until(EC.presence_of_element_located(USER_NAME))
        name = driver.find_element(*USER_NAME)
        assert name.text == "User."

    def test_register_invalid_email(self, driver):
        driver.get("https://qa-desk.stand.praktikum-services.ru/")
        driver.find_element(*BUTTON_LOGIN_SIGNUP).click()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located(MODAL))
        driver.find_element(*BUTTON_NO_ACCOUNT).click()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located(INPUT_EMAIL))

        driver.find_element(*INPUT_EMAIL).send_keys("invalid-email")
        driver.find_element(*BUTTON_REGISTER).click()

        error = WebDriverWait(driver, 10).until(EC.presence_of_element_located(ERROR_MESSAGE_SPAN))
        assert error.is_displayed()

    def test_register_existing_user(self, driver):
        driver.get("https://qa-desk.stand.praktikum-services.ru/")
        driver.find_element(*BUTTON_LOGIN_SIGNUP).click()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located(MODAL))
        driver.find_element(*BUTTON_NO_ACCOUNT).click()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located(INPUT_EMAIL))

        driver.find_element(*INPUT_EMAIL).send_keys("test@example.com")
        driver.find_element(*INPUT_PASSWORD).send_keys("password123")
        driver.find_element(*INPUT_REPEAT_PASSWORD).send_keys("password123")
        driver.find_element(*BUTTON_REGISTER).click()

        error = WebDriverWait(driver, 10).until(EC.presence_of_element_located(ERROR_MESSAGE_SPAN))
        assert error.is_displayed()