import pytest
from server.app import create_app, db
from server.models.user import User
from server.models.guest import Guest
from server.models.episode import Episode
from server.models.appearance import Appearance
from flask_jwt_extended import create_access_token
from datetime import date

@pytest.fixture
def client():
    app = create_app()
    app.config["TESTING"] = True
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"
    app.config["JWT_SECRET_KEY"] = "test-secret"

    with app.app_context():
        db.create_all()

   
        user = User(username="alvine")
        user.set_password("test123")
        db.session.add(user)

        guest = Guest(name="Test Guest", occupation="Tester")
        db.session.add(guest)

        episode = Episode(date=date.today(), number=1)
        db.session.add(episode)
        db.session.commit()

        yield app.test_client()

        db.session.remove()
        db.drop_all()

def test_register(client):
    response = client.post("/register", json={
        "username": "newuser",
        "password": "newpass"
    })
    assert response.status_code == 201

def test_login(client):
    response = client.post("/login", json={
        "username": "alvine",
        "password": "test123"
    })
    assert response.status_code == 200
    assert "access_token" in response.get_json()

def test_get_episodes(client):
    response = client.get("/episodes")
    assert response.status_code == 200
    assert isinstance(response.get_json(), list)

def test_get_episode_by_id(client):
    response = client.get("/episodes/1")
    assert response.status_code == 200
    assert "appearances" in response.get_json()

def test_get_guests(client):
    response = client.get("/guests")
    assert response.status_code == 200
    assert isinstance(response.get_json(), list)

def test_unauthorized_post_appearance(client):
    response = client.post("/appearances", json={
        "guest_id": 1,
        "episode_id": 1,
        "rating": 5
    })
    assert response.status_code == 401 

