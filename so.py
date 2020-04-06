import requests
from bs4 import BeautifulSoup
URL = f"https://stackoverflow.com/jobs?q=javascript"


def get_last_page():
    result = requests.get(URL)
    soup = BeautifulSoup(soup.text, "html.parser")
    pages = soup.find("div", {"class": "pagination"}).find_all("a")


def get_jobs():
    last_page = get_last_page()
    return []
