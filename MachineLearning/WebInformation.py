#Takes a input file with set of URLS and extracts the data and loads it to a text file.

import urllib2
from bs4 import BeautifulSoup


def fetch_content_of_url(url):
    page = urllib2.urlopen(url)
    soup = BeautifulSoup(page, 'html.parser')

    # Remove the script and css in the page
    for script in soup(["script", "style"]):
        script.extract()

    # Obtain all the text from the page
    text = soup.get_text().strip()

    # break into lines and remove leading and trailing space on each
    lines = (line.strip() for line in text.splitlines())

    # break multi-headlines into a line each
    chunks = (phrase.strip() for line in lines for phrase in line.split("  "))

    # drop blank lines
    text = '\n'.join(chunk for chunk in chunks if chunk)
    load_text_to_file(text)
    print "Loaded data of the URL  :  ", url

def load_text_to_file(text):
    fh = open("content.txt", "a")
    fh.write(text.encode('utf-8'))
    fh.close

def web_scraper(file_name):
    file = open(file_name, "r")
    urls = file.readlines()
    for url in urls:
        fetch_content_of_url(url.replace("\n", ""))
    file.close



web_scraper("list_of_url.txt")

