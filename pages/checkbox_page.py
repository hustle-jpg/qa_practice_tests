from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage

class CheckBoxPage(BasePage):
    CHECKBOX = (By.ID, 'id_checkbox_0')

    def open(self):
        self.driver.get('https://www.qa-practice.com/elements/checkbox/single_checkbox')

    def click_checkbox(self):
        self.wait.until(EC.element_to_be_clickable(self.CHECKBOX)).click()

    def click_button(self):
        self.wait.until(EC.element_to_be_clickable(self.SUBMIT_BUTTON)).click()