from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')


class LoginPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    REGISTER_FORM = (By.CSS_SELECTOR, '#register_form')


class ProductPageLocators:
    ADD_TO_BASKET_BUTTON = (
        By.XPATH, "//button[contains(@class, 'btn-add-to-basket') and contains(text(), 'Add to basket')]"
    )
    ACTUAL_TITLE = (By.XPATH, "(//*[@id='messages']//strong)[1]")
    EXPECTED_TITLE = (By.XPATH, "//div[@class='col-sm-6 product_main']/h1")
    ACTUAL_PRICE = (By.XPATH, "(//*[@id='messages']//strong)[3]")
    EXPECTED_PRICE = (By.XPATH, "//p[@class='price_color']")
    SUCCESS_MESSAGE = (By.XPATH, "//*[@id='messages']/*[1]")


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    # LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.XPATH, '//a[@href="/en-gb/basket/" and contains(text(), "View basket")]')
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class BasketPageLocators:
    EMPTY_BASKET_MESSAGE = (By.XPATH, "//p[contains(text(), 'Your basket is empty.')]")
    PRODUCT_IN_BASKET_MESSAGE = (By.XPATH, "// h2[contains(text(), 'Items to buy now')]")


class RegistrationFormLocators:
    EMAIL_FIELD = (By.CSS_SELECTOR, "#id_registration-email")
    PASSWORD_FIELD = (By.CSS_SELECTOR, "#id_registration-password1")
    CONFIRM_PASSWORD_FIELD = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTER_BUTTON = (By.NAME, "registration_submit")
    THANKS_FOR_REGISTRATION_MESSAGE = (By.CSS_SELECTOR, "div.alertinner.wicon")
