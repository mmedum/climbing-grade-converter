from starlette.testclient import TestClient

from climbing_grade_converter.main import app

client = TestClient(app)


def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"msg": "Hello from the Climbing Grade Converter!"}
