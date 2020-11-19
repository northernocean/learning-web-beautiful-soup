from bs4 import BeautifulSoup
import requests
from fake_useragent import UserAgent

def read_file():
    with open("test.html") as file:
        return file.read()

html = read_file()

soup = BeautifulSoup(html, "lxml")

tests = [0]

if 0 in tests:
    print("A)\n", soup.prettify())
    print("B)\n", soup.meta["charset"])
    print("C)\n", soup.title.string)
    soup.title.string = "***"
    print("D)\n", soup.prettify())
    print("E)\n", soup.p)

if 1 in tests:
    print("")
    print("~~~~~head.contents~~~~~")
    # 1 element --> the head element
    elements = [child for child in soup.head.contents if child != '\n']
    print(len(elements))
    for child in elements:
        print(child)

if 2 in tests:
    print("")
    print("~~~~~body.contents~~~~~")
    # 4 elements --> the body elements (b, p, p, p). Only direct children
    elements = [child for child in soup.body.contents if child != '\n']
    print(len(elements))
    for child in elements:
        print(child)

if 3 in tests:
    print("")
    print("~~~~~body.children~~~~~")
    # 4 elements --> the body elements (b, p, p, p). Only direct children
    elements = [child for child in soup.body.children if child != '\n']
    print(len(elements))
    for child in elements:
        print(child)

if 4 in tests:
    print("")
    print("~~~~~head.descendants~~~~~")
    # 2 elements --> the title tag, and the inner text of the title tag
    elements = [child for child in soup.head.descendants if child != '\n']
    print(len(elements))
    for child in elements:
        print(child)

if 5 in tests:
    print("")
    print("~~~~~body.descendants~~~~~")
    # many elements --> the body tag, its children, and their children
    elements = [child for child in soup.body.descendants if child != '\n']
    print(len(elements))
    for index, child in enumerate(elements):
        print(index, '{' + str(child) + '}')

if 6 in tests:
    print(type(soup.body.contents)) # --> list
    print(type(soup.body.children)) # --> list_iterator
    print(type(soup.body.descendants)) # --> generator
    print(type(soup.body.parents)) # --> generator

if 7 in tests:
    # parents
    print(1, soup.a)
    print(2, soup.a.parent)
    print(3, soup.a.parent.parent)
    print(4, soup.a.parent.parent.parent)

if 8 in tests:
    # parents
    elements = soup.a.parents
    for index, element in enumerate(elements):
        print(chr(index+97) + ') ', element)

if 9 in tests:
    # parents
    elements = soup.a.parents
    for index, element in enumerate(elements):
        print(chr(index+97) + ') ', element.name)

if 10 in tests:
    # siblings
    print(soup.body.p)
    print(soup.body.p.next_sibling) # a newline character
    print(soup.body.p.next_sibling.next_sibling) # the next p tag
    print(soup.body.p.next_sibling.next_sibling.next_sibling) # a newline character
    print(soup.body.p.next_sibling.next_sibling.next_sibling.next_sibling) # the next p tag
    print(soup.body.p.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling) # a newline character
    print(soup.body.p.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling) # None

