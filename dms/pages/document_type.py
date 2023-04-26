from utils import insert,click,select,sleep
import time
from constants import url
name = "wxyz12"
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def document_type(driver):
    sleep(2)
    driver.get(url+"/#/documentTypes")
    sleep(2)
    click(driver, '//*[@id="root"]/div[2]/div/main/div[2]/div/div[2]/div/div[1]/a')
    sleep(2)
    insert(driver, '//*[@id="name"]', name)
    select(driver, 'parentId',"3")
    click(driver, '//*[@id="root"]/div[2]/div/main/div[2]/div/form/div[2]/button[2]')
    time.sleep(2)
    # click(driver, '//*[@id="cursor-pointer"]/span')
    click(driver,'//*[@id="root"]/div[2]/div/main/div[2]/div/div[2]/div/div[2]/div/table/tbody/tr[last()]/td[last()]/button')
    sleep(2)
    WebDriverWait(driver, 10).until(EC.alert_is_present())
    driver.switch_to.alert.accept()


