from utils import insert, click, select
import time
from constants import url
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
father_name = 'abcd'
acc_number = '9842376644'
grandfather = 'efgh'
name = 'automation testing'


def add_document(driver):
    time.sleep(2)
    driver.get(url+"/#/admin/documentList")
    time.sleep(2)
    click(driver, '//*[@id="root"]/div[2]/div/main/div[2]/div/div[2]/div/div[1]/a')
    time.sleep(2)
    select(driver, 'documentTypeId', "3")
    insert(driver, '//*[@id="root"]/div[2]/div/main/div[2]/form/div/div[2]/div[2]/div[1]/div/input[1]',father_name)
    insert(driver, '//*[@id="root"]/div[2]/div/main/div[2]/form/div/div[2]/div[2]/div[2]/div/input[1]',grandfather)
    insert(driver, '//*[@id="root"]/div[2]/div/main/div[2]/form/div/div[2]/div[2]/div[3]/div/input[1]',acc_number)
    insert(driver, '//*[@id="otherTitle"]', name)
    select(driver, 'locationMapId', "3")
    select(driver, 'checker', "3")
    click(driver, '//*[@id="root"]/div[2]/div/main/div[2]/form/div/div[3]/button[2]')
    time.sleep(2)
    driver.execute_script("window.scrollTo(0, 1080)")
    insert(driver, '//*[@id="file"]',"C:/Users/DELL/Downloads/download.jpg")
    click(driver, '//*[@id="root"]/div[2]/div/main/div[2]/div/div[3]/div[1]/div[3]/button[2]')
    time.sleep(2)
    click(driver,'//*[@id="caret"]')
    WebDriverWait(driver, 10).until(EC.alert_is_present())
    driver.switch_to.alert.accept()
