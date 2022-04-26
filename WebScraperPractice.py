# Selenium imports
import wget as wget
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

# Tkinter imports
import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk

# Other imports
import os

root = tk.Tk()
root.resizable(0, 0)
root.title("Social Media Aggregator")
canvas = Canvas(root).pack()

#instagram login
driver = webdriver.Chrome()
driver.get("https://www.instagram.com/")
username = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
    (By.CSS_SELECTOR, "input[name='username']")))
password = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
    (By.CSS_SELECTOR, "input[name='password']")))

username.clear()
password.clear()
username.send_keys("comp363_test")
password.send_keys("Comp363Test*")

log_in = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
    (By.CSS_SELECTOR, "button[type= 'submit']"))).click()

not_now = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
    (By.XPATH, "//button[contains(text(), 'Not Now')]"))).click()
not_now2 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
    (By.XPATH, "//button[contains(text(), 'Not Now')]"))).click()

driver.execute_script("window.scrollTo(0, 5000);")

image_srcs = driver.find_elements(By.CLASS_NAME, "FFVAD")
image_srcs = [image.get_attribute('src') for image in image_srcs]

PILimages = []

for image_src in image_srcs:
    wget.download(image_src, 'C:/Users/raybo/OneDrive/Documents/School/Comp 363/images')

for img_file in os.listdir('C:/Users/raybo/OneDrive/Documents/School/Comp 363/images'):
    img = ImageTk.PhotoImage(Image.open(img_file))
    PILimages.append(img)
    canvas.create_image(20, 20, anchor=NW, image=img)


#Twitter login
driver = webdriver.Chrome()
driver.get("https://twitter.com/?lang=en")
click_sign_in = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
    (By.XPATH, "//button[contains(text(), 'Sign in')]"))).click()
username = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
    (By.CSS_SELECTOR, "input[name='test']")))
username.clear()
username.send_keys("comptest363")
click_next = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
    (By.XPATH, "//button[contains(text(), 'Next')]"))).click()

password.clear()
password = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
    (By.CSS_SELECTOR, "input[name='password']")))
password.send_keys("Comp12345*")
log_in = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
    (By.CSS_SELECTOR, "button[type= 'Log in']"))).click()


#Facebook login
driver = webdriver.Chrome()
driver.get("https://twitter.com/?lang=en")
username = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
    (By.CSS_SELECTOR, "input[name='email']")))
username.clear()
username.send_keys("comptest363@gmail.com")

password = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
    (By.CSS_SELECTOR, "input[name='pass']")))
password.clear()
password.send_keys("Comp12345*")
log_in = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
    (By.CSS_SELECTOR, "button[type= 'Log in']"))).click()



root.mainloop()
