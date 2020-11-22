import sys
import os.path
from bs4 import BeautifulSoup
import requests
from fake_useragent import UserAgent

if not os.path.exists("codingbat-java.txt"):
    ua = UserAgent()
    headers = {"user-agent":ua.random}
    response = requests.get(
        "https://codingbat.com/java",
        headers=headers)
    if response:
        soup = BeautifulSoup(response.text, "lxml")
        with open("codingbat-java.html", "w") as file:
            file.write(soup.prettify())

with open("codingbat-java.html", "r") as file:
    text = file.read()

soup = BeautifulSoup(text, "lxml")

tables = soup.find_all("table")

exercises = {}
for table in tables:
    divs = table.find_all("div", class_="summ")
    dic = {
        "https://codingbat.com" + div.a["href"].strip() :
        div.a.span.string.strip()
        for div in divs
        }
    if dic:
        exercises.update(dic)

for key, value in exercises.items():
    print(key, value)





