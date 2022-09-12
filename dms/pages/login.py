from dms.utils import click, insert

email_key = "admin@gentech.com"
password_key = "admin123"


def login(driver):
    insert(driver, "//*[@id='signin-form']/div[1]/input", email_key)
    insert(driver, "//*[@id='signin-form']/div[2]/input", password_key)

    click(driver, "//*[@id='signin-form']/div[3]/div/button")

