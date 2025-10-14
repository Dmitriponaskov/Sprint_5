import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from locators import *
from faker import Faker

fake = Faker()


class TestCreateAd:

    def test_create_ad_unauthorized(self, driver):
        driver.get("https://qa-desk.stand.praktikum-services.ru/")
        driver.find_element(*BUTTON_POST_AD).click()
        # Неавторизованный пользователь перенаправляется на /login
        WebDriverWait(driver, 10).until(lambda d: "/login" in d.current_url)
        assert "/login" in driver.current_url

    def test_create_ad_authorized(self, driver):
        # Генерируем уникальное название объявления
        ad_title = fake.sentence(nb_words=3).rstrip(".")

        # Авторизация
        driver.get("https://qa-desk.stand.praktikum-services.ru/")
        driver.find_element(*BUTTON_LOGIN_SIGNUP).click()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located(MODAL))
        driver.find_element(*INPUT_EMAIL).send_keys("test@example.com")
        driver.find_element(*INPUT_PASSWORD).send_keys("password123")
        driver.find_element(*BUTTON_LOGIN_IN_MODAL).click()

        # Ждём появления имени пользователя
        WebDriverWait(driver, 15).until(EC.presence_of_element_located(USER_NAME))

        # Переход к созданию объявления
        driver.find_element(*BUTTON_POST_AD).click()

        # Ждём загрузки формы по заголовку
        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//h1[text()='Новое объявление']"))
        )

        # === Заполнение формы с надёжным вводом ===
        name_input = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.NAME, "name"))
        )
        name_input.click()
        name_input.clear()
        name_input.send_keys(ad_title)

        desc_input = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.NAME, "description"))
        )
        desc_input.click()
        desc_input.clear()
        desc_input.send_keys("Описание объявления")

        price_input = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.NAME, "price"))
        )
        price_input.click()
        price_input.clear()
        price_input.send_keys("1000")

        # Выбор состояния "Новый"
        new_radio = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//input[@value='Новый']"))
        )
        new_radio.click()

        # Публикация
        publish_btn = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(BUTTON_PUBLISH_AD)
        )
        publish_btn.click()

        # Подтверждение публикации
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//h1[text()='Объявление опубликовано']"))
        )

        # Переход в профиль и проверка наличия объявления
        driver.get("https://qa-desk.stand.praktikum-services.ru/profile")
        ad_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, f"//h2[text()='{ad_title}']"))
        )
        assert ad_element.is_displayed()