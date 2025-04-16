import pytest
from pages.button_page import ButtonPage


@pytest.mark.button
def test_click_button(driver, wait):
    page = ButtonPage(driver, wait)
    page.open()
    page.click_button()
    actual_text = page.get_result_text()
    assert actual_text == 'Submitted', f'Expected "Submitted", but got "{actual_text}"'