from fastapi import FastAPI
from api.routes import router
from core.logging import setup_logging

setup_logging()
app = FastAPI()

app.include_router(router, prefix="/scrape")