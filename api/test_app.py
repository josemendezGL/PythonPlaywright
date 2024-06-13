import pytest
from playwright.sync_api import *

@pytest.fixture
def api_context(playwright: Playwright) -> APIRequestContext:
    api_context = playwright.request.new_context(
        base_url="https://dummyjson.com",
        extra_http_headers={'Content-Type': 'application/json'},
    )
    yield api_context
    api_context.dispose()

@pytest.mark.skip()
def test_users_search(api_context: APIRequestContext):
    query = "Jack"
    response = api_context.get(f"/users/search?q={query}")
        
    users_data = response.json()
    print("Users found: ", users_data["total"])    
    
    for user in users_data["users"]:
        print("Checking user: ", user["firstName"])
        assert query in user["firstName"]
        
@pytest.mark.skip()
def test_create_user(api_context: APIRequestContext):
    response = api_context.post(
        "users/add",
        data={
            "firstName": "Damien",
            "lastName": "Smith",
            "age": 27
        }
    )
    user_data = response.json()
    
    print(f"\n{user_data}")
    
    assert user_data["id"] == 209
    assert user_data["firstName"] == "Damien"

@pytest.mark.skip()
def test_update_user(api_context: APIRequestContext):
    response = api_context.put(
        "users/1",
        data={
            "firstName": "Damien",
            "lastName": "Smith",
            "age": 27
        }
    )
    user_data = response.json()
    
    print(f"\n{user_data}")
    
    assert user_data["firstName"] == "Damien"
    
def test_delete_user(api_context: APIRequestContext):
    response = api_context.delete(
        "users/1",
    )
    
    request_status = response.status
    user_data = response.json()    
    
    print("Status code >>>>>> ", request_status)
    print(f"\n{user_data}")
    




    
    
    