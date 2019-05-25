import pytest
from flask import url_for

@pytest.fixture
def test_homepage_response(client):
    res = client.get("/")
    assert res.status_code == 200
    assert res.data == b"ok"

