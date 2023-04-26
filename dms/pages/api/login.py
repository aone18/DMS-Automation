import requests
from utils import sleep
from utils import setCookie

def login_api(driver):
    payload = {'email': 'admin@gentech.com', 'password': 'admin123'}
    url = 'https://0f2a-2400-1a00-b040-a50c-c17c-798d-be3b-a602.in.ngrok.io/api/signin'
    response = requests.post(url, data=payload)
    sleep(2)
    json_response = response.json()
    # setCookie(driver,'jwt',json_response['user']['token'])
    token ='eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MSwiZW1haWwiOiJhZG1pbkBnZW50ZWNoLmNvbSIsInJvbGVJZCI6MSwiaGllcmFyY2h5IjoiU3VwZXItMDAxIiwiYnJhbmNoSWQiOjEsImRlcGFydG1lbnRJZCI6MSwiZXhwIjoxNjcyMDY1MDk0LCJpYXQiOjE2NzIwNDcwOTR9.e6JyOV1HAb8r-eXpgb6JkioTgJ4MmLW8ryBVCwwfQP0'
    setCookie(driver,'jwt',token)
    driver.refresh()