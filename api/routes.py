from fastapi import APIRouter
from services.scraper import  scrape_site

router = APIRouter()

@router.get("/")
def scrape(site: str, page: int = 1):
    return scrape_site(site, page)