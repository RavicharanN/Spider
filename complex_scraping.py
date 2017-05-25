#import urllib.requests
# Scraping in which the first page contains the likns to the jokes(page 2)
# the joke is present in page2  and is reqired to be scraped
import requests
from bs4 import BeautifulSoup

page  =  requests.get("http://jokes.cc.com/funny-technology")

soup = BeautifulSoup(page.content,'html.parser')
listjokes = list(soup.findAll(class_="middle")) #

#print(listjokes)
jokelinks = listjokes[2] # Look into the Sorce code of the webpage and then uncomment line12. Then compare them.

for item in jokelinks.findAll('a'):
	jokepage = requests.get(item.get('href'))  #item.get('href') gives the link of the page.
	Jokesoup = BeautifulSoup(jokepage.content,'html.parser') #And the BS of that pge is stored in a soup
	for item in Jokesoup.findAll(class_='content_wrap') :
		print (item.find('a').get("href")) #If an a tag is present it gives the href
		print (item.find('p').get_text()) #prints all the 'p's inside a class 
		
