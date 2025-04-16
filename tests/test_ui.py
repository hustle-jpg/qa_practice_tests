# from pages.button_page import ButtonPage
# from pages.checkbox_page import CheckBoxPage
# from pages.dropdown_page import DropdownPage
# from pages.new_tab_page import NewTabPage
# from pages.alert_page import AlertPage
#
#
# def test_click_button(driver, wait):
#     page = ButtonPage(driver, wait)
#     page.open()
#     page.click_button()
#     actual_text = page.get_result_text()
#     assert actual_text == 'Submitted', f'Expected "Submitted", but got "{actual_text}"'
#
# def test_checkbox(driver, wait):
#     page = CheckBoxPage(driver, wait)
#     page.open()
#     page.click_checkbox()
#     page.click_button()
#     actual_text = page.get_result_text()
#     assert actual_text == 'select me or not', f'Expected "select me or not", but got "{actual_text}"'
#
# def test_select_programming_language(driver, wait):
#     page = DropdownPage(driver, wait)
#     page.open()
#     selected_text = page.select_language('Python')
#     assert selected_text == 'Python', f'Expected "Python", but got "{selected_text}"'
#
#
# def test_open_new_page(driver, wait):
#     page = NewTabPage(driver, wait)
#     page.open()
#     page.click_link_and_switch()
#     actual_text = page.get_result_text()
#     assert actual_text == 'I am a new page in a new tab', f'Expected "I am a new page in a new tab", but got "{actual_text}"'
#
#
# def test_alert_appears(driver, wait):
#     page = AlertPage(driver, wait)
#     page.open()
#     alert_text = page.trigger_alert_and_get_text()
#     assert alert_text == 'I am an alert!', f'Expected "I am an alert!", but got "{alert_text}"'
