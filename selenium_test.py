import unittest

from selenium import webdriver

from automationpractice.login_page import LoginPage


class TestLogin(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.browser = webdriver.Chrome()
        cls.browser.implicitly_wait(2)

    def setUp(self):
        LoginPage(self.browser).open()


    def test_login_with_incorrect_pass(self):
        LoginPage(self.browser).login('s1iderorama@gmail.com', 'codespace')

        self.assertIn('Customer Login', self.browser.title)

    def test_forgot_password(self):
        LoginPage(self.browser).forgot_account()

        self.assertIn('Forgot Your Password', self.browser.title)

    @classmethod
    def tearDownClass(cls):
        cls.browser.quit()