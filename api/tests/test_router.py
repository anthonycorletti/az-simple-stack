from httpx import AsyncClient


async def test_livez(client: AsyncClient) -> None:
    response = await client.get("/livez")
    assert response.status_code == 202
