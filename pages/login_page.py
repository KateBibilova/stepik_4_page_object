from selenium.common import TimeoutException

from .base_page import BasePage
from .locators import LoginPageLocators, RegistrationFormLocators
import pytest
import faker
import random
import string
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "Substring 'login' is not present in current URL"
        assert True

    def should_be_login_form(self):
        self.browser.find_element(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"
        assert True

    def should_be_register_form(self):
        self.browser.find_element(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"
        assert True

    def register_new_user(self):
        f = faker.Faker()
        email = f.email()
        password = ''.join([random.choice(string.ascii_letters + string.digits) for n in range(10)])

        email_field = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located(RegistrationFormLocators.EMAIL_FIELD))
        email_field.send_keys(email)

        password_field = self.browser.find_element(*RegistrationFormLocators.PASSWORD_FIELD)
        password_field.send_keys(password)

        confirm_password_field = self.browser.find_element(*RegistrationFormLocators.CONFIRM_PASSWORD_FIELD)
        confirm_password_field.send_keys(password)

        register_button = self.browser.find_element(*RegistrationFormLocators.REGISTER_BUTTON)
        register_button.click()

    def check_registration(self):
        wait = WebDriverWait(self.browser, 3)
        try:
            thanks_for_registration_message = wait.until(
                EC.presence_of_element_located((By.ID, "THANKS_FOR_REGISTRATION_MESSAGE")))
        except TimeoutException:
            print("The thanks for registration message did not appear after registration")
