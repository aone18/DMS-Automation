from pages.add_user import add_user, number, name, update_user, nameUpdated, delete_user
from utils import insert, select, click, sleep, clear, userNameCheck
import time
from constants import url
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_user_creation_by_name(driver):
    add_user(driver)
    driver.get(url + "/#/admin/users")
    time.sleep(2)
    driver.implicitly_wait(10)
    insert(driver, "//input[@placeholder='Search by name column']", name)
    time.sleep(2)
    driver.implicitly_wait(2)
    user_name = userNameCheck(driver,'//*[@id="toExcelData"]/tbody/tr/td[3]')
    assert user_name is not None, "User name element not found"
    assert user_name.text == name, f"User name not found: {user_name.text}"
    print(f"User Created Successfully: {user_name.text}")

def test_user_update_by_name(driver):
    driver.get(url + "/#/admin/users")
    time.sleep(2)
    driver.implicitly_wait(2)
    insert(driver, "//input[@placeholder='Search by name column']", name)
    time.sleep(2)
    update_user(driver)
    time.sleep(5)
    insert(driver, "//input[@placeholder='Search by name column']", nameUpdated)
    time.sleep(5)
    user_name_updated = userNameCheck(driver,'//*[@id="toExcelData"]/tbody/tr/td[3]')
    assert user_name_updated is not None, "User name element not found"
    assert user_name_updated.text == nameUpdated, f"User name not found: {user_name_updated.text}"
    print(f"User Name Updated Successfully: {user_name_updated.text}")

def test_user_delete_by_name(driver):
    driver.get(url + "/#/admin/users")
    time.sleep(2)
    driver.implicitly_wait(2)
    insert(driver, "//input[@placeholder='Search by name column']", nameUpdated)
    time.sleep(2)
    delete_user(driver)
    time.sleep(2)
    insert(driver, "//input[@placeholder='Search by name column']", nameUpdated)
    time.sleep(2)
    driver.implicitly_wait(2)
    user_name_updated = userNameCheck(driver, '//*[@id="toExcelData"]/tbody/tr/td[3]')
    assert user_name_updated is not None, "User name element found"
    assert user_name_updated.text == nameUpdated, f"User Deletion Unsuccessful: {user_name_updated.text}"
    print(f"User Deleted Successfully: {user_name_updated.text}")