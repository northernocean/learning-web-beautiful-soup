from bs4 import BeautifulSoup
import requests
from fake_useragent import UserAgent

ua = UserAgent()

headers = {"user-agent": ua.random}

url = "https://google.com/"

# Getting the webpage, creating a Response object.
response = requests.get(
    url=url,
    headers=headers,
    timeout=3)

# Extracting the source code of the page.
content = response.content

soup = BeautifulSoup(content, "lxml")

# print(soup.prettify())
# print(soup.meta["charset"])
print(soup.body)