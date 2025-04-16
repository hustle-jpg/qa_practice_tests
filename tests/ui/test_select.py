import pytest
from pages.dropdown_page import DropdownPage


@pytest.mark.select
def test_select_programming_language(driver, wait):
    page = DropdownPage(driver, wait)
    page.open()
    selected_text = page.select_language('Python')
    assert selected_text == 'Python', f'Expected "Python", but got "{selected_text}"'