import pytest
from playwright.sync_api import Playwright, APIRequestContext
from api.tests.organizations.helpers.organizations_api_helper import get_all_organizations
from api.tests.boards.helpers.boards_api_helpers import (create_board, delete_all_boards,
    delete_board, update_board, get_board)
import json

@pytest.fixture
def api_context(playwright: Playwright) -> APIRequestContext:
    api_context = playwright.request.new_context(
        base_url="https://api.trello.com/1/",
        extra_http_headers={'Content-Type': 'application/json'},
    )
    yield api_context
    api_context.dispose()

@pytest.mark.skip()
def test_get_all_boards(api_context: APIRequestContext):
    response = get_all_organizations(api_context)
    
    # Print status and raw response text for debugging
    print(f"Status code: {response.status}")
    #assert(response.status==200)
    print(f"Response text: {response.text()}")

    # Attempt to parse JSON if status is OK
    if response.status == 200:
        try:
            json_data = response.json()
            print(json_data)
        except Exception as e:
            print(f"Failed to parse JSON: {e}")
    else:
        print("Request failed with status code:", response.status)
        
        
@pytest.mark.skip()        
def test_create_board(api_context: APIRequestContext):
    response = create_board(api_context)
    
    print(f"Status code: {response.status}")
    #assert(response.status==200)
    print(f"Response text: {response.text()}")

    # Attempt to parse JSON if status is OK
    if response.status == 200:
        try:
            json_data = response.json()
            print(json_data)
        except Exception as e:
            print(f"Failed to parse JSON: {e}")
    else:
        print("Request failed with status code:", response.status)
   
    
@pytest.mark.skip()        
def test_delete_board(api_context: APIRequestContext):
    create_response = create_board(api_context)
    
    print(f"Status code: {create_response.status}")
    #assert(response.status==200)
    print(f"Response text: {create_response.text()}")
    
    created_board_text = create_response.text()    
    created_board_dict = json.loads(created_board_text)
    # Obtener el valor del campo 'id'
    created_board_id = created_board_dict['id']

    create_response = delete_board(api_context, created_board_id)

    # Attempt to parse JSON if status is OK
    if create_response.status == 200:
        try:
            json_data = create_response.json()
            print(json_data)
        except Exception as e:
            print(f"Failed to parse JSON: {e}")
    else:
        print("Request failed with status code:", create_response.status)     
        
@pytest.mark.skip()  
def test_delete_all_boards(api_context: APIRequestContext):
    response = delete_all_boards(api_context)
    
    print(response.body())
    
@pytest.mark.skip()  
def test_update_board(api_context: APIRequestContext):
    create_response = create_board(api_context)
    
    print(f"Status code: {create_response.status}")
    #assert(response.status==200)
    print(f"Response text: {create_response.text()}")
    
    created_board_text = create_response.text()    
    created_board_dict = json.loads(created_board_text)
    # Obtener el valor del campo 'id'
    created_board_id = created_board_dict['id']

    update_response = update_board(api_context, created_board_id)

    # Attempt to parse JSON if status is OK
    if update_response.status == 200:
        try:
            json_data = update_response.json()
            print("Board with ID: ", created_board_id, " was correctly updated!")
            print(json_data)
        except Exception as e:
            print(f"Failed to parse JSON: {e}")
    else:
        print("Request failed with status code:", update_response.status)
    
    delete_response = delete_board(api_context, created_board_id)
    
    
#@pytest.mark.skip()  
def test_get_board(api_context: APIRequestContext):  
    create_response = create_board(api_context)
    
    print(f"Status code: {create_response.status}")
    #assert(response.status==200)
    print(f"Response text: {create_response.text()}")
    
    created_board_text = create_response.text()    
    created_board_dict = json.loads(created_board_text)
    # Obtener el valor del campo 'id'
    created_board_id = created_board_dict['id']

    get_response = get_board(api_context, created_board_id)

    # Attempt to parse JSON if status is OK
    if get_response.status == 200:
        try:
            json_data = get_response.json()
            print("Board with ID: ", created_board_id, " was correctly updated!")
            print(json_data)
        except Exception as e:
            print(f"Failed to parse JSON: {e}")
    else:
        print("Request failed with status code:", get_response.status)
    
    delete_response = delete_board(api_context, created_board_id)