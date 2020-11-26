import sys
import os.path
from bs4 import BeautifulSoup
from bs4.element import NavigableString
import requests
from fake_useragent import UserAgent

ua = None
headers = None

def init():
    global ua
    global headers
    if ua == None:
        ua = UserAgent()
        headers = {"user-agent":ua.random}


def scrape_home():
    global ua
    global headers
    init()
    if(False):
        if not os.path.exists("codingbat-java.txt"):
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
    else:
        response = requests.get(
            "https://codingbat.com/java",
            headers=headers)
        if response:
            soup = BeautifulSoup(response.text, "lxml")

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

    return list(exercises.keys())


def scrape_section(url):
    global ua
    global headers
    init()
    if(False):
        if not os.path.exists("codingbat-java2.html"):
            response = requests.get(
                url,
                headers=headers)
            if response:
                soup = BeautifulSoup(response.text, "lxml")
                with open("codingbat-java2.html", "w") as file:
                    file.write(soup.prettify())
        with open("codingbat-java2.html", "r") as file:
            text = file.read()
        soup = BeautifulSoup(text, "lxml")
    else:
        response = requests.get(
            url,
            headers=headers)
        if response:
            soup = BeautifulSoup(response.text, "lxml")

    table_cells = (
        soup
        .find("div", class_="tabin")
        .find("table")
        .find_all("td"))
    
    return ["https://codingbat.com" + cell.find("a")["href"] for cell in table_cells]
    

def scrape_question(url):
    global ua
    global headers
    init()
    if(True):   
        if not os.path.exists("codingbat-java3.html"):
            response = requests.get(
                url,
                headers=headers)
            if response:
                soup = BeautifulSoup(response.text, "lxml")
                with open("codingbat-java3.html", "w") as file:
                    file.write(soup.prettify())
        with open("codingbat-java3.html", "r") as file:
            text = file.read()
            soup = BeautifulSoup(text, "lxml")
    else:
        response = requests.get(
            url,
            headers=headers)
        if response:
            soup = BeautifulSoup(response.text, "lxml")

    table_cell = soup.find("div", class_="tabin").find("table").find("td")
    result = "-------------\n"
    result += str(table_cell.find("p").string).strip() + "\n"
    result += "-------------\n"
    for child in table_cell.children:
        if type(child) is NavigableString and child != "\n":
            result += str(child).strip() + "\n"

    return result