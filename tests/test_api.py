"""Tests for FastAPI endpoints."""

from __future__ import annotations

import base64

import cv2
import numpy as np
import pytest
from fastapi.testclient import TestClient

from fastAPI.main import app


@pytest.fixture
def client() -> TestClient:
    return TestClient(app)


def _make_payload(size: tuple[int, int] = (64, 64)) -> dict[str, str]:
    img = np.random.randint(0, 255, (size[0], size[1], 3), dtype=np.uint8)
    _, buf = cv2.imencode(".jpg", img)
    return {"data": base64.b64encode(buf).decode()}


def test_process_image_returns_200(client: TestClient) -> None:
    resp = client.post("/process", json=_make_payload())
    assert resp.status_code == 200
    assert "image" in resp.json()


def test_process_image_returns_valid_b64(client: TestClient) -> None:
    resp = client.post("/process", json=_make_payload())
    result = resp.json()["image"]
    decoded = base64.b64decode(result)
    assert len(decoded) > 0


def test_process_missing_data_returns_422(client: TestClient) -> None:
    resp = client.post("/process", json={})
    assert resp.status_code == 422
