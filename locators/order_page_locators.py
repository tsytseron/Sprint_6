from selenium.webdriver.common.by import By

class OrderPageLocators:
    'Форма Для кого самокат'
    # Надпись Для кого самокат
    WHOSE_SCOOTER_INSCRIPTION = (By.XPATH, "//div[text()='Для кого самокат']")
    # Поле Имя
    NAME_FIELD = (By.XPATH, "//input[@placeholder='* Имя']")
    # Поле Фамилия
    LAST_NAME_FIELD = (By.XPATH, "//input[@placeholder='* Фамилия']")
    # Поле Адрес: куда привезти заказ
    ADDRESS_FIELD = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
    # Выпадающий список станций метро
    DROP_DOWN_METRO_LIST = (By.CLASS_NAME, "select-search__input")
    # Станция Сокольники
    SOKOLNIKI_STATION = (By.XPATH, "//div[text()='Сокольники']")
    # Поле Телефон: на него позвонит курьер
    PHONE_FIELD = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")
    # Кнопка Далее
    FARTHER_BUTTON = (By.CLASS_NAME, "Button_Button__ra12g.Button_Middle__1CSJM")
    'Форма Про аренду'
    # Надпись Про аренду
    RENT_INSCRIPTION = (By.XPATH, "//div[text()='Про аренду']")
    # Поле Когда привезти самокат
    DATE_FIELD = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
    # Выпадающий список срока аренды
    DROP_DOWN_RENT_LIST = (By.XPATH, "//div[text()='* Срок аренды']")
    # Вариант 'четверо суток' в списке срока аренды
    FOR_DAYS = (By.XPATH, "//div[@class = 'Dropdown-option' and text()='четверо суток']")
    # Чекбокс Серая безысходность
    BLACK_CHECKBOX = (By.ID, "grey")
    # Поле Комменрарий для курьера
    COMMENT_COURIER_FIELD = (By.XPATH, "//input[@placeholder='Комментарий для курьера']")
    # Кнопка Заказать
    ORDER_BUTTON = (By.XPATH, "//button[@class='Button_Button__ra12g Button_Middle__1CSJM' and text()='Заказать']")
    # Окно Хотите оформить заказ?
    WANT_ORDER_WINDOW = (By.XPATH, "Order_Modal__YZ-d3")
    # Кнопка Да в окне Хотите оформить заказ?
    YES_BUTTON = (By.XPATH, "//button[text()='Да']")
    # Надпись Заказ оформлен в окне Заказ оформлен
    ORDER_PLACED_INSCRIPTION = (By.CLASS_NAME, "Order_ModalHeader__3FDaJ")
    # Кнопка Посмотреть статус в окне Заказ оформлен
    VIEW_STATUS_BUTTON = (By.CLASS_NAME, "//button[text()='Посмотреть статус']")
