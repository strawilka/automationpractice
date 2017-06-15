
import unittest
from selenium import webdriver

from automationpractice.registration_page import RegistrationPage


class TestRegistration(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.browser = webdriver.Chrome()

    def setUp(self):
        RegistrationPage(self.browser).open()

    def test_registration_with_different_passwords(self):
        page = RegistrationPage(self.browser)
        reg_data = {
            'first_name': 'Vova',
            'last_name': 'ZiLvova',
            'email': 'my_vovan_test@gmail.com',
            'password': 'pwd123',
            'confirmation': 'pwd1234'
        }

        for field, value in reg_data.items():
            page.find_element(field).send_keys(value)

        page.find_element('register_btn').click()

        self.assertEqual()