import uvicorn

from src.settings import settings


def main():
    uvicorn.run("src.app:app", host=settings.host, port=settings.port, reload=settings.debug)


if __name__ == "__main__":
    main()
