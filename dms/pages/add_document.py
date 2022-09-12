from dms.utils import insert, click, select,sleep
import time
from dms.constants import url
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
name = 'abcd'



def add_document(driver):
    sleep(2)
    driver.get(url+"/#/admin/documentList")
    sleep(2)
    click(driver, '//*[@id="root"]/div[2]/div/main/div[2]/div/div[2]/div/div[1]/a')
    sleep(2)
    select(driver, 'documentTypeId', "10")
    insert(driver, '//*[@id="otherTitle"]', name)


