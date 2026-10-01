from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class QuotePage(BasePage):

    INSURANCE_TYPE = (By.ID, "insuranceType")
    REGISTRATION = (By.ID, "registration")
    MAKE = (By.ID, "make")
    MODEL = (By.ID, "model")
    CONTINUE_BUTTON = (By.ID, "continueButton")

    def enter_vehicle_details(
        self,
        insurance_type,
        registration,
        make,
        model
    ):
        self.select_by_visible_text(
            self.INSURANCE_TYPE,
            insurance_type
        )

        self.enter_text(
            self.REGISTRATION,
            registration
        )

        self.enter_text(
            self.MAKE,
            make
        )

        self.enter_text(
            self.MODEL,
            model
        )

    def click_continue(self):
        self.click(self.CONTINUE_BUTTON)