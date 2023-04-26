from  utils import insert, click,sleep,clear
from  constants import url
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
name= 'abcd'
name1= 'efgh'

def location_type(driver):
    sleep(2)
    driver.get(url+"/#/locationTypes")
    sleep(2)
    click(driver,'//*[@id="root"]/div[2]/div/main/div[2]/div/div[1]/a')
    sleep(2)
    insert(driver,'//*[@id="name"]',name)
    click(driver,'//*[@id="root"]/div[2]/div/main/div[2]/div/form/div[2]/button[2]')
    sleep(2)
    click(driver,'//*[@id="root"]/div[2]/div/main/div[2]/div/div[2]/div[2]/table/tbody/tr[last()]/td[last()]/div/a/i')
    sleep(2)
    clear(driver, 'name')
    insert(driver,'//*[@id="name"]',name1)
    click(driver,'//*[@id="root"]/div[2]/div/main/div[2]/div/form/div[2]/button[2]')
    sleep(4)
    click(driver,'//*[@id="toExcelData"]/tbody/tr[last()]/td[last()]/div/button/i')
    WebDriverWait(driver, 10).until(EC.alert_is_present())
    driver.switch_to.alert.accept()