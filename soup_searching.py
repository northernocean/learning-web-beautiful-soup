from bs4 import BeautifulSoup
import requests
import re
from fake_useragent import UserAgent

with open("test.html") as file:
    html = file.read()

soup = BeautifulSoup(html, "lxml")

tests = [1]

if 1 in tests:
    print("")
    print("~~~~~searching~~~~~")
    # search for a tag
    for tag in soup.find_all("b"):
        print(tag.name)
    print("")
    # search for a tag using regex matching
    for tag in soup.find_all(re.compile("^b")):
        print(tag.name)
    print("")
    # search for tags from a list
    for tag in soup.find_all(["a","html","body"]):
        print(tag.name)
    # search for a tags using a function
    print("")
    for tag in soup.find_all(lambda tag : tag.has_attr("charset")):
        print(tag.name)


