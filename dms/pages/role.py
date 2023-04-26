from utils import insert,click,sleep,click_name
from constants import url
from pages.add_branch import add_branch
from pages.add_department import add_department
from pages.add_user import add_user
from pages.document_type import document_type
from pages.document_index import document_index
from pages.location_type import location_type
from pages.location_maps import location_maps
from pages.languages import languages
from pages.add_document import add_document
from pages.document_conditions import document_conditions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.security_hierarchy import security_hierarchy
name = 'maker1'
def role(driver):
    sleep(2)
    driver.get(url+"/#/roles")
    sleep(2)
    click(driver, '//*[@id="root"]/div[2]/div/main/div[2]/div/div[1]/a')
    sleep(2)
    insert(driver, '//*[@id="name"]', name)
    click_name(driver, 'control-6')
    driver.execute_script("window.scrollTo(0, 1080)")
    click(driver, '//*[@id="root"]/div[2]/div/main/div[2]/div/form/div[3]/button[2]')
    sleep(2)
    click(driver, '//*[@id="toExcelData"]/tbody/tr[last()]/td[last()]/div/button/i')
    sleep(2)
    WebDriverWait(driver, 10).until(EC.alert_is_present())
    driver.switch_to.alert.accept()
    add_branch(driver)
    sleep(2)
    add_department(driver)
    sleep(2)
   # add_user(driver)
    sleep(2)
   # document_type(driver)
    sleep(2)
    #document_index(driver)
    sleep(2)
    #location_type(driver)
    sleep(2)
    #location_maps(driver)
    sleep(2)
    #languages(driver)
    sleep(2)
    #document_conditions(driver)
    sleep(10)
    # add_document(driver)


