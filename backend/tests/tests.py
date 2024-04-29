import jwt
from fastapi.testclient import TestClient

from app.main import get_db, app

client = TestClient(app)


def create_access_token(payload):
    secret_key = 'test_secret_key'
    algorithm = 'HS256'

    access_token = jwt.encode(payload, secret_key, algorithm=algorithm)
    return access_token


test_username = "test_user"
test_book_id = "OL7353617M"
test_token = create_access_token({"username": test_username})
test_auth_header = {'Authorization': test_token}


# Test if the user creation endpoint works as expected
def test_create_user():
    response = client.post("/user", json={"username": test_username},
                           headers=test_auth_header)

    assert response.status_code == 200
    assert response.json()["username"] == test_username


# Test if the search books endpoint returns the expected result
def test_search_books():
    response = client.get("/search_books?"
                          "name=example"
                          "&author=author1"
                          "&tags=tag1,tag2"
                          "&page=1"
                          "&size=1")
    assert response.status_code == 200
    assert len(response.json()) > 0


# Test if the endpoint to choose favorite books works as expected
def test_choose_favorites():
    response = client.post(f"/user/{test_username}/books",
                           json=[test_book_id],
                           headers=test_auth_header)
    assert response.status_code == 200
    assert response.json() == {"message": "Favorites updated successfully"}


# Test if the endpoint to delete favorite books works as expected
def test_delete_favorites():
    response = client.delete(f"/user/{test_username}/books/{test_book_id}")
    assert response.status_code == 200
    assert response.json() == {"message": "Favorite book deleted successfully"}


# Test if the endpoint to get favorite books works as expected
def test_get_favorites():
    response = client.get(f"/user/{test_username}/books?brief=True")
    assert response.status_code == 200
    assert len(response.json()) == 0
