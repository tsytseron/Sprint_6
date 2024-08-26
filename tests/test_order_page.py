import allure
import pytest
from data import personal_data
from pages.main_page import MainPage
from pages.order_page import OrderPage


class TestOrderPage:

    @allure.title('Заказ самоката по кнопке Заказать в шапке')
    @allure.description('Заказ самоката с 2 наборами данных по кнопке Заказать в шапке')
    @pytest.mark.parametrize('name, lastname, address, metro, number', [*personal_data])
    def test_successful_order_header_button(self, driver, name, lastname, address, metro, number):
        order_page = OrderPage(driver)
        order_page.click_header_button_order()
        order_page.enter_rental_details(name, lastname, address, metro, number)
        text_order = order_page.waiting_order_confirmation()
        assert "Заказ оформлен" in text_order

    @allure.title('Заказ самоката по кнопке Заказать в основном контенте')
    @allure.description('Заказ самоката с 2 наборами данных по кнопке Заказать в основном контенте')
    @pytest.mark.parametrize('name, lastname, address, metro, number', [*personal_data])
    def test_successful_order_bottom_button(self, driver, name, lastname, address, metro, number):
        order_page = OrderPage(driver)
        main_page = MainPage(driver)
        main_page.click_bottom_button_order()
        order_page.enter_rental_details(name, lastname, address, metro, number)
        text_order = order_page.waiting_order_confirmation()
        assert "Заказ оформлен" in text_order
