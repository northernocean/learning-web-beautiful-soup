from bs4 import BeautifulSoup
import requests
from fake_useragent import UserAgent

with open("test.html") as file:
    html = file.read()

soup = BeautifulSoup(html, "lxml")

tests = [13]

if 0 in tests:
    print("A)\n", soup.prettify(), sep="")
    print("B)\n", soup.meta["charset"], sep="")
    print("C)\n", soup.title.string, sep="")
    soup.title.string = "***"
    print("D)\n", soup.prettify(), sep="")
    print("E)\n", soup.p, sep="")

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

if 11 in tests:
    # siblings
    print(soup.body.previous_sibling) # a newline character
    print(soup.body.previous_sibling.previous_sibling) # head

if 12 in tests:
    # better way to get all siblings (also works for previous_siblings)
    for sibling in soup.body.p.next_siblings:
        if sibling != "\n":
            print(sibling.name)

if 13 in tests:
    # no previous siblings so generator yields no results.
    print("-")
    for sibling in soup.head.previous_sibling.previous_siblings:
        print(sibling)
    print("-")