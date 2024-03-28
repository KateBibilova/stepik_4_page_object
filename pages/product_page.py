import math
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoAlertPresentException, TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def get(self):
        self.browser.get(self.url)

    def add_to_basket(self):
        login_link = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        login_link.click()

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        time.sleep(1)
        alert.accept()
        time.sleep(5)

        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

    def check_title(self):
        WebDriverWait(self.browser, 10).until(
            EC.visibility_of_element_located(ProductPageLocators.ACTUAL_TITLE)
        )
        actual_title_element = self.browser.find_element(*ProductPageLocators.ACTUAL_TITLE)
        actual_title = actual_title_element.text

        title_element = self.browser.find_element(*ProductPageLocators.EXPECTED_TITLE)
        expected_title = title_element.text

        assert actual_title == expected_title, (f"Название товара в уведомлении не совпадает: "
                                                f"ожидалось '{expected_title}', получено '{actual_title}'")

    def check_price(self):
        actual_price_element = self.browser.find_element(*ProductPageLocators.ACTUAL_PRICE)
        actual_price = actual_price_element.text

        price_element = self.browser.find_element(*ProductPageLocators.EXPECTED_PRICE)
        expected_price = price_element.text

        assert actual_price == expected_price, (f"Стоимость в уведомлении не совпадает: ожидалось '{expected_price}'"
                                                f", получено '{actual_price}'")

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def is_disappeared(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until_not(
                EC.presence_of_element_located((how, what))
            )
        except TimeoutException:
            return False

        return True
