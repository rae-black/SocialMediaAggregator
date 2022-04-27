# Selenium imports
import wget as wget
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options

# Tkinter imports
import tkinter as tk
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkvideo import tkvideo

# Other imports
import time
import os

instagramUsername = "comptest363"
instagramPassword = "Comp12345*"


root = tk.Tk()
root.geometry("800x600")
root.resizable(1, 1)
root.title("Social Media Aggregator")

canvas = Canvas(root)
scroll_y = Scrollbar(root, orient="vertical", command=canvas.yview)

frame = Frame(canvas)

frame.bind(
    "<Configure>",
    lambda e: canvas.configure(
        scrollregion=canvas.bbox("all")
    )
)

photos = []


def displayMedia(img):

    image = Image.open(img)
    photo = ImageTk.PhotoImage(image)
    photos.append(photo)  # keep references!
    newPhoto_label = Label(frame, image=photo)
    newPhoto_label.pack()


def displayVideo(video):
    label = Label(frame)
    label.pack()
    player = tkvideo(video, label, loop=1, size=(700, 400))
    player.play()


#instagram login
options = Options()
options.add_argument("--disable-blink-features=AutomationControlled")


driver = webdriver.Chrome(options=options)
driver.get("https://www.instagram.com/")

cookies = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
    (By.XPATH, "//button[contains(text(), 'Only allow essential cookies')]"))).click()


username = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
    (By.CSS_SELECTOR, "input[name='username']")))
password = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
    (By.CSS_SELECTOR, "input[name='password']")))

username.clear()
time.sleep(2)
password.clear()
time.sleep(2)
username.send_keys(instagramUsername)
time.sleep(2)
password.send_keys(instagramPassword)
time.sleep(2)

log_in = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
    (By.CSS_SELECTOR, "button[type= 'submit']"))).click()
time.sleep(2)

not_now = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
    (By.XPATH, "//button[contains(text(), 'Not Now')]"))).click()
time.sleep(2)

not_now2 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
    (By.XPATH, "//button[contains(text(), 'Not Now')]"))).click()
time.sleep(2)

# ensure post quantity
post = driver.find_element(By.TAG_NAME, 'article')

posts = []

while len(posts) < 10:
    driver.execute_script("return arguments[0].scrollIntoView();", post)
    posts.append(driver.find_element(By.CLASS_NAME, 'FFVAD'))

print(posts)

media_srcs = [image.get_attribute("src") for image in posts]
# image_srcs = [image.get_attribute('src') for image in image_srcs]
# video_srcs = [video.get_attribute('src') for video in posts]
# video_srcs = [image.get_attribute('src') for image in video_srcs]

print(media_srcs)

post_media = []

for media_src in media_srcs:
    wget.download(media_src, post_media)

for file in post_media:
    displayMedia(file)
    print(file)


canvas.create_window(0, 0, anchor='nw', window=frame)
canvas.update_idletasks()

canvas.configure(scrollregion=canvas.bbox('all'), yscrollcommand=scroll_y.set)

canvas.pack(fill='both', expand=True, side='left')
scroll_y.pack(fill='y', side='right')


root.mainloop()

# Email account password: Comp12345*

# instagram username: comptest363
# instagram password: Comp12345*
