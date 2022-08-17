from utils import insert, select,click
import time
from constants import url
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

name= 'baneshwor branch'
name1= 'baluwatar branch'
def location_maps(driver):
    time.sleep(2)
    driver.get(url+"/#/admin/locationMaps")
    time.sleep(2)
    click(driver,'//*[@id="root"]/div[2]/div/main/div[2]/div/div[2]/div/div[1]/a')

    time.sleep(2)
    insert(driver,'//*[@id="name"]',name)
    select(driver,'locationTypeId',"3")
    click(driver,'//*[@id="root"]/div[2]/div/main/div[2]/div/form/div[2]/button[2]')
    time.sleep(2)
    click(driver,'//*[@id="root"]/div[2]/div/main/div[2]/div/div[2]/div/div[2]/div[2]/table/tbody/tr[last()]/td[last()]/div/a/i')
    time.sleep(2)
    driver.find_element_by_id('name').clear()
    insert(driver,'//*[@id="name"]',name1)
    select(driver, 'locationTypeId', "2")
    click(driver, '//*[@id="root"]/div[2]/div/main/div[2]/div/form/div[2]/button[2]')
    time.sleep(2)
    click(driver, '//*[@id="root"]/div[2]/div/main/div[2]/div/div[2]/div/div[2]/div[2]/table/tbody/tr[last()]/td[last()]/div/button/i')
    WebDriverWait(driver, 10).until(EC.alert_is_present())
    driver.switch_to.alert.accept()