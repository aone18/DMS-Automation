from dms.utils import click, insert
from time import sleep

email_key = "aone@rbb.com.np"
password_key = "Aone@1234"
email = "sagar@rbb.com.np"
password = "Aone@1234"


def login(driver):
    insert(driver, "//*[@id='signin-form']/div[1]/input", email_key)
    insert(driver, "//*[@id='signin-form']/div[2]/input", password_key)

    click(driver, "//*[@id='signin-form']/div[3]/div/button")

def logout(driver):
    driver.implicitly_wait(20)
    click(driver, '//*[@id="root"]/div[2]/header/ul/li/a/span/i')
    driver.implicitly_wait(20)
    click(driver, '//*[@id="root"]/div[2]/header/ul/li/div/button[2]')



def checker_login(driver):

    insert(driver, "//*[@id='signin-form']/div[1]/input", email)
    insert(driver, "//*[@id='signin-form']/div[2]/input", password)

    click(driver, "//*[@id='signin-form']/div[3]/div/button")