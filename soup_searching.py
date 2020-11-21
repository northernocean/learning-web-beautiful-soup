from bs4 import BeautifulSoup
import requests
import re
from fake_useragent import UserAgent

with open("test.html") as file:
    html = file.read()

soup = BeautifulSoup(html, "lxml")

tests = [5]

if 1 in tests:
    print("")
    print("~~~~~basic searching~~~~~")
    print("\n1)")
    # search for a tag
    for tag in soup.find_all("b"):
        print(tag.name)
    print("\n2)")
    # search for a tag using regex matching
    for tag in soup.find_all(re.compile("^b")):
        print(tag.name)
    print("\n3)")
    # search for tags from a list
    for tag in soup.find_all(["a","html","body"]):
        print(tag.name)
    print("\n4)")
    # search for tag with a filter predicate
    for tag in soup.find_all(id="link2"):
        print(tag.name)
    # search for a tags using a function
    print("\n5)")
    for tag in soup.find_all(lambda tag : tag.has_attr("charset")):
        print(tag.name)

if 2 in tests:
    print("")
    print("~~~~~find_all()~~~~~")
    print("\n1)")
    # if not a recognized argument, then filter on attributes
    for tag in soup.find_all("link1"):
        print(tag)
    print("\n2)")
    for tag in soup.find_all(id="link1"):
        print(tag)
    
    print("\n3)")
    # use a dictionary to pass multiple attributes
    attr={"id":"link1", "class":"sister"}
    for tag in soup.find_all(attrs=attr):
        print(tag)
    print("\n4)")
    # mix tag searching with attr searching
    attr={"id":"link1", "class":"sister"}
    for tag in soup.find_all("a", attrs=attr):
        print(tag)
    print("\n5)")
    # class is a reserved word - special syntax
    for tag in soup.find_all(class_="story"):
        print(tag.name)

if 3 in tests:
    print("")
    print("\n1)")
    # using string parameter to search inner text
    for tag in soup.find_all(string="Elsie"):
        print(tag)

if 4 in tests:
    print("")
    print("\n1")
    # non-recursive search (applies only to find_all and find)
    for tag in soup.find_all("title"):
        print(tag)
    print("\n2")
    for tag in soup.find_all("title", recursive=False):
        print(tag)
    
if 5 in tests:
    print("")
    print("\n1")
    # find is like find_all but returns only the first match
    # and does not return a list...
    for tag in soup.find("title"):
        print(tag)
    print (soup.find("title"))
    
    print("")
    print("\n2")
    # note: find returns a tag element:
    x = soup.find("title")
    print(type(x))
    print(x)
    print("")
    print("\n3")
    # iterating this result returns the things in the tag:
    for x in soup.find("title"):
        print(type(x))
        print(x)

    print("")
    print("\n4")
    # note: find_all returns a list (actually a ResultSet!):
    x = soup.find_all("title", limit=1)
    print(type(x))
    print(x)
    print("")
    print("\n5")
    # iterating this result returns the things in the ResultSet:
    for x in soup.find_all("title", limit=1):
        print(type(x))
        print(x)
