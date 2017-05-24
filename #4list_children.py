import requests
from bs4 import BeautifulSoup

page = open("test.html","r") 

soup = BeautifulSoup(page,'html.parser')

soup_child = list(soup.children) 

print (soup_child) # This prints all seperate children of soup.

#Now if we want to access a specific para we access it as a hierarchy
# First we access the second item in the list, i.e ,  the <html>...</html> part and access itas children.
# this is done as a hierarchy

html =  list(soup_child[2]) #storing the list of children of html tag

print(html) # prints the children of html

body = list(html[3])

print(body)

p  = (body[1])
print(p.get_text()) #thus the sesired paragraph is accessed this way.

