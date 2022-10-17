from dms.utils import insert,select,click,sleep,clear
import time
from dms.constants import url
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
number = '3221231'
email = 'ram@rbb.com.np'
name = 'abcdef'
name1 = 'sabin11'
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
    select(driver, 'roleId', "1005")
    select(driver, 'hierarchy', "Branch_4")
    insert(driver, '//*[@id="password"]', new_password)
    insert(driver, '//*[@id="confirmPassword"]', confirm_password)
    click(driver,'//*[@id="signup-form"]/div[2]/button[2]')
    sleep(2)
    click(driver, '//*[@id="toExcelData"]/tbody/tr[last()]/td[last()]/div/a')
    sleep(2)
    clear(driver,'name')
    insert(driver, '//*[@id="name"]', name1)
    select(driver,'roleId', "1009")
    click(driver,'//*[@id="signup-form"]/div[2]/button[2]')
    time.sleep(2)
    WebDriverWait(driver, 10).until(EC.alert_is_present())
    driver.switch_to.alert.accept()
    sleep(2)
    click(driver,'//*[@id="toExcelData"]/tbody/tr[last()]/td[last()]/div/button/i')
    sleep(2)
    WebDriverWait(driver, 10).until(EC.alert_is_present())
    driver.switch_to.alert.accept()


