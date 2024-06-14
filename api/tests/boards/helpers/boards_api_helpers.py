import requests
from playwright.sync_api import APIRequestContext
#from boards_endpoints import BoardsEndpoints
#from boards_endpoints_constants import BoardsEndpointsConstants
from api.tests.boards.constants.boards_constants import BOARDS_ENDPOINTS
from api.tests.organizations.helpers.organizations_api_helper import get_all_organizations
import json
from api.tests.organizations.constants.organizations_endpoints import ORGANIZATION_ENDPOINTS
from api.tests.boards.endpoints.boards_endpoints import delete_board_by_id
import urllib.parse

API_KEY = 'f67ad04141e131370165b7d6c17450fa'
TOKEN = 'ATTAaa0a3e118da8914edcd7982318ee93abbfe17549c1412ef58aa220237f6ef9d6A108439D'

def create_board(api_context: APIRequestContext):
    create_board_url = BOARDS_ENDPOINTS["POST_BOARD"] + '?key=f67ad04141e131370165b7d6c17450fa&token=ATTAaa0a3e118da8914edcd7982318ee93abbfe17549c1412ef58aa220237f6ef9d6A108439D'
        
    request_body = {"name": "My Board (API)"}

    response = api_context.post(create_board_url, data=request_body)
    return response

def delete_board(api_context: APIRequestContext, board_id):
    base_url = 'https://api.trello.com/1/'

    # Construir la URL completa con el endpoint y los parámetros
    delete_board_url = urllib.parse.urljoin(base_url, BOARDS_ENDPOINTS["DELETE_BOARD"].format(boardId=board_id))
    delete_board_url += f'?key={API_KEY}&token={TOKEN}'

    print("Current URL:", delete_board_url)
    response = api_context.delete(delete_board_url)
    
    print(f"Status code: {response.status}")
    print(f"Response text: {response.text()}")
    
    # Intentar analizar JSON si el estado es OK
    if response.status == 200:
        try:
            json_data = response.json()
            print(json_data)
        except Exception as e:
            print(f"Failed to parse JSON: {e}")
    else:
        print("Request failed with status code:", response.status)
    
    return response    
    
    
def delete_all_boards(api_context: APIRequestContext):
    # Obtain all boards in organization
    base_url = 'https://api.trello.com/1/'
    all_boards_in_organization = ORGANIZATION_ENDPOINTS['GET_BOARDS_IN_ORGANIZATION'] + '?key=f67ad04141e131370165b7d6c17450fa&token=ATTAaa0a3e118da8914edcd7982318ee93abbfe17549c1412ef58aa220237f6ef9d6A108439D'
    all_boards_response = api_context.get(all_boards_in_organization)
    
    if all_boards_response.status != 200:
        print(f"Failed to fetch boards. Status code: {all_boards_response.status}")
        return
    
    boards_data = all_boards_response.json()
    
    for board in boards_data:
        board_id = board['id']
        
        response = delete_board(api_context, board_id)
        print(f"Deleted board with ID {board_id}. Status code: {response.status}")
    
    return response