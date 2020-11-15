from bs4 import BeautifulSoup
import requests
from fake_useragent import UserAgent

content = """<html>
<head>
  <title>The Dormouse's story</title>
</head>
<body>
  <b></b>
  <p class="title">
    <b>The Dormouse's story</b>
  </p>
  <p class="story">
    Once upon a time there were three little sisters; and their names were
    <a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>,
    <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a> and
    <a class="sister" href="http://example.com/tillie" id="link2"> Tillie</a>
      ; and they lived at the bottom of a well.
  </p>
  <p class="story">
    <b>The End</b>
  </p>
</body>
</html>"""

soup = BeautifulSoup(content, "lxml")

head = soup.head

for child in head.contents:
    print(child if child is not None else "")

body = soup.body

for child in body.contents:
    print(child if child is not None else "")

for child in body.children:
    print(child if child is not None else "")

print(type(soup.body.contents))
print(type(soup.body.children))
