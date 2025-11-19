from app import create_app
import pytest

@pytest.fixture
def app():
    return create_app()

@pytest.mark.asyncio
async def test_check_session_returns_false_when_not_logged(app):
    async with app.test_client() as client:
        response = await client.get('/auth/check-session')
        assert response.status_code == 200
        json_data = await response.get_json()
    assert 'logged_in' in json_data
    assert json_data['logged_in'] is False
