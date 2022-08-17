from utils import insert,click
import time
from constants import url
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
name= 'aone'
name1= "aone sen"
def add_department(driver):
    time.sleep(2)
    driver.get(url+"/#/admin/departments")
    time.sleep(2)
    click(driver, '//*[@id="root"]/div[2]/div/main/div[2]/div/div[2]/div/div[1]/a')
    time.sleep(2)
    insert(driver, '//*[@id="name"]', name)
    click(driver, '//*[@id="root"]/div[2]/div/main/div[2]/div/form/div[2]/button[2]')
    time.sleep(2)
    click(driver, '//*[@id="root"]/div[2]/div/main/div[2]/div/div[2]/div/div[2]/div/table/tbody/tr[last()]/td[last()]/a/i')
    time.sleep(2)
    driver.find_element_by_id('name').clear()
    insert(driver, '//*[@id="name"]',name1)
    click(driver, '//*[@id="root"]/div[2]/div/main/div[2]/div/form/div[2]/button[2]')
    time.sleep(2)
    click(driver, '//*[@id="root"]/div[2]/div/main/div[2]/div/div[2]/div/div[2]/div/table/tbody/tr[last()]/td[last()]/button/i')
    time.sleep(2)
    WebDriverWait(driver, 10).until(EC.alert_is_present())
    driver.switch_to.alert.accept()

