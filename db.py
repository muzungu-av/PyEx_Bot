import requests as req
from config import DB_TOKEN
from file.example import _exam_resp

def get_request(path:str, limit:int = -1, token:str = None):
    """делаем запрос"""
    url = f'https://api.simplify-bots.com/items/{path}?limit={limit}'
    if token:
        url = url + f'&access_token={token}'
    print(url)
    return req.get(url)


def response_handler(resp = None):
    """обрабатываем запрос"""
    # if _exam_resp["data"]:
    if resp:
        for d in _exam_resp["data"]:
            print( d)
