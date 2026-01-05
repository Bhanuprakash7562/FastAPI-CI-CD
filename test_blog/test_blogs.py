def test_get_blogs(client, auth_headers):
    response = client.get("/blogs/get-Blogs", headers=auth_headers)
    assert response.status_code == 200
    
    data = response.json()
    assert isinstance(data, list)
    
    assert len(data) >= 0


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