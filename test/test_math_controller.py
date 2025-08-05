import json
import pytest  # type: ignore
from fastapi.testclient import TestClient  # type: ignore
from src.app import app  # type: ignore

client = TestClient(app)


def test_pow_success(monkeypatch):
    payload = {"base": 2, "exponent": 3}
    response = client.post("/pow", json=payload)
    assert response.status_code == 200
    body = response.json()
    assert body["result"] == "8"


def test_fib_success(monkeypatch):
    payload = {"n": 5}
    response = client.post("/fib", json=payload)
    assert response.status_code == 200
    assert response.json()["result"] == "5"


def test_factorial_success():
    response = client.post("/factorial", json={"n": 4})
    assert response.status_code == 200
    assert response.json()["result"] == "24"


def test_negative_fib():
    response = client.post("/fib", json={"n": -1})
    assert response.status_code == 422  # validation error


def test_invalid_json():
    response = client.post("/pow", data="notjson")
    assert response.status_code == 422


def test_server_error(monkeypatch):
    def bad_pow(base, exponent):
        raise Exception("boom")

    monkeypatch.setattr("services.math_service.compute_pow", bad_pow)
    response = client.post("/pow", json={"base": 2, "exponent": 3})
    assert response.status_code == 500
    assert response.json()["detail"] == "Internal server error"
