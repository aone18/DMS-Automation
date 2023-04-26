from constants import url
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from pages.login import login
from dms.test.testUser import test_user_creation_by_name, test_user_update_by_name, test_user_delete_by_name
from pages.role import role

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
role(driver)

# add security hierarchy path
# security_hierarchy(driver)


###---TEST CASES---###

# test_user_creation_by_name(driver)
# test_user_update_by_name(driver)
# test_user_delete_by_name(driver)