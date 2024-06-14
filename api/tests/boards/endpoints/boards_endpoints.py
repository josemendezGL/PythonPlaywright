#from boards_endpoints_constants import BoardsEndpointsConstants
from api.tests.boards.constants.boards_constants import BOARDS_ENDPOINTS

def get_board_by_id(board_id):
        return BOARDS_ENDPOINTS.GET_BOARD.format(boardId=board_id)

def update_board_by_id(board_id):
        return BOARDS_ENDPOINTS.PUT_BOARD.format(boardId=board_id)

def delete_board_by_id(board_id):
        return BOARDS_ENDPOINTS.DELETE_BOARD.format(boardId=board_id)
