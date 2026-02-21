from fastapi import FastAPI

from src.lifespan import lifespan
from src.logging import setup_logging
from src.router import router
from src.settings import settings

setup_logging()

app = FastAPI(title=settings.app_name, debug=settings.debug, lifespan=lifespan)
app.include_router(router)
