from  utils import select, insert, click,selectname,clear,sleep
import time
from  constants import url
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
name = "aone"
name1 = "efgh"

def document_index(driver):
    time.sleep(2)
    driver.get(url+"/#/indexType")
    time.sleep(2)
    select(driver, 'documentTypeId', "3")
    click(driver, '//*[@id="root"]/div[2]/div/main/div[2]/div/div[2]/div/div[1]/a')
    time.sleep(2)
    selectname(driver, 'dataType',"string")
    insert(driver,'//*[@id="root"]/div[2]/div/main/div[2]/div/form/div[1]/div/div[2]/div/input',name)
    click(driver, '//*[@id="root"]/div[2]/div/main/div[2]/div/form/div[2]/button')
    sleep(2)
    select(driver, 'documentTypeId', "3")
    click(driver, '//*[@id="root"]/div[2]/div/main/div[2]/div/div[2]/div/div[2]/div/table/tbody/tr[last()]/td[last()]/button')
    sleep(2)
    WebDriverWait(driver, 10).until(EC.alert_is_present())
    driver.switch_to.alert.accept()
