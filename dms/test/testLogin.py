import pytest
from pages.login import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_valid_login(driver):
    loginT(driver, "admin@gentech.com", "admin123")
    get_url = driver.current_url
    assert str(get_url) == "http://192.168.1.109:3000/#/admin/dashboard", f"FAIL - Login Unsuccessful : test_valid_login"
    print("PASS - Login Successful : test_valid_login")
    logout(driver)

def test_invalid_login(driver):
    driver.implicitly_wait(10)
    loginT(driver, "admin1@gentech.com", "admin123")
    WebDriverWait(driver, 10).until(EC.alert_is_present())
    driver.switch_to.alert.accept()
    get_url = driver.current_url
    assert str(get_url) == "http://192.168.1.109:3000/#/admin/login", f"FAIL - Login Successful : test_invalid_login"
    print("PASS - Login Failed : test_invalid_login")
