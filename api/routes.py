from fastapi import APIRouter
from services.scraper import scrape_quotes

router = APIRouter()

@router.get("/quotes")
def get_quotes(page: int = 1):
    return scrape_quotes(page)