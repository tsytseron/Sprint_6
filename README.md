﻿Sprint_6

Автотесты с отчётами для сайта qa-scooter.praktikum-services.ru

allure_results: отчёты о тестировании

locators:  
base_page_locators.py - локаторы базовых элементов  
main_page_locators.py - локаторы элементов главной страницы  
order_page_locators.py - локаторы элементов страницы заказа

pages:  
base_page.py - базовые методы  
main_page.py - методы главной страницы  
order_page.py - методы страницы заказа

tests:  
test_main_page.py - тестирование лого Яндекс, лого Самокат и выпадающего списка вопросов  
test_order_page.py - тестирование заказа самоката по кнопкам Заказать в шапке и в основном контенте

conftest.py: фикстура

data.py: данные пользователя
