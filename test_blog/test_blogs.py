def test_create_user(client):
    payload = {
        "name": "Test User",
        "email": "testuser@example.com",
        "password": "StrongPass123$"
        }

    response = client.post("/users/create-user", json=payload)

    assert response.status_code == 200
    assert "rows inserted" in response.json()["Response"]

# def test_get_user(client):
#     email = "testuser@example.com"

#     response = client.get(f"/users/get-user/{email}")

#     assert response.status_code == 200

    # data = response.json()["data"]

    # # Returned fields (excluding password)
    # assert data[0] == "Test User"
    # assert data[1] == "testuser@example.com"

def test_create_blog(client, auth_headers):
    payload = {
        "title": "Test Blog Title",
        "body": "This is a test blog body",
        "used_id": 1
        }
    
    response = client.post(
        "/blogs/create-blog",
        json=payload,
        headers=auth_headers
    )
    
    assert response.status_code in (200, 201)

def test_get_blogs(client, auth_headers):
    response = client.get("/blogs/get-Blogs", headers=auth_headers)
    assert response.status_code == 200
    
    data = response.json()
    assert isinstance(data, list)
    
    assert len(data) >= 0