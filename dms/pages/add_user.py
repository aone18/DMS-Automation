from utils import insert, select, click, sleep, clear
import time
from  constants import url
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
number = 'qa 5'
email = 'qa5@rbb.com.np'
name = 'qa 5'
nameUpdated = 'qa 5 upt'
new_password = 'Admin@123'
confirm_password = 'Admin@123'
def add_user(driver):
    time.sleep(2)
    driver.get(url+"/#/admin/users")
    time.sleep(2)
    click(driver, '//*[@id="root"]/div[2]/div/main/div[2]/div/div[2]/div/div[1]/a')
    time.sleep(2)
    insert(driver, '//*[@id="identityNo"]', number)
    insert(driver, '//*[@id="email"]', email)
    insert(driver, '//*[@id="name"]', name)
    select(driver, 'roleId', "3")
    select(driver, 'hierarchy', "Branch_107")
    insert(driver, '//*[@id="password"]', new_password)
    insert(driver, '//*[@id="confirmPassword"]', confirm_password)
    click(driver,'//*[@id="signup-form"]/div[2]/button[2]')
    sleep(2)

def update_user(driver):
    click(driver, "//i[@class='fa fa-pencil']")
    sleep(2)
    clear(driver,'name')
    insert(driver, '//*[@id="name"]', nameUpdated)
    select(driver,'roleId', "4")
    click(driver,'//*[@id="signup-form"]/div[2]/button[2]')
    time.sleep(2)
    WebDriverWait(driver, 10).until(EC.alert_is_present())
    driver.switch_to.alert.accept()

def delete_user(driver):
    sleep(2)
    click(driver,"//i[@class='fas fa-trash']")
    sleep(2)
    WebDriverWait(driver, 10).until(EC.alert_is_present())
    driver.switch_to.alert.accept()


