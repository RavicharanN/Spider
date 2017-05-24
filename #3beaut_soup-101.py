import requests
from bs4 import BeautifulSoup

page = open("test.html","r") # the contents of a sample html file have been fed into this variable

soup = BeautifulSoup(page,'html.parser') 
# In the above class, "page" contains the required text(here html content)..and..
# .."html.parser" instructs that the content should be parsed as per the html format

print soup.prettify()
# prints the html file with a proper indentation

