# from selenium.webdriver.common.alert import Alert
# from selenium.webdriver.support.expected_conditions import element_to_be_clickable, presence_of_element_located, \
#     alert_is_present
# from selenium.webdriver.support.ui import Select
# from selenium.webdriver.common.by import By
#
# RESULT_TEXT = (By.ID, 'result-text')
#
#
# def test_click_button(driver, wait):
#     driver.get('https://www.qa-practice.com/elements/button/simple')
#     wait.until(element_to_be_clickable((By.ID, 'submit-id-submit'))).click()
#     element = driver.find_element(*RESULT_TEXT)
#     assert element.text == 'Submitted', f'Expected "Submitted", but got "{element.text}"'
#
# def test_checkbox(driver, wait):
#     driver.get('https://www.qa-practice.com/elements/checkbox/single_checkbox')
#     wait.until(element_to_be_clickable((By.ID, 'id_checkbox_0'))).click()
#     wait.until(element_to_be_clickable((By.ID, 'submit-id-submit'))).click()
#     element = driver.find_element(*RESULT_TEXT)
#     assert element.text == 'select me or not', f'Expected "select me or not", but got "{element.text}"'
#
# def test_select_programming_language(driver, wait):
#     driver.get('https://www.qa-practice.com/elements/select/single_select')
#     dropdown = Select(wait.until(presence_of_element_located((By.ID, "id_choose_language"))))
#     dropdown.select_by_visible_text('Python')
#     selected_option = dropdown.first_selected_option
#     assert selected_option.text == 'Python', f'Expected "Python", but got "{selected_option.text}"'
#
# def test_open_new_page(driver, wait):
#     driver.get('https://www.qa-practice.com/elements/new_tab/link')
#     wait.until(element_to_be_clickable((By.ID, 'new-page-link'))).click()
#     driver.switch_to.window(driver.window_handles[1])
#     new_window_element = driver.find_element(*RESULT_TEXT)
#     assert new_window_element.text == 'I am a new page in a new tab', f'Expected "I am a new page in a new tab", but got "{new_window_element.text}"'
#
# def test_alert_appears(driver, wait):
#     driver.get('https://www.qa-practice.com/elements/alert/alert#')
#     wait.until(element_to_be_clickable((By.CSS_SELECTOR, '.a-button'))).click()
#     wait.until(alert_is_present())
#     alert = Alert(driver)
#     assert alert.text == 'I am an alert!', f'Expected "I am an alert!", but got "{alert.text}"'
#     alert.accept()