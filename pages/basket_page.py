from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_basket_is_empty_text(self):
        basket_is_empty = self.browser.find_element(*BasketPageLocators.BASKET_IS_EMPTY)
        assert "Your basket is empty. Continue shopping" == basket_is_empty.text, "Basket have a item"

    def should_be_basket_has_items(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_ITEMS), "Basket is empty"
