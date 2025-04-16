import pytest
from pages.new_tab_page import NewTabPage


@pytest.mark.new_page
def test_open_new_page(driver, wait):
    page = NewTabPage(driver, wait)
    page.open()
    page.click_link_and_switch()
    actual_text = page.get_result_text()
    assert actual_text == 'I am a new page in a new tab', f'Expected "I am a new page in a new tab", but got "{actual_text}"'