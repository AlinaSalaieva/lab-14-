import requests as ny
from bs4 import BeautifulSoup

content = ny.get("https://lipsum.com/").content
soup = BeautifulSoup(content, "html.parser")

headerList = soup.find_all("h2")

completeString = ""
for h in headerList:
    completeString += str(h) + "\n"

with open("headers.txt", "w") as f:
    f.write(completeString)