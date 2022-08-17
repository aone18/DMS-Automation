from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

# hover and click navigation
def navigate_sidebar(driver, nav_parent, nav_child):
    # loginng time for page
    time.sleep(5)

    hover_element = driver.find_element(By.XPATH, nav_parent)
    action = ActionChains(driver)
    action.move_to_element(hover_element).perform()
    driver.find_element(By.XPATH, nav_child).click()