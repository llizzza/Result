from selenium.webdriver.common.by import By


class ProductPageLocators():
    # Кнопка "Добавить в корзину"
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, "button.btn-add-to-basket")

    # Название товара на странице
    PRODUCT_NAME = (By.CSS_SELECTOR, "div.product_main h1")
    # Цена товара на странице
    PRODUCT_PRICE = (By.CSS_SELECTOR, "div.product_main p.price_color")

    # Сообщение о том, что товар добавлен в корзину
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "div.alert-success:nth-child(1) strong")
    # Сообщение со стоимостью корзины
    BASKET_PRICE_MESSAGE = (By.CSS_SELECTOR, "div.alert-info strong")