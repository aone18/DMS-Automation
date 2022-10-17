from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from pages.add_document import add_document
from pages.file_upload_modal import file_upload_modal
from pages.login import login, logout
from pages.role import role
from pages.security_hierarchy import security_hierarchy
from pages.checker import checker
from pages.checker_login import checker_login
from pages.add_user import add_user
from pages.add_department import add_department
from dms.pages.add_branch import add_branch
from pages.document_type import document_type
from pages.document_index import document_index
from navigate import navigate_sidebar
from pages.location_maps import location_maps
from pages.location_type import location_type
from pages.languages import languages
from pages.document_conditions import document_conditions
from dms.constants import url, driver_url
#from pages.edit_document import edit_document
# used chrome driver
from utils import setCookieForLogin

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get(url+"/#/admin/hierarchy/add")



# full screen
driver.maximize_window()
# login path
# login(driver)
setCookieForLogin(driver)

# checker login
# checker_login(driver)
# logout(driver)
# checker path
# checker(driver)
# add_document(driver)
# add user path
# add_user(driver)
# add_department path
# add_department(driver)
# add branches path
# add_branch(driver)
# document type path
# document_type(driver)
# document_index path
# document_index(driver)
# location type path
# location_type(driver)
# location map path
# location_maps(driver)
# languages path
# languages(driver)



# add document conditions path
# document_conditions(driver)

# edit document path
# edit_document(driver)

# upload file path
# file_upload_modal(driver)

# add document form
# add_document(driver)

# add role path
role(driver)

# add security hierarchy path
# security_hierarchy(driver)