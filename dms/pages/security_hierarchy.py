from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from  utils import insert, select,selectname, click, sleep,dynamic_explicitly_click
from  constants import url
name = "aone"

def security_hierarchy(driver):
    sleep(2)
    driver.get(url+"/#/admin/hierarchy")
    sleep(2)
    click(driver,'//*[@id="root"]/div[2]/div/main/div[2]/div/div[2]/div/div[1]/a')
    sleep(2)
    dynamic_explicitly_click(driver, By.CSS_SELECTOR,'.select__value-container.select__value-container--is-multi.css-g1d714-ValueContainer')
    sleep(2)
    dynamic_explicitly_click(driver, By.CSS_SELECTOR, '.select__menu #react-select-8-option-1')
    select(driver, 'parentId', '13')
    click(driver, '//*[@id="root"]/div[2]/div/main/div[2]/div/form/div[2]/button[2]')
    sleep(2)
    click(driver,'//*[@id="root"]/div[2]/div/main/div[2]/div/div[2]/div/div[1]/a')
    sleep(2)
    select(driver, 'parentId', '39')
    select(driver, 'provinceUnit', 'Unit_')
    selectname(driver, 'department', '215')
    insert(driver, '//*[@id="name"]',name)
    click(driver, '//*[@id="root"]/div[2]/div/main/div[2]/div/form/div[2]/button[2]')
    sleep(20)


