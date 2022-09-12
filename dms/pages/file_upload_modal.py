from dms.utils import insert, click, select
import time
from dms.constants import url

def file_upload_modal(driver):
    time.sleep(2)

    driver.get(url+"/#/admin/view?i=KvZaAJzVG3")

    time.sleep(2)

    driver.execute_script("window.scrollTo(0, 1080)")   # scroll down

    # Open upload modal
    click(driver, "//*[@id='root']/div[2]/div/main/div[2]/div/div[3]/div[1]/div[3]/button")

    time.sleep(2)
    # select document type
    select(driver, 'documentTypeId', "39")
    # add file
    insert(driver, "//*[@id='file']", "C:/Users/DELL/Downloads/download.jpg")
    # upload file
    click(driver, "/html/body/div[3]/div/div[1]/div/div/div[2]/div/form/div[2]/button[1]")