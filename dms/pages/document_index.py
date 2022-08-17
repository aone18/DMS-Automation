from utils import select, insert, click,selectname
import time
from constants import url
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
name = "abcd"
name1 = "efgh"
field1 = "8"
field2 = "12"
def document_index(driver):
    time.sleep(2)
    driver.get(url+"/#/admin/indexType")
    time.sleep(2)
    select(driver, 'documentTypeId', "2")
    click(driver, '//*[@id="root"]/div[2]/div/main/div[2]/div/div[2]/div/div[1]/a')
    time.sleep(2)
    selectname(driver, 'dataType',"string")
    insert(driver,'//*[@id="root"]/div[2]/div/main/div[2]/div/form/div[1]/div/div[2]/div/input',name)
    insert(driver, '//*[@id="service"]',field1)
    insert(driver ,'//*[@id="serviceTwo"]',field2)
    click(driver, '//*[@id="root"]/div[2]/div/main/div[2]/div/form/div[2]/button')
    time.sleep(2)
    select(driver, 'documentTypeId', "2")
    click(driver, '//*[@id="root"]/div[2]/div/main/div[2]/div/div[2]/div/div[2]/div/table/tbody/tr[last()]/td[last()]/a/i')
    time.sleep(2)
    driver.find_element_by_name('label').clear()
    insert(driver,'//*[@id="root"]/div[2]/div/main/div[2]/div/form/div[1]/div/div[2]/div/input', name1)
    click(driver,'//*[@id="root"]/div[2]/div/main/div[2]/div/form/div[2]/button')
    time.sleep(2)
    click(driver,'//*[@id="root"]/div[2]/div/main/div[2]/div/div[2]/div/div[2]/div/table/tbody/tr[last()]/td[last()]/button/i')
    WebDriverWait(driver, 10).until(EC.alert_is_present())
    driver.switch_to.alert.accept()
