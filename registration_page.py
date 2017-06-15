from basepage import BasePage
from selenium.common.exceptions import NoSuchElementException


class RegistrationPage(BasePage):

    def __init__(self, browser):
        super(RegistrationPage).__init__(browser)
        self.url = 'http://magento-demo.lexiconn.com/customer/account/create/'
        self.locators = {
            'first_name': '//input[@id="firstname"]',
            'last_name': '//input[@id="lastname"]',
            'email': '//input[@id="email_address"]',
            'password': '//input[@id="password"]',
            'confirmation': '//input[@id="cpassword"]',
            'newsletter_chbx': '//checkbox[@id="is_subscribed"]',
            'register_btn': '//button[@title="Register" and @type="submit"]'
        }
        self.error_locators = {
            'password': '//div[@id="advice-validate-cpassword-confirmation"]'
        }

    @property
    def is_password_validation_error(self):
        try:
            self.browser.find_element_by_xpath(self.error_locators['password'])
        except NoSuchElementException:
            return False
        else:
            return True