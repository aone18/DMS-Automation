from constants import url
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from  pages.add_branch import add_branch
from  pages.add_department import add_department
from  pages.add_user import add_user
from  pages.document_type import document_type
from  pages.document_index import document_index
from  pages.location_type import location_type
from  pages.location_maps import location_maps
from  pages.languages import languages
from  pages.add_document import add_document
from  pages.document_conditions import document_conditions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from  pages.security_hierarchy import security_hierarchy
from pages.login import login
from pages.role import role
from pages.api.login import login_api
from pages.testUser import test_user_creation_by_name, test_user_update_by_name, test_user_delete_by_name

# from pages.edit_document import edit_document
# used chrome driver

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get(url)



# full screen
driver.maximize_window()
# login path
login(driver)
#login_api(driver)




# checker login
# checker_login(driver)
# logout(driver)
# checker path
# checker(driver)
# add_document(driver)
# add user path
test_user_creation_by_name(driver)
test_user_update_by_name(driver)
test_user_delete_by_name(driver)
#add_user(driver)
# add_department path
# add_department(driver)
# add branches path
#add_branch(driver)
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
#role(driver)

# add security hierarchy path
# security_hierarchy(driver)