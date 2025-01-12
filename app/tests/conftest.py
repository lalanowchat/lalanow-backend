import pytest

from fastapi.testclient import TestClient


@pytest.fixture(scope="module")
def client():
    import app.main as main

    return TestClient(main.app)
