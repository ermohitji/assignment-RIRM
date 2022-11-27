import re

import requests
from bs4 import BeautifulSoup

sn_links = ["facebook", "linkedin", "instagram", "github", "youtube"]


def get_links(url):
    result = {}
    found_social_links = set()
    found_emails = set()
    found_phones = set()

    body = requests.get(url)
    soup = BeautifulSoup(body.text, 'html.parser')
    results = soup.find_all("a")

    for i in range(0, len(results)):
        if "href" in results[i].attrs:
            for social in sn_links:
                if re.search("^(http|https)([a-z]).*" + social, results[i].attrs["href"]):
                    found_social_links.add(results[i].attrs["href"])
            if re.search("mailto", results[i].attrs["href"]):
                email = results[i].attrs["href"].removeprefix("mailto:")
                found_emails.add(email)
            if re.search("tel:", results[i].attrs["href"]):
                phone = results[i].string.removeprefix("tel:")
                found_phones.add(phone)
    result["social"] = list(found_social_links)
    result["emails"] = list(found_emails)
    result["phones"] = list(found_phones)

    return result
