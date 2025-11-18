from app import create_app
import pytest

@pytest.fixture
def app():
    return create_app()

@pytest.mark.asyncio
async def test_index_loads(app):
    async with app.test_client() as client:
        response = await client.get('/')
    assert response.status_code == 200
    data = await response.get_data()
    assert b'EcomData' in data or b'Ingreso' in data