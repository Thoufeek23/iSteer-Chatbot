import requests
from bs4 import BeautifulSoup
import html2text


def get_internal_links(base_url, max_pages=100):
    visited = set()
    to_visit = [base_url]
    pages = []

    while to_visit and len(pages) < max_pages:
        url = to_visit.pop()
        if url in visited:
            continue
        visited.add(url)
        try:
            resp = requests.get(url)
            soup = BeautifulSoup(resp.text, 'html.parser')
            pages.append((url, soup))

            for link in soup.find_all('a', href=True):
                full_url = requests.compat.urljoin(base_url, link['href'])
                if base_url in full_url and full_url not in visited:
                    to_visit.append(full_url)
        except Exception as e:
            continue
    return pages

def scrape_website_recursively(base_url):
    pages = get_internal_links(base_url)
    all_text = ""
    for url, soup in pages:
        print(f"Scraping {url}")
        for tag in soup(["script", "style", "nav", "footer"]):
            tag.decompose()
        markdown = html2text.HTML2Text()
        markdown.ignore_images = True
        markdown.body_width = 0
        all_text += markdown.handle(str(soup)) + "\n\n"
    return all_text
