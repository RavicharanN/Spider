# this code prints the html content of the downloaded page
import requests
page = requests.get("https://google.co.in")
print page.content
