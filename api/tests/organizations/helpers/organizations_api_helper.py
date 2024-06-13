# organizations_api_helper.py

from playwright.sync_api import APIRequestContext
#from organizations_Endpoint_Constants import ORGANIZATION_ENDPOINTS
from api.tests.organizations.constants.organizations_endpoints import ORGANIZATION_ENDPOINTS

def get_all_organizations(api_context: APIRequestContext):
    org_url = ORGANIZATION_ENDPOINTS['GET_BOARDS_IN_ORGANIZATION'] + '?key=f67ad04141e131370165b7d6c17450fa&token=ATTAaa0a3e118da8914edcd7982318ee93abbfe17549c1412ef58aa220237f6ef9d6A108439D'
    
    response = api_context.get(org_url)
    return response
