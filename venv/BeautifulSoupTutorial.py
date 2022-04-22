from tkinter import *
import requests
from bs4 import BeautifulSoup

URL = "https://realpython.github.io/fake-jobs/"
page = requests.get(URL)

# creates beautifulsoupobject
soup = BeautifulSoup(page.content, "html.parser")

results = soup.find(id="ResultsContainer")
job_elements = results.find_all("div", class_="card-content")

python_jobs = results.find_all(
    "h2", string=lambda text: "python" in text.lower()\
    )
python_job_elements = [
    h2_element.parent.parent.parent for h2_element in python_jobs
]

root = Tk()
scrollbar = Scrollbar(root, orient=VERTICAL)
scrollbar.pack(side = RIGHT, fill = Y)
text = Text(root, yscrollcommand = scrollbar.set)
for job_element in python_job_elements:
    title_element = job_element.find("h2", class_="title")
    company_element = job_element.find("h3", class_="company")
    location_element = job_element.find("p", class_="location")
    text.insert(END, title_element.text + company_element.text +
               location_element.text + "\n")
    links = job_element.find_all("a", text="Apply")
    for link in links:
        link_url = link["href"]
        text.insert(END, f"Apply here: {link_url}\n")
    text.insert(END, "\n")

text.pack(side=LEFT, expand=True)
scrollbar.config(command=text.yview)

root.mainloop()