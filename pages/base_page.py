from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

class BasePage:
    RESULT_TEXT = (By.ID, 'result-text')
    SUBMIT_BUTTON = (By.ID, 'submit-id-submit')

    def __init__(self, driver, wait: WebDriverWait):
        self.driver = driver
        self.wait = wait

    def get_result_text(self):
        return self.driver.find_element(*self.RESULT_TEXT).text