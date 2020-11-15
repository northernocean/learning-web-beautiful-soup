from bs4 import BeautifulSoup
import requests
from fake_useragent import UserAgent

content = """<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Intro_to_soup</title>
    </head>
    <body>
        <div>
            <p>In first div</p>
        </div>
        <div>
            <p>In second div</p>
        </div>
    </body>
</html>"""
soup = BeautifulSoup(content, "lxml")

print(soup.prettify())
print(soup.meta["charset"])
print(soup.title.string)
soup.title.string = "***"
print(soup.prettify())
print(soup.p)



