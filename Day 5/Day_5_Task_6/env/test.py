#Use Of Requests
import requests
import re

def title(html):
    pattern = r"<title>.*</title>"
    title = re.findall(pattern,html)
    return(title[0][7:-8])

#Fetching the page
x = requests.get("https://www.srmist.edu.in/")
html = x.text

print(title(html))
