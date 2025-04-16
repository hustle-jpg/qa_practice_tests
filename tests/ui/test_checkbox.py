import pytest
from pages.checkbox_page import CheckBoxPage


@pytest.mark.checkbox
def test_checkbox(driver, wait):
    page = CheckBoxPage(driver, wait)
    page.open()
    page.click_checkbox()
    page.click_button()
    actual_text = page.get_result_text()
    assert actual_text == 'select me or not', f'Expected "select me or not", but got "{actual_text}"'