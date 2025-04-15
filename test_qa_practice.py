from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

def test_click_button(driver):
    driver.get('https://www.qa-practice.com/elements/button/simple')
    driver.find_element(By.ID, 'submit-id-submit').click()
    element = driver.find_element(By.ID, 'result-text')
    assert element.text == 'Submitted'

def test_checkbox(driver):
    driver.get('https://www.qa-practice.com/elements/checkbox/single_checkbox')
    driver.find_element(By.ID, 'id_checkbox_0').click()
    driver.find_element(By.ID, 'submit-id-submit').click()
    element = driver.find_element(By.ID, 'result-text')
    assert element.text == 'select me or not'

def test_select_programming_language(driver):
    driver.get('https://www.qa-practice.com/elements/select/single_select')
    dropdown = Select(driver.find_element(By.ID, "id_choose_language"))
    dropdown.select_by_index(1)
    selected_option = dropdown.first_selected_option
    assert selected_option.text == 'Python'

def test_open_new_page(driver):
    driver.get('https://www.qa-practice.com/elements/new_tab/link')
    driver.find_element(By.ID, 'new-page-link').click()
    driver.switch_to.window(driver.window_handles[1])
    new_window_element = driver.find_element(By.ID, 'result-text')
    assert new_window_element.text == 'I am a new page in a new tab'

def test_alert_appears(driver):
    driver.get('https://www.qa-practice.com/elements/alert/alert#')
    driver.find_element(By.CSS_SELECTOR, '.a-button').click()
    alert = Alert(driver)
    assert alert.text == 'I am an alert!'
    alert.accept()