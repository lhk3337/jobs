import requests
from bs4 import BeautifulSoup

indeed_result = requests.get(https: // www.indeed.com/jobs?q=javascript & limit=50)
indeed_soup = BeautifulSoup(indeed_result.text, "html.parser")

pagination = indeed_soup.find("div", {"class": "pagination"})

link = pagination.find_all("a")
pages = []
for link in links[:-1]:
    pages.append(int(link.string))

max_page = pages[-1]
