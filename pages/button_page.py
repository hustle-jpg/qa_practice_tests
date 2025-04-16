from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage


class ButtonPage(BasePage):
    RESULT_TEXT = (By.ID, 'result-text')


    def open(self):
        self.driver.get('https://www.qa-practice.com/elements/button/simple')

    def click_button(self):
        self.wait.until(EC.element_to_be_clickable(self.SUBMIT_BUTTON)).click()