from  utils import click, insert
from time import sleep

email_key = "admin@gentech.com"
password_key = "admin123"
email = "sagar@rbb.com.np"
password = "Aone@1234"


def login(driver):
    insert(driver, "//*[@id='signin-form']/div[1]/input", email_key)
    insert(driver, "//*[@id='signin-form']/div[2]/input", password_key)

    click(driver, "//*[@id='signin-form']/div[3]/div/button")

def loginT(driver,loginEmail, loginPassword):
    insert(driver, "//*[@id='signin-form']/div[1]/input", loginEmail)
    insert(driver, "//*[@id='signin-form']/div[2]/input", loginPassword)
    click(driver, "//*[@id='signin-form']/div[3]/div/button")
    sleep(2)

def logout(driver):
    driver.implicitly_wait(10)
    click(driver, "//i[@class='fas fa-user-circle fa-2x']")
    driver.implicitly_wait(10)
    click(driver, "//i[@class='fas fa-sign-out-alt']")



def checker_login(driver):

    insert(driver, "//*[@id='signin-form']/div[1]/input", email)
    insert(driver, "//*[@id='signin-form']/div[2]/input", password)

    click(driver, "//*[@id='signin-form']/div[3]/div/button")