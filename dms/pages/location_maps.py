from  utils import insert, select,click,clear,sleep
import time
from  constants import url
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

name= 'baluwatar branch'

def location_maps(driver):
    time.sleep(2)
    driver.get(url+"/#/locationMaps")
    time.sleep(2)
    click(driver, '//*[@id="root"]/div[2]/div/main/div[2]/div/div[2]/div/div[1]/a')
    sleep(2)
    insert(driver, '//*[@id="name"]', name)
    select(driver, 'locationTypeId', '2')
    click(driver,'//*[@id="root"]/div[2]/div/main/div[2]/div/form/div[2]/button[2]')


