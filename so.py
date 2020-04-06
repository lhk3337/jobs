import requests
from bs4 import BeautifulSoup
URL = f"https://stackoverflow.com/jobs?q=javascript"


def get_last_page():
    result = requests.get(URL)
    soup = BeautifulSoup(soup.text, "html.parser")
    pages = soup.find("div", {"class": "pagination"}).find_all("a")
    last_pages = pages[-2].get_text(strip=True)


def extract_jobs(last_jobs):
    jobs = []
    for page in range(last_jobs):
        print(f"Scrapping S0: Page: {page}")
        result = requests.get(f"{URL}&pg={page+1}")
        soup = BeautifulSoup(result.text, "html.parser")
        results = soup.find_all("div", {"class": "-job"})
        for result in results:
            print(result[data-jobid])


def get_jobs():
    last_page = get_last_page()
    jobs = extract_jobs(last_page)
    return jobs
