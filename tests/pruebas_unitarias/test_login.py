from app import create_app
import pytest

@pytest.fixture
def app():
    return create_app()

@pytest.mark.asyncio
async def test_login_page_loads(app):
    async with app.test_client() as client:
        response = await client.get('/auth/login')
    assert response.status_code == 200
    data = await response.get_data()
    assert b'Ingresar' in data or b'Usuario' in data