# Gathering locators for the elements in the page
# Using page object model
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class UsersPage():

    def __init__(self, driver):
        self.driver = driver
        self.add_button = (By.CSS_SELECTOR, 'button[type="add"]')
        self.first_name = (By.CSS_SELECTOR, '[name="FirstName"]')
        self.last_name = (By.CSS_SELECTOR, '[name="LastName"]')
        self.user_name = (By.CSS_SELECTOR, '[name="UserName"]')
        self.password = (By.CSS_SELECTOR, '[name="Password"]')
        self.role = (By.CSS_SELECTOR, '[name="RoleId"]')
        self.email = (By.CSS_SELECTOR, '[name="Email"]')
        self.phone = (By.CSS_SELECTOR, '[name="Mobilephone"]')
        self.role = (By.CSS_SELECTOR, '[name="RoleId"]')
        self.save = (By.CSS_SELECTOR, ".btn.btn-success")
        self.popup_ok_button = (By.CSS_SELECTOR, ".modal .btn-primary")

    def click_add(self):
        self.driver.find_element(*self.add_button).click()

    def enter_first_name(self, value):
        self.driver.find_element(*self.first_name).send_keys(value)

    def enter_last_name(self, value):
        self.driver.find_element(*self.last_name).send_keys(value)

    def enter_username(self, value):
        self.driver.find_element(*self.user_name).send_keys(value)

    def enter_password(self, value):
        self.driver.find_element(*self.password).send_keys(value)

    def select_customer(self, customer):
        self.driver.find_element(*(By.XPATH, "//label[contains(.,'" + customer + "')]/input")).click()

    def select_role(self, role):
        sel = Select(self.driver.find_element(*self.role))
        sel.select_by_visible_text(role)

    def enter_email(self, value):
        self.driver.find_element(*self.email).send_keys(value)

    def enter_phone(self, value):
        self.driver.find_element(*self.phone).send_keys(value)

    def click_save(self):
        self.driver.find_element(*self.save).click()

    def is_user_present(self, user_name):
        return len(self.driver.find_elements(*(By.XPATH, "//td[contains(text(),'" + user_name + "')]"))) > 0

    def delete_user(self, user_name):
        self.driver.find_element(
            *(By.XPATH,
              "//td[contains(text(),'" + user_name + "')]/parent::tr//i[contains(@class,'icon-remove')]")).click()

    def click_popup_ok_button(self):
        self.driver.find_element(*self.popup_ok_button).click()
