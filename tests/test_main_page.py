import allure
import pytest
from data import answer_text, DZEN_WEBSITE
from pages.base_page import BasePage
from pages.main_page import MainPage
from pages.order_page import OrderPage


class TestMainPage:

    @allure.title('Клик по Яндекс и переход на Дзен')
    @allure.description('После клика по Яндекс в новом окне открывается Дзен')
    def test_check_yandex_logo_click(self, driver):
        base_page = BasePage(driver)
        base_page.click_yandex_logo()
        url = base_page.wait_for_url(DZEN_WEBSITE)
        assert DZEN_WEBSITE in url

    @allure.title('Клик по Самокат')
    @allure.description('После клика на самокат попадаем на главную страницу')
    def test_check_scooter_logo_click(self, driver):
        order_page = OrderPage(driver)
        base_page = BasePage(driver)
        order_page.click_header_button_order()
        order_url = driver.current_url
        base_page.click_scooter_logo()
        home_url = driver.current_url
        assert order_url != home_url


    @allure.title('Ответ соответствует вопросу в блоке Вопросы о важном')
    @allure.description('При клике на вопрос выпадает нужный ответ')
    @pytest.mark.parametrize("index, answer_text",
                             [(0, answer_text[0]),
                              (1, answer_text[1]),
                              (2, answer_text[2]),
                              (3, answer_text[3]),
                              (4, answer_text[4]),
                              (5, answer_text[5]),
                              (6, answer_text[6]),
                              (7, answer_text[7])])
    def test_check_answers(self, driver, index, answer_text):
        main_page = MainPage(driver)
        main_page.click_cookie_button()
        main_page.scroll_to_questions()
        question = main_page.click_question(index)
        result = main_page.find_answer(index)
        assert answer_text[question] == result
