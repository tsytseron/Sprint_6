import allure
from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage


class MainPage(BasePage):

    @allure.step('Клик на кнопку Заказать в основном контенте')
    def click_bottom_button_order(self):
        self.scroll_to_element(MainPageLocators.MAIN_ORDER_BUTTON)
        self.click_element(MainPageLocators.MAIN_ORDER_BUTTON)

    @allure.step('Скроллинг до блока Вопросы о важном')
    def scroll_to_questions(self):
        self.scroll_to_element(MainPageLocators.IMPORTANT_QUESTS_INSCRIPTION)

    @allure.step('Клик на вопрос в блоке Вопросы о важном')
    def click_question(self, index):
        selector, locator = MainPageLocators.DROP_DOWN_LIST_QUESTION
        locator = locator.format(index)
        self.wait_element((selector, locator))
        self.click_element((selector, locator))
        return self.wait_element((selector, locator)).get_attribute("id")

    @allure.step('Нахождение ответа в в выпадающем списке блока Вопросы о важном')
    def find_answer(self, index):
        selector, locator = MainPageLocators.DROP_DOWN_LIST_ANSWER
        locator = locator.format(index)
        element = self.wait_element((selector, locator))
        return element.text
