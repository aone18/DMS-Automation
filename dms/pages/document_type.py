from utils import selectname,insert,click,select
import time
from constants import url
name = "abcd"

def document_type(driver):
    time.sleep(2)
    driver.get(url+"/#/admin/documentTypes")
    time.sleep(2)
    click(driver, '//*[@id="root"]/div[2]/div/main/div[2]/div/div[2]/div/div[1]/a')
    time.sleep(2)
    insert(driver, '//*[@id="name"]', name)
    select(driver, 'parentId',"5")
    click(driver, '//*[@id="root"]/div[2]/div/main/div[2]/div/form/div[2]/button[2]')
    time.sleep(2)
    click(driver, '/html/body/div[2]/div[2]/div/main/div[2]/div/div[2]/div/div[2]/div/table/tbody/tr[last()]/td[last()]/a/i')
    time.sleep(2)
    cl
