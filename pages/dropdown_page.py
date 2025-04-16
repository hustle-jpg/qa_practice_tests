from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from pages.base_page import BasePage

class DropdownPage(BasePage):
    LANGUAGE_DROPDOWN = (By.ID, 'id_choose_language')

    def open(self):
        self.driver.get('https://www.qa-practice.com/elements/select/single_select')

    def select_language(self, language: str):
        dropdown_element = self.wait.until(presence_of_element_located(self.LANGUAGE_DROPDOWN))
        dropdown = Select(dropdown_element)
        dropdown.select_by_visible_text(language)
        return dropdown.first_selected_option.text