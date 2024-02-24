from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):

    # def should_be_product_page(self):
    #     self.add_to_basket()
    #     self.should_be_same_price()
    #     self.should_be_same_name()

    def add_to_basket(self):
        add_to_basket_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
        add_to_basket_button.click()

    def should_be_same_price(self):
        price_product = self.browser.find_element(*ProductPageLocators.PRICE_PRODUCT)
        price_basket = self.browser.find_element(*ProductPageLocators.PRICE_BASKET)
        assert price_product.text == price_basket.text, 'Price is not equal to basket'

    def should_be_same_name(self):
        approved_name = self.browser.find_element(*ProductPageLocators.APPROVE_NAME)
        name_product = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME)
        assert approved_name.text == name_product.text, 'Name is not same'

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.APPROVE_NAME), \
            "Success message is presented, but should not be"

    def should_be_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.APPROVE_NAME), \
            "Success message is presented, but should not be"
