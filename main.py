from fastapi import FastAPI
import requests
from bs4 import BeautifulSoup

app = FastAPI()

@app.get("/scrape/quotes")
def scrape_quotes(page: int=1):
    url = f"http://quotes.toscrape.com/{page}"
    response = requests.get(url)

    soup = BeautifulSoup(response.text, "html.parser")

    quotes = soup.find_all("div", class_="quote")

    data = [] 

    for q in quotes:
        text = q.find("span", class_="text").text
        author = q.find("small", class_="author").text

        data.append({
            "text": text,
            "author": author
        })

    return {"data": data}