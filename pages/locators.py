from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.ID, "registration_link")


class LoginPageLocators():
    LOGIN_FORM = (By.ID, "login_form")
    REGISTER_FORM = (By.ID, "register_form")
    EMAIL_FORM = (By.ID, "id_registration-email")
    PASSWORD_FORM = (By.ID, "id_registration-password1")
    PASSWORD_FORM_2 = (By.ID, "id_registration-password2")
    REGISTRATION_BUTTON = (By.XPATH, '//*[@id="register_form"]/button')



class ProductPageLocators():
    ADD_TO_BASKET = (By.XPATH, '//*[@id="add_to_basket_form"]/button')
    PRODUCT_NAME = (By.XPATH, '//*[@id="content_inner"]/article/div[1]/div[2]/h1')
    APPROVE = (By.XPATH, '//*[@id=""]')
    APPROVE_NAME = (By.XPATH, '//*[@id="messages"]/div[1]/div/strong')
    PRICE_PRODUCT = (By.XPATH, '//*[@id="content_inner"]/article/div[1]/div[2]/p[1]')
    PRICE_BASKET = (By.XPATH, '//*[@id="messages"]/div[3]/div/p[1]/strong')
    SUCCESS_MESSAGE = (By.XPATH, '//*[@id="messages"]/div[1]/div/strong')


class BasePageLocators():
    LOGIN_LINK = (By.ID, "registration_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class BasketPageLocators():
    BASKET_LINK = (By.XPATH, '//*[@id="default"]/header/div[1]/div/div[2]/span/a')
    BASKET_ITEMS = (By.CLASS_NAME, 'basket_item')
    BASKET_IS_EMPTY = (By.XPATH, '//*[@id="content_inner"]/p')
