import pytest


@pytest.mark.asyncio
async def test_read_root_returns_html(app_client):
    response = await app_client.get("/")
    assert response.status_code == 200
    assert "text/html" in response.headers.get("content-type", "")


@pytest.mark.asyncio
async def test_create_greeting_redirects(app_client):
    response = await app_client.post(
        "/",
        data={"name": "TestUser", "message": "Hello Test!"}
    )
    assert response.status_code == 200


@pytest.mark.asyncio
async def test_create_greeting_empty_message(app_client):
    response = await app_client.post(
        "/",
        data={"name": "TestUser", "message": "   "}
    )
    assert response.status_code == 200
