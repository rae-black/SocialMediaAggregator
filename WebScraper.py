from tkinter import *
import requests
from requests.auth import HTTPBasicAuth
import selenium.webdriver as webdriver
from selenium.webdriver.common.keys import Keys

# insta login page
url = "https://www.instagram.com/?hl=en"

# page = insta main feed
page = requests.get(url, auth=HTTPBasicAuth('comp363_test', 'Comp363Test*'))

driver = webdriver.Chrome()
driver.get(page.url)

print(soup.prettify())


