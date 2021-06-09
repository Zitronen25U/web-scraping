import requests 
from bs4 import BeautifulSoup

def get_citations_needed_count(URL):
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")
    citations_needed = soup.find_all("a", title="Wikipedia:Citation needed")
    return len(citations_needed)

def get_citations_needed_report(URL):
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")
    data = soup.find_all("a", title="Wikipedia:Citation needed")
    print(f"The amount of citations needed is {data}")


string_data = get_citations_needed_report("https://en.wikipedia.org/wiki/Agios_Epiktitos")
total_count = get_citations_needed_count("https://en.wikipedia.org/wiki/Agios_Epiktitos")
print(total_count)

