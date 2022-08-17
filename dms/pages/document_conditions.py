from utils import insert,click
import time
from constants  import url
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
condition= 'very good'
condition1='bhumika didi'
def document_conditions(driver):
    time.sleep(2)
    driver.get(url+"/#/admin/document-conditions")
    time.sleep(2)
    click(driver,'//*[@id="root"]/div[2]/div/main/div[2]/div/div[1]/a')
    time.sleep(2)
    insert(driver,'//*[@id="name"]',condition)
    click(driver,"//*[@id='root']/div[2]/div/main/div[2]/div/form/div[2]/button[2]")
    time.sleep(5)
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH,"//*[@id='root']/div[2]/div/main/div[2]/div/div[2]/div/table/tbody/tr[4]/td[6]/a/i"))).click()
    time.sleep(5)
    driver.find_element_by_id('name').clear()
    time.sleep(2)
    insert(driver,'//*[@id="name"]',condition1 )
    click(driver,"//*[@id='root']/div[2]/div/main/div[2]/div/form/div[2]/button[2]")
    time.sleep(2)
    click(driver,"//*[@id='root']/div[2]/div/main/div[2]/div/div[2]/div/table/tbody/tr[3]/td[6]/button/i")
    time.sleep(2)
    WebDriverWait(driver, 10).until(EC.alert_is_present())
    driver.switch_to.alert.accept()
