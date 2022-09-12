from utils import insert,select,click
import time
from constants import url
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
number = '3221'
email = 'abcd@rbb.com.np'
name = 'abcdef'
name1 = 'sabin'
new_password = 'Aone@123'
confirm_password = 'Aone@123'
def add_user(driver):
    time.sleep(2)
    driver.get(url+"/#/admin/users")
    time.sleep(2)
    click(driver, '//*[@id="root"]/div[2]/div/main/div[2]/div/div[2]/div/div[1]/a')
    time.sleep(2)
    insert(driver, '//*[@id="identityNo"]', number)
    insert(driver, '//*[@id="email"]', email)
    insert(driver, '//*[@id="name"]', name)
    select(driver, '//*[@id="roleId"]', "1")
    select(driver, '//*[@id="hierarchy"]', "Branch_2")
    insert(driver, '//*[@id="password"]', new_password)
    insert(driver, '//*[@id="confirmPassword"]', confirm_password)
    click(driver,'//*[@id="signup-form"]/div[2]/button[2]')
    time.sleep(2)
    driver.execute_script("window.scrollTo(0, 1080)")
    click(driver,'//*[@id="root"]/div[2]/div/main/div[2]/div/div[2]/div/div[2]/div[3]/div[1]/nav/ul/li[last()]/button')
    time.sleep(2)
    click(driver, '//*[@id="toExcelData"]/tbody/tr[last()]/td[last()]/div/a/i')
    time.sleep(2)
    driver.find_element_by_id('name').clear()
    insert(driver, '//*[@id="name"]', name1)
    select(driver,'roleId', "4")
    click(driver,'//*[@id="signup-form"]/div[2]/button[2]')
    time.sleep(2)
    WebDriverWait(driver, 10).until(EC.alert_is_present())
    driver.switch_to.alert.accept()
    time.sleep(2)
    driver.execute_script("window.scrollTo(0, 1080)")
    click(driver,'//*[@id="root"]/div[2]/div/main/div[2]/div/div[2]/div/div[2]/div[3]/div[1]/nav/ul/li[last()]/button')
    click(driver,'//*[@id="toExcelData"]/tbody/tr[last()]/td[last()]/div/button/i')
    WebDriverWait(driver, 10).until(EC.alert_is_present())
    driver.switch_to.alert.accept()


