from dms.utils import insert,click,sleep,click_name
from dms.constants import url
from dms.pages.add_branch import add_branch
from dms.pages.add_department import add_department
from dms.pages.add_user import add_user
from dms.pages.document_type import document_type
from dms.pages.document_index import document_index
from dms.pages.location_type import location_type
from dms.pages.location_maps import location_maps
from dms.pages.languages import languages
from dms.pages.add_document import add_document
from dms.pages.document_conditions import document_conditions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from dms.pages.security_hierarchy import security_hierarchy
name = 'maker1'
def role(driver):
    sleep(2)
    driver.get(url+"/#/admin/roles")
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
    add_user(driver)
    sleep(2)
    document_type(driver)
    sleep(2)
    document_index(driver)
    sleep(2)
    location_type(driver)
    sleep(2)
    location_maps(driver)
    sleep(2)
    languages(driver)
    sleep(2)
    document_conditions(driver)
    sleep(5)
    add_document(driver)
    sleep(10)


