import allure
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators.base_page_locators import BasePageLocators

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Ожидание {locator}')
    def wait_element(self, locator):
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    @allure.step('Ожидание возможности клика по {locator}')
    def wait_element_clickable(self, locator):
        element = WebDriverWait(self.driver, 5).until(expected_conditions.element_to_be_clickable(locator))
        return element

    @allure.step('Клик по {locator}')
    def click_element(self, locator):
        self.driver.find_element(*locator).click()

    @allure.step('Клик по кнопке да все привыкли')
    def click_cookie_button(self):
        self.wait_element(BasePageLocators.COOKIE_BUTTON)
        self.click_element(BasePageLocators.COOKIE_BUTTON)

    @allure.step('Клик по Яндекс')
    def click_yandex_logo(self):
        self.click_element(BasePageLocators.YANDEX_LOGO)

    @allure.step('Переключение на последнее открытое окно с активного')
    def switch_to_last_window(self):
        self.driver.switch_to.window(self.driver.window_handles[-1])

    @allure.step('Ожидание {url} в новом окне')
    def wait_for_url(self, url):
        self.switch_to_last_window()
        url = self.wait_url_contains(url)
        return url

    @allure.step('Клик по Самокат')
    def click_scooter_logo(self):
        self.click_element(BasePageLocators.SCOOTER_LOGO)

    @allure.step('Скроллинг к {locator}')
    def scroll_to_element(self, locator):
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step('Ввод {text} в {locator}')
    def enter_text(self, locator, text):
        self.wait_element_clickable(locator)
        self.driver.find_element(*locator).send_keys(text)

    @allure.step('Клик на Заказать в шапке')
    def click_header_button_order(self):
        self.click_element(BasePageLocators.ORDER_BUTTON)

    @allure.step('Ожидание URL текущей страницы')
    def wait_url_contains(self, url):
        WebDriverWait(self.driver, 10).until(expected_conditions.url_contains(url))
        return self.driver.current_url
