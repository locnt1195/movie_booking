import pytest
from app import app


@pytest.fixture(scope='module')
def client():
    with app.test_client() as c:
        yield c


def test_api_key(client):
    response = client.get('/api/cinema')
    assert response.status_code == 401
    response = client.get('/api/cinema', headers={'api_key': '123'})
    assert response.status_code == 401
    response = client.get(
        '/api/cinema',
        headers={'api_key': '2d4278333671cd4b6b06a74742ebbca1'})
    assert response.status_code == 200


def test_booking(client):
    # # Sheet has been booked
    response = client.post(
        '/api/sheet/booking?sheet_id=2&book=True',
        headers={'api_key': '2d4278333671cd4b6b06a74742ebbca1'},
    )
    assert response.status_code == 400
    # Sheet has been booked
    response = client.post(
        '/api/sheet/booking?sheet_id=4&book=False',
        headers={'api_key': '2d4278333671cd4b6b06a74742ebbca1'},
    )
    assert response.status_code == 200
    # Sheet has not been booked but request false
    response = client.post(
        '/api/sheet/booking?sheet_id=3&book=True',
        headers={'api_key': '2d4278333671cd4b6b06a74742ebbca1'},
    )
    assert response.status_code == 200
