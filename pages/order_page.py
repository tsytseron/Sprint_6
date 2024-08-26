import allure
from data import date
from locators.order_page_locators import OrderPageLocators
from pages.base_page import BasePage

class OrderPage(BasePage):

    @allure.step('Заполнение поля Имя')
    def input_name(self, name):
        self.enter_text(OrderPageLocators.NAME_FIELD, name)

    @allure.step('Заполнение поля Фамилия')
    def input_surname(self, lastname):
        self.enter_text(OrderPageLocators.LAST_NAME_FIELD, lastname)

    @allure.step('Заполнение поля Адрес: куда привезти заказ')
    def input_address(self, address):
        self.enter_text(OrderPageLocators.ADDRESS_FIELD, address)

    @allure.step('Выбор станции Сокольники в выпадающем списке станций метро')
    def choose_metro(self, metro):
        self.click_element(OrderPageLocators.DROP_DOWN_METRO_LIST)
        self.enter_text(OrderPageLocators.DROP_DOWN_METRO_LIST, metro)
        self.click_element(OrderPageLocators.SOKOLNIKI_STATION)

    @allure.step('Заполнение поля Телефон: на него позвонит курьер')
    def input_phone_number(self, number):
        self.enter_text(OrderPageLocators.PHONE_FIELD, number)

    @allure.step('Заполнение поля Когда привезти самокат')
    def input_date_start_rent(self):
        self.enter_text(OrderPageLocators.DATE_FIELD, date)
        self.click_element(OrderPageLocators.RENT_INSCRIPTION)

    @allure.step('Выбор длительности аренды в выпадающем списке срока аренды')
    def choose_rent_period(self):
        self.click_element(OrderPageLocators.DROP_DOWN_RENT_LIST)
        self.click_element(OrderPageLocators.FOR_DAYS)

    @allure.step('Заполнение страницы заказа деталями аренды')
    def enter_rental_details(self, name, lastname, address, metro, number):
        self.input_name(name)
        self.input_surname(lastname)
        self.input_address(address)
        self.choose_metro(metro)
        self.input_phone_number(number)
        self.click_element(OrderPageLocators.FARTHER_BUTTON)
        self.wait_element(OrderPageLocators.RENT_INSCRIPTION)
        self.input_date_start_rent()
        self.choose_rent_period()
        self.click_element(OrderPageLocators.ORDER_BUTTON)
        self.click_element(OrderPageLocators.YES_BUTTON)

    @allure.step('Ожидание подтверждения оформления заказа')
    def waiting_order_confirmation(self):
        element = self.wait_element(OrderPageLocators.ORDER_PLACED_INSCRIPTION)
        return element.text
