import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from fastapi.testclient import TestClient

from Blog.main import app
from Blog.database import get_db
from Blog.models import base

SQLALCHEMY_DATABASE_URL = "postgresql+psycopg2://postgres:Iamironman2268$@localhost:5432/fastapi-test-db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)

TestingSessionLocal = sessionmaker(
    autocommit=False, autoflush=False, bind=engine
)

# Create tables for test DB
base.metadata.create_all(bind=engine)

def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()

# Override dependency
app.dependency_overrides[get_db] = override_get_db


@pytest.fixture
def client():
    return TestClient(app)

@pytest.fixture
def auth_headers(client):
    login_data = {
        "username": "testuser@example.com",
        "password": "abcdefg1234$"
    }

    response = client.post(
        "/login",
        data=login_data  # form-data for OAuth2PasswordRequestForm
    )

    assert response.status_code == 200

    token = response.json()["access_token"]

    return {
        "Authorization": f"Bearer {token}"
    }
