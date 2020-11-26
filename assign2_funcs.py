import sys
import os.path
from bs4 import BeautifulSoup
from bs4.element import NavigableString
import requests
from fake_useragent import UserAgent

ua = None
headers = None
BASE_URL = "https://codingbat.com"


def get_soup(url):
    global ua
    global headers
    if ua == None:
        ua = UserAgent()
        headers = {"user-agent":ua.random}
    response = requests.get(
        url,
        headers=headers)
    if response:
        soup = BeautifulSoup(response.text, "lxml")
    else:
        text = '<!DOCTYPE html><html lang="en"><head>'
        text += '<meta charset="UTF-8"><meta name="viewport" '
        text += 'content="width=device-width, initial-scale=1.0">'
        text += '<title>Document</title></head><body></body></html>'
        soup = BeautifulSoup(text, "lxml")
    return soup


def scrape_home():
    soup = get_soup(BASE_URL + "/java")
    tables = soup.find_all("table")
    exercises = {}
    for table in tables:
        divs = table.find_all("div", class_="summ")
        dic = {
            BASE_URL + div.a["href"].strip() :
            div.a.span.string.strip()
            for div in divs
            }
        if dic:
            exercises.update(dic)
    return list(exercises.keys())


def scrape_section(url):
    soup = get_soup(url)
    table_cells = (
        soup
        .find("div", class_="tabin")
        .find("table")
        .find_all("td"))
    return [BASE_URL + cell.find("a")["href"] for cell in table_cells]
    

def scrape_question(url):
    soup = get_soup(url)
    table_cell = soup.find("div", class_="tabin").find("table").find("td")
    result = "-------------\n"
    result += str(table_cell.find("p").string).strip() + "\n"
    result += "-------------\n"
    for child in table_cell.children:
        if type(child) is NavigableString and child != "\n":
            result += str(child).strip() + "\n"
    return result
