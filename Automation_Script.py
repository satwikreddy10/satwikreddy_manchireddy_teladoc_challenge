# Adding a user and deleting user novak
import unittest

from selenium import webdriver
from Users_Page import UsersPage


class Automation(unittest.TestCase):

    def test_add_user(self=None):

        self.driver = webdriver.Chrome()
        self.driver.get('https://www.way2automation.com/angularjs-protractor/webtables/')
        self.driver.maximize_window()

        # Adding the user and validate that user is added to the table
        user_page = UsersPage(self.driver)
        user_page.click_add()
        user_page.enter_first_name("test_firstname")
        user_page.enter_last_name("test_lastname")
        user_page.enter_username("test_username")
        user_page.enter_password("test_password")
        user_page.select_customer("Company BBB")
        user_page.select_role("Admin")
        user_page.enter_email("sample.test@gmail.com")
        user_page.enter_phone("9903280129")
        user_page.click_save()
        self.assertEqual(True, user_page.is_user_present("test_username"))
        self.driver.quit()

    def test_delete_user(self=None):

        self.driver = webdriver.Chrome()
        self.driver.get('https://www.way2automation.com/angularjs-protractor/webtables/')
        self.driver.maximize_window()

        # Deleting user novak and validate that user is deleted from the table
        user_page = UsersPage(self.driver)
        user_page.delete_user("novak")
        user_page.click_popup_ok_button()
        self.assertEqual(False, user_page.is_user_present("novak"))
        self.driver.quit()
