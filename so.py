import requests
from bs4 import BeautifulSoup
URL = f"https://stackoverflow.com/jobs?q=javascript"


def get_last_page():
    result = requests.get(URL)
    soup = BeautifulSoup(soup.text, "html.parser")
    pages = soup.find("div", {"class": "pagination"}).find_all("a")
    last_pages = pages[-2].get_text(strip=True)


def extract_job(html):
    title = html.find("a", {"class": "s-link"})["title"]
    company_txt, location_txt = html.find(
        "h3", {"class": "mb4"}).find_all("span", recursive=False)
    company = company_txt.get_text(strip=True)
    location = location_txt.get_text(strip=True)
    job_id = html['data-jobid']

    return {"title": title, "company": company, "location": location, "apply_link": f"https://stackoverflow.com/jobs/{job_id}"}


def extract_jobs(last_page):
    jobs = []
    for page in range(last_page):
        print(f"Scrapping S0: Page: {page}")
        result = requests.get(f"{URL}&pg={page+1}")
        soup = BeautifulSoup(result.text, "html.parser")
        results = soup.find_all("div", {"class": "-job"})
        for result in results:
            job = extract_job(result)
            jobs.append(job)
        return jobs


def get_jobs():
    last_page = get_last_page()
    jobs = extract_jobs(last_page)
    return jobs
