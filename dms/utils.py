from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def insert(driver, xpath, value):
    driver.find_element(By.XPATH, xpath).send_keys(value)

def insertname(driver,name, value):
    driver.find_element(By.NAME, name).send_keys(value)

def click(driver, xpath):
    driver.find_element(By.XPATH, xpath).click()

def explicitly_click(driver, xpath,time=10):
    element = WebDriverWait(driver, time).until(
        EC.presence_of_element_located((By.XPATH, xpath))
    )
    element.click()

def select(driver,name,value):
    select = Select(driver.find_element(By.ID,name))
    select.select_by_value(value)

def selectname(driver,name,value):
    select = Select(driver.find_element(By.NAME,name))
    select.select_by_value(value)

def clear(driver,name):
    driver.find_element(By.NAME,name).clear()

def sleep(value):
    time.sleep(value)

def implicitly_wait(driver,value):
    driver.implicitly_wait(value)