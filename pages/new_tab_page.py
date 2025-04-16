from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage

class NewTabPage(BasePage):
    NEW_TAB_LINK = (By.ID, 'new-page-link')

    def open(self):
        self.driver.get('https://www.qa-practice.com/elements/new_tab/link')

    def click_link_and_switch(self):
        self.wait.until(EC.element_to_be_clickable(self.NEW_TAB_LINK)).click()
        self.driver.switch_to.window(self.driver.window_handles[1])