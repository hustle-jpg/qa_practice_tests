import pytest
from pages.alert_page import AlertPage

@pytest.mark.alert
def test_alert_appears(driver, wait):
    page = AlertPage(driver, wait)
    page.open()
    alert_text = page.trigger_alert_and_get_text()
    assert alert_text == 'I am an alert!', f'Expected "I am an alert!", but got "{alert_text}"'