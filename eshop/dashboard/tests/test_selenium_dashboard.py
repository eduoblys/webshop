import pytest
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

@pytest.mark.selenium
def test_dashboard_admin_login(live_server, chrome_browser_instance):
    browser = chrome_browser_instance
    browser.get(("%s%s" % (live_server.url, "/admin/login/")))

    user_name = browser.find_element(By.NAME, "username")
    user_password = browser.find_element(By.NAME, "password")
    submit = browser.find_element(By.XPATH, "/html/body/div/div[2]/div/div[1]/div/form/div[3]/input")

    user_name.send_keys("admin")
    user_password.send_keys("password")
    submit.send.keys(Keys.RETURN)

    assert "Site administration" in browser.page_source