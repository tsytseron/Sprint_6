from selenium.webdriver.common.by import By

class BasePageLocators:
    'Общие элементы'
    # Кнопка да все привыкли
    COOKIE_BUTTON = (By.ID, "rcc-confirm-button")
    # Логотип Яндекс
    YANDEX_LOGO = (By.XPATH, "//a[contains(@class,'Header_LogoYandex')]")
    # Логотип Самокат
    SCOOTER_LOGO = (By.XPATH, "//a[contains(@class,'Header_LogoScooter')]")
    # Кнопка Заказать в шапке
    ORDER_BUTTON = (By.XPATH, "//div[contains(@class,'Header_Nav')]/button[text()='Заказать']")
    # Кнопка Статус заказа
    STATUS_BUTTON = (By.XPATH, "//div[contains(@class,'Header_Nav')]/button[text()='Статус заказа']")
    # Поле ввода номера заказа
    NUMBER_FIELD = (By.XPATH, "//input[@placeholder='Введите номер заказа']")
    # Кнопка Go!
    GO_BUTTON = (By.XPATH, "//div[contains(@class,'Header_SearchInput')]/button[text()='Go!']")
