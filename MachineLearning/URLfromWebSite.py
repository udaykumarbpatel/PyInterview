#Fetch all the URL's from a given WebSite

from bs4 import BeautifulSoup
import requests
url = raw_input("Enter a website to extract the URL's from: ")
r = requests.get("http://" + url)
data = r.text
soup = BeautifulSoup(data, "html.parser")

for link in soup.find_all('a'):
    print(link.get('href'))
