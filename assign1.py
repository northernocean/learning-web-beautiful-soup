from bs4 import BeautifulSoup
import requests
from fake_useragent import UserAgent

ua = UserAgent()
headers = {"user-agent":ua.random}
response = requests.get(
    "https://boston.craigslist.org/search/sof",
    headers=headers)
soup = BeautifulSoup(response.text, "lxml")
for item in soup.find_all("li", class_="result-row"):
    el = item.find("a", class_="result-title")
    print("Job: " + el.text)
    print("URL: " + el.attrs.get("href"))
    print("")