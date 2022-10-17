from dms.utils import insert,select,click,clear,sleep
import time
from dms.constants import url
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
name = 'abc'
code = '012'
name1 = 'xyz'
code1 ='067'
def languages(driver):
    time.sleep(2)
    driver.get(url+"/#/admin/languages")
    time.sleep(2)
    click(driver,'//*[@id="root"]/div[2]/div/main/div[2]/div/div[1]/a')
    time.sleep(2)
    insert(driver, '//*[@id="name"]', name)
    insert(driver, '//*[@id="code"]', code)
    click(driver, "//*[@id='root']/div[2]/div/main/div[2]/div/form/div[2]/button[2]")
    sleep(2)
    click(driver,'//*[@id="root"]/div[2]/div/main/div[2]/div/div[2]/div/table/tbody/tr[last()]/td[last()]/a/i')
    clear(driver, 'name')
    insert(driver,'//*[@id="name"]', name1)
    clear(driver, 'code')
    insert(driver,'//*[@id="code"]',code1)
    click(driver, "//*[@id='root']/div[2]/div/main/div[2]/div/form/div[2]/button[2]")
    time.sleep(2)
    click(driver,'//*[@id="root"]/div[2]/div/main/div[2]/div/div[2]/div/table/tbody/tr[last()]/td[last()]/button/i')
    WebDriverWait(driver, 10).until(EC.alert_is_present())
    driver.switch_to.alert.accept()