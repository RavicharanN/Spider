#import urllib.requests
import requests
from bs4 import BeautifulSoup

page  =  requests.get("http://jokes.cc.com/funny-technology")

soup = BeautifulSoup(page.content,'html.parser')
listjokes = list(soup.findAll(class_="middle"))

#print(listjokes)
jokelinks = listjokes[2] 

for item in jokelinks.findAll('a'):
	jokepage = requests.get(item.get('href'))
	soup = BeautifulSoup(jokepage.content,'html.parser')
	for item in soup.findAll(class_='content_wrap') :
		print (item.find('a').get("href")) #If an a tag is present it gives the href
		print (item.find('p').get_text()) #prints all the 'p's inside a class 
		