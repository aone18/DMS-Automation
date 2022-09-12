from dms.utils import insert, click, select,sleep
from dms.constants import url
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from dms.pages.login import logout,login,checker_login
from dms.pages.checker import checker
name = 'automation testing'


def add_document(driver):
    sleep(2)
    driver.get(url+"/#/admin/documentList")

    # Click Add document
    sleep(2)
    click(driver, '//*[@id="root"]/div[2]/div/main/div[2]/div/div[2]/div/div[1]/a')

    # fill form
    sleep(2)
    select(driver, 'documentTypeId', "10")
    insert(driver, '//*[@id="otherTitle"]', name)
    select(driver, 'statusId', "1")
    select(driver, 'locationMapId', "3")
    select(driver, 'checker',"3")
    click(driver, '//*[@id="root"]/div[2]/div/main/div[2]/form/div/div[3]/button[2]')

    # upload document / file
    sleep(2)
    driver.execute_script("window.scrollTo(0, 1080)")   # scroll down
    insert(driver, '//*[@id="file"]',"C:/Users/bhumika/Pictures/dms dashboard.PNG")
    click(driver,'//*[@id="root"]/div[2]/div/main/div[2]/div/div[3]/div[1]/div[3]/button')

    # Click send to checker button
    click(driver, '//*[@id="caret"]')
    sleep(2)
    WebDriverWait(driver, 10).until(EC.alert_is_present())
    driver.switch_to.alert.accept()
    sleep(10)

    # logout and login with checker and approve the document
    logout(driver)
    sleep(2)
    checker_login(driver)
    sleep(2)
    checker(driver)
    sleep(10)
    logout(driver)

    # maker login
    sleep(2)
    login(driver)
    click(driver,'//*[@id="root"]/div[2]/div/div/div/ul/li[2]/a/i')
    click(driver, '//*[@id="root"]/div[2]/div/div/div/ul/li[2]/ul/li[1]/a')
    click(driver, '//*[@id="toExcel"]/tbody/tr[1]/td[4]/a')
    sleep(2)
    driver.execute_script("window.scrollTo(0, 1080)")
    insert(driver,'//*[@id="file"]',"C:/Users/bhumika/Pictures/dms dashboard - Copy.PNG")
    click(driver, '//*[@id="root"]/div[2]/div/main/div[2]/div/div[3]/div[1]/div[3]/button')
    select(driver, 'checker',"3")
    click(driver, '//*[@id="root"]/div[2]/div/main/div[2]/div/div[3]/div[1]/div[3]/form/div/div[2]/button')

    # popup: select okay
    sleep(2)
    WebDriverWait(driver, 10).until(EC.alert_is_present())
    driver.switch_to.alert.accept()
    sleep(10)
    logout(driver)
    sleep(2)
    checker_login(driver)
    sleep(2)
    checker(driver)

    sleep(10)



