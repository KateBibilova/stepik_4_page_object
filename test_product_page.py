from .pages.basket_page import BasketPage
from .pages.locators import ProductPageLocators
from .pages.login_page import *
from .pages.product_page import ProductPage


# раздел 4.3 задание 4: Задание: независимость контента, ищем баг
class TestOfferPages:
    @pytest.mark.parametrize('link', [
        "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
        "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
        "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
        "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
        "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
        "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
        "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
        pytest.param(
            "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
            marks=pytest.mark.xfail(reason="This offer is expected to fail")
        ),
        "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
        "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"
    ])
    @pytest.mark.need_review
    def test_guest_can_add_product_to_basket(self, browser, link):
        page = ProductPage(browser, link)
        page.open()
        page.add_to_basket()
        page.solve_quiz_and_get_code()
        page.check_title()
        page.check_price()


# раздел 4.3 задание 6: Задание: отрицательные проверки
class TestNegativeChecks:
    def test_guest_cant_see_success_message_after_adding_product_to_basket(self, browser):
        page = ProductPage(browser,
                           "http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/?promo=offer0")
        page.open()
        page.add_to_basket()
        page.is_element_present(*ProductPageLocators.SUCCESS_MESSAGE)

    def test_guest_cant_see_success_message(self, browser):
        page = ProductPage(browser,
                           "http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/?promo=offer0")
        page.open()
        page.is_element_present(*ProductPageLocators.SUCCESS_MESSAGE)

    def test_message_disappeared_after_adding_product_to_basket(self, browser):
        page = ProductPage(browser,
                           "http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/?promo=offer0")
        page.open()
        page.add_to_basket()
        page.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE)


# раздел 4.3 задание 8: Плюсы наследования: пример
# оба теста должны проходить, так как я поправила селекторы на нужные, как это посоветовали
# сделать в комментариях к заданию (а именно не использовала LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
class TestAdvantagesOfInheritance:
    def test_guest_should_see_login_link_on_product_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
        page = ProductPage(browser, link)
        page.open()
        page.should_be_login_link()

    @pytest.mark.need_review
    def test_guest_can_go_to_login_page_from_product_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
        page = ProductPage(browser, link)
        page.open()
        page.go_to_login_page()


# раздел 4.3 задание 10: Задание: наследование и отрицательные проверки
class TestBasketCheck:
    @pytest.mark.need_review
    def test_guest_cant_see_product_in_basket_opened_from_product_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/hacking-exposed-wireless_208/"
        page = ProductPage(browser, link)
        page.open()
        page.go_to_basket()
        # Создаем экземпляр страницы корзины и вызываем метод проверки сообщения об отсутствии товара в корзине
        basket_page = BasketPage(browser, browser.current_url)
        basket_page.should_not_be_product_in_basket()


# раздел 4.3 задание 13: Задание: группировка тестов и setup
class TestUserAddToBasketFromProductPage:
    @pytest.fixture
    def setup(self, browser):
        login_page_url = "https://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
        page = LoginPage(browser, login_page_url)
        page.open()
        page.register_new_user()
        page.check_registration()

    @pytest.mark.need_review
    @pytest.mark.usefixtures("setup")
    def test_user_can_add_product_to_basket(self, browser):
        link = "https://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/"
        page = ProductPage(browser, link)
        page.open()
        page.add_to_basket()
        page.check_title()
        page.check_price()

    @pytest.mark.usefixtures("setup")
    def test_user_cant_see_success_message(self, browser):
        page = ProductPage(browser,
                           "https://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/")
        page.open()
        page.is_element_present(*ProductPageLocators.SUCCESS_MESSAGE)
