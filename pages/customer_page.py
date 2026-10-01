from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class CustomerPage(BasePage):

    FIRST_NAME = (By.ID, "firstName")
    LAST_NAME = (By.ID, "lastName")
    ID_NUMBER = (By.ID, "idNumber")
    EMAIL = (By.ID, "email")
    PHONE = (By.ID, "phone")
    AGE = (By.ID, "age")
    CONTINUE_BUTTON = (By.ID, "continueButton")
    SUBMIT_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")
    ERROR_MESSAGE = (By.ID, "errorMessage")

    def __init__(self, driver):
        super().__init__(driver)

    def enter_customer_details(
        self,
        first_name,
        last_name,
        id_number,
        email,
        phone,
        age
    ):
        self.enter_text(self.FIRST_NAME, first_name)
        self.enter_text(self.LAST_NAME, last_name)
        self.enter_text(self.ID_NUMBER, id_number)
        self.enter_text(self.EMAIL, email)
        self.enter_text(self.PHONE, phone)
        self.enter_text(self.AGE, age)

    def click_continue(self):
        self.click(self.CONTINUE_BUTTON)

    def submit(self):
        self.click(self.SUBMIT_BUTTON)

    def get_error_message(self):
        return self.get_text(self.ERROR_MESSAGE)