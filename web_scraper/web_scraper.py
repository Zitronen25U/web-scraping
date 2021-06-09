import requests 
from bs4 import BeautifulSoup

def get_citations_needed_count(URL):
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")
    citations_needed = soup.find_all("a", title="Wikipedia:Citation needed")
    return len(citations_needed)

def get_citations_needed_report():
    pass

total_count = get_citations_needed_count(#URL GOES HERE)
print(total_count)