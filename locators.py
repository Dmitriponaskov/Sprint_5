from selenium.webdriver.common.by import By

# === Общие элементы ===
BUTTON_LOGIN_SIGNUP = (By.XPATH, "//button[contains(text(), 'Вход и регистрация')]")
BUTTON_POST_AD = (By.XPATH, "//button[contains(text(), 'Разместить объявление')]")
USER_NAME = (By.CSS_SELECTOR, "h3.profileText.name")
BUTTON_LOGOUT = (By.XPATH, "//button[contains(text(), 'Выйти')]")

# === Модальное окно входа/регистрации ===
MODAL = (By.CSS_SELECTOR, ".popUp_shell__LuyqR")
BUTTON_NO_ACCOUNT = (By.XPATH, "//button[contains(text(), 'Нет аккаунта')]")
BUTTON_LOGIN_IN_MODAL = (By.XPATH, "//button[contains(text(), 'Войти')]")
BUTTON_REGISTER = (By.XPATH, "//button[contains(text(), 'Создать аккаунт')]")

# === Поля форм ===
INPUT_EMAIL = (By.NAME, "email")
INPUT_PASSWORD = (By.NAME, "password")
INPUT_REPEAT_PASSWORD = (By.NAME, "submitPassword")

# === Ошибки ===
ERROR_MESSAGE_SPAN = (By.CSS_SELECTOR, ".input_span__yWPqB")

# === Создание объявления ===
INPUT_NAME_AD = (By.NAME, "name")          # ← ИСПРАВЛЕНО: не "title", а "name"
INPUT_DESCRIPTION_AD = (By.NAME, "description")
INPUT_PRICE_AD = (By.NAME, "price")
INPUT_CATEGORY = (By.NAME, "category")     # readonly input
INPUT_CITY = (By.NAME, "city")             # readonly input
RADIOBUTTON_CONDITION_NEW = (By.XPATH, "//input[@value='Новый']")
BUTTON_PUBLISH_AD = (By.XPATH, "//button[contains(text(), 'Опубликовать')]")