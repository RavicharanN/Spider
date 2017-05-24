# This code checks whether the required page is downloaded.
# if Downloaded the status_code takes the value 200 and it is printedS
import requests

page = requests.get("http://google.co.in")
print page.status_code


