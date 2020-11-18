from bs4 import BeautifulSoup
import requests
from fake_useragent import UserAgent

content = """
<html>
  <head>
    <title>The Dormouse's story</title>
  </head>
  <body>
    <b></b>
    <p class="title">
      <b>The Dormouse's story</b>
    </p>
    <p class="story">Once upon a time there were three little sisters; and their names were
        <a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>, 
        <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a> and 
        <a class="sister" href="http://example.com/tillie" id="link2"> Tillie</a>
        ; and they lived at the bottom of a well.
    </p>
    <p class="story">
      <b>The End</b>
    </p>
  </body>
</html>
"""

soup = BeautifulSoup(content, "lxml")
print(soup.prettify())

print("")
print("~~~~~head.contents~~~~~")
# 1 element --> the head element
elements = [child for child in soup.head.contents if child != '\n']
print(len(elements))
for child in elements:
    print(child)

print("")
print("~~~~~body.contents~~~~~")
# 4 elements --> the body elements (b, p, p, p). Only direct children
elements = [child for child in soup.body.contents if child != '\n']
print(len(elements))
for child in elements:
    print(child)

print("")
print("~~~~~body.children~~~~~")
# 4 elements --> the body elements (b, p, p, p). Only direct children
elements = [child for child in soup.body.children if child != '\n']
print(len(elements))
for child in elements:
    print(child)

print("")
print("~~~~~head.descendants~~~~~")
# 2 elements --> the title tag, and the inner text of the title tag
elements = [child for child in soup.head.descendants if child != '\n']
print(len(elements))
for child in elements:
    print(child)

print("")
print("~~~~~body.descendants~~~~~")
# many elements --> the body tag, its children, and their children
elements = [child for child in soup.body.descendants if child != '\n']
print(len(elements))
for index, child in enumerate(elements):
    print(index, '{' + str(child) + '}')

# print(type(soup.body.contents)) # --> list
# print(type(soup.body.children)) # --> list_iterator
# print(type(soup.body.descendants)) # --> generator
