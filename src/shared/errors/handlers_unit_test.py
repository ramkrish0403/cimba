from fastapi import FastAPI
from fastapi.testclient import TestClient
from pydantic import BaseModel

from src.shared.errors.exceptions import AppError, NotFoundError
from src.shared.errors.handlers import register_exception_handlers


def _create_test_app() -> FastAPI:
    app = FastAPI()
    register_exception_handlers(app)

    class Item(BaseModel):
        name: str
        price: float

    @app.get("/not-found")
    async def raise_not_found():
        raise NotFoundError("Thing not found")

    @app.get("/app-error")
    async def raise_app_error():
        raise AppError("Something broke")

    @app.get("/unhandled")
    async def raise_unhandled():
        raise RuntimeError("unexpected")

    @app.post("/validate")
    async def validate_body(item: Item):
        return item

    return app


client = TestClient(_create_test_app(), raise_server_exceptions=False)


def test_not_found_error():
    resp = client.get("/not-found")
    assert resp.status_code == 404
    body = resp.json()
    assert body["error"] == "not_found"
    assert body["message"] == "Thing not found"
    assert body["details"] is None


def test_app_error():
    resp = client.get("/app-error")
    assert resp.status_code == 500
    body = resp.json()
    assert body["error"] == "internal_error"
    assert body["message"] == "Something broke"


def test_http_exception_for_unknown_route():
    resp = client.get("/nonexistent")
    assert resp.status_code == 404
    body = resp.json()
    assert body["error"] == "404"
    assert "Not Found" in body["message"]


def test_validation_error():
    resp = client.post("/validate", json={"name": "x"})
    assert resp.status_code == 422
    body = resp.json()
    assert body["error"] == "validation_error"
    assert body["message"] == "Validation failed"
    assert isinstance(body["details"], list)
    assert any("price" in d["field"] for d in body["details"])


def test_unhandled_exception():
    resp = client.get("/unhandled")
    assert resp.status_code == 500
    body = resp.json()
    assert body["error"] == "internal_error"
    assert body["message"] == "Internal server error"
