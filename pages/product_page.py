import math
from selenium.common.exceptions import NoAlertPresentException
from pages.base_page import BasePage
from pages.locators import ProductPageLocators

class ProductPage(BasePage):
    def add_product_to_basket(self):
        basket_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        basket_button.click()

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"\nYour code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

    def get_product_name(self):
        # Метод, который вытаскивает название товара со страницы
        return self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text

    def get_product_price(self):
        # Метод, который вытаскивает цену товара со страницы
        return self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text

    def should_be_success_message(self, product_name):
        # Проверяем название в сообщении, сравнивая с переданным аргументом
        message_product_name = self.browser.find_element(*ProductPageLocators.SUCCESS_MESSAGE).text
        assert product_name == message_product_name, \
            f"Название товара в сообщении ('{message_product_name}') не совпадает с оригинальным ('{product_name}')!"

    def should_be_basket_price(self, product_price):
        # Проверяем стоимость корзины, сравнивая с переданным аргументом цены
        basket_price = self.browser.find_element(*ProductPageLocators.BASKET_PRICE_MESSAGE).text
        assert product_price == basket_price, \
            f"Стоимость корзины ('{basket_price}') не равна цене товара ('{product_price}')!"