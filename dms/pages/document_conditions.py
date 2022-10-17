from dms.utils import insert,click,clear,sleep
import time
from dms.constants  import url
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
condition= 'abcdef'
condition1='wxyz'
def document_conditions(driver):
    time.sleep(2)
    driver.get(url+"/#/admin/document-conditions")
    time.sleep(2)
    click(driver,'//*[@id="root"]/div[2]/div/main/div[2]/div/div[1]/a')
    time.sleep(2)
    insert(driver,'//*[@id="name"]',condition)
    click(driver,"//*[@id='root']/div[2]/div/main/div[2]/div/form/div[2]/button[2]")
    sleep(2)
    click(driver, '//*[@id="root"]/div[2]/div/main/div[2]/div/div[2]/div/table/tbody/tr[last()]/td[last()]/a/i')
    clear(driver, 'name')
    insert(driver,'//*[@id="name"]',condition1 )
    click(driver,"//*[@id='root']/div[2]/div/main/div[2]/div/form/div[2]/button[2]")
    time.sleep(2)
    click(driver,"//*[@id='root']/div[2]/div/main/div[2]/div/div[2]/div/table/tbody/tr[last()]/td[last()]/button/i")
    time.sleep(2)
    WebDriverWait(driver, 10).until(EC.alert_is_present())
    driver.switch_to.alert.accept()
