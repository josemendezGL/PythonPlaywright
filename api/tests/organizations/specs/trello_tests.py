import pytest
from playwright.sync_api import Playwright, APIRequestContext
from api.tests.organizations.helpers.organizations_api_helper import get_all_organizations

@pytest.fixture
def api_context(playwright: Playwright) -> APIRequestContext:
    api_context = playwright.request.new_context(
        base_url="https://api.trello.com/1/",
        extra_http_headers={'Content-Type': 'application/json'},
    )
    yield api_context
    api_context.dispose()

def test_get_all_organizations(api_context: APIRequestContext):
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
