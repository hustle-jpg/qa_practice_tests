from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.expected_conditions import alert_is_present
from pages.base_page import BasePage

class AlertPage(BasePage):
    ALERT_BUTTON = (By.CSS_SELECTOR, '.a-button')

    def open(self):
        self.driver.get('https://www.qa-practice.com/elements/alert/alert#')

    def trigger_alert_and_get_text(self):
        self.wait.until(EC.element_to_be_clickable(self.ALERT_BUTTON)).click()
        self.wait.until(alert_is_present())
        alert = Alert(self.driver)
        text = alert.text
        alert.accept()
        return text
