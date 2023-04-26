from utils import click, select
import time
from constants import url
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
def edit_document(driver):
    time.sleep(2)
    driver.get(url+"/#/edit?i=QDmz20XdO3")
    time.sleep(2)
    select(driver, 'securityLevel', "3")

    click(driver, "//*[@id='root']/div[2]/div/main/div[2]/div/form/div[2]/div[6]/button")
    WebDriverWait(driver, 10).until(EC.alert_is_present())
    driver.switch_to.alert.accept()

