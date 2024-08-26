from selenium.webdriver.common.by import By

class MainPageLocators:
    'Главная страница'
    # Надпись Самокат на пару дней
    TWO_DAYS_INSCRIPTION = (By.CLASS_NAME, "Home_Header__iJKdX")
    # Кнопка Заказать в основном контенте
    MAIN_ORDER_BUTTON = (By.XPATH, "//div[contains(@class,'Home_FinishButton')]/button[text()='Заказать']")
    # Надпись Вопросы о важном
    IMPORTANT_QUESTS_INSCRIPTION = (By.XPATH, "//div[text()='Вопросы о важном']")
    # Вопрос выпадающго списка
    DROP_DOWN_LIST_QUESTION = (By.ID, "accordion__heading-{}")
    # Ответ в выпадающем списке
    DROP_DOWN_LIST_ANSWER = (By.ID, "accordion__panel-{}")
