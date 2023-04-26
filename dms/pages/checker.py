from  utils import click, sleep
from  constants import url
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def checker(driver):
    sleep(2)
    driver.get(url+"/#/pending")
    sleep(2)
    click(driver, "//*[@id='toExcel']/tbody/tr[1]/td[4]/a")
    sleep(2)
    click(driver, '//*[@id="root"]/div[2]/div/main/div[2]/div/div[1]/div[1]/div[2]/div/div/button[1]/i')
    WebDriverWait(driver, 10).until(EC.alert_is_present())
    driver.switch_to.alert.accept()



