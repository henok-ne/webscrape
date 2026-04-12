import requests
from bs4 import BeautifulSoup

def scrape_quotes(page: int):
    url = f"http://quotes.toscrape.com/page/{page}"

    headers = {"User-Agent": "Mozilla/5.0"}

    try:
        response = requests.get(url, headers=headers, timeout=5)
        response.raise_for_status()
    except:
        return {"error": "Failed to fetch website"}

    soup = BeautifulSoup(response.text, "html.parser")
    quotes = soup.find_all("div", class_="quote")

    if not quotes:
        return {"error": "No quotes found"}

    data = []

    for q in quotes:
        text_tag = q.find("span", class_="text")
        author_tag = q.find("small", class_="author")

        text = text_tag.text if text_tag else "N/A"
        author = author_tag.text if author_tag else "N/A"

        data.append({
            "text": text,
            "author": author
        })

    return {"page": page, "data": data}