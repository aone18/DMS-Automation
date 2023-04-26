from  utils import insert, click,clear
import time
from  constants import url
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


name = 'aone'
address = 'kritipur'
code = '21'
name1 = 'aonesen'


def add_branch(driver):
    time.sleep(2)
    driver.get(url + "/#/branches")
    time.sleep(2)
    click(driver, '//*[@id="root"]/div[2]/div/main/div[2]/div/div[1]/a')
    time.sleep(2)
    insert(driver, '//*[@id="name"]', name)
    insert(driver, '//*[@id="street"]', address)
    insert(driver, '//*[@id="branchCode"]', code)
    click(driver, '//*[@id="root"]/div[2]/div/main/div[2]/div/form/div[2]/button[2]')
    time.sleep(2)
    driver.execute_script("window.scrollTo(0, 1080)")
    click(driver, '//*[@id="root"]/div[2]/div/main/div[2]/div/div[3]/div[3]/div[1]/nav/ul/li[8]/button')
    time.sleep(2)
    click(driver, '//*[@id="toExcelData"]/tbody/tr[last()]/td[last()]/div/a/i')
    time.sleep(2)
    clear(driver, 'name')
    insert(driver, '//*[@id="name"]', name1)
    click(driver, '//*[@id="root"]/div[2]/div/main/div[2]/div/form/div[2]/button[2]')
    time.sleep(2)
    WebDriverWait(driver, 10).until(EC.alert_is_present())
    driver.switch_to.alert.accept()
    time.sleep(2)
    driver.execute_script("window.scrollTo(0, 1080)")
    click(driver, '//*[@id="root"]/div[2]/div/main/div[2]/div/div[3]/div[3]/div[1]/nav/ul/li[8]/button')
    time.sleep(2)
    click(driver, '//*[@id="toExcelData"]/tbody/tr[last()]/td[last()]/div/button/i')
    time.sleep(2)
    WebDriverWait(driver, 10).until(EC.alert_is_present())
    driver.switch_to.alert.accept()
