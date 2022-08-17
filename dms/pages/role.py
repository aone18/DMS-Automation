from utils import insert,click,sleep
import time
from constants import url

name = 'maker'
def role(driver):
    sleep(2)
    driver.get(url + "/#/admin/roles/add")
    sleep(2)

    insert(driver, "//*[@id='name']",name)

    click(driver,'//*[@id="2"]')