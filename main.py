import requests as req
from file.example import _exam_resp

_token = 'UokPEWhb7Gjf2hrqjRv_FlHOzWPSViPG'

def get_request(path:str, limit:int = -1, token:str = None):
    """делаем запрос"""
    url = f'https://api.simplify-bots.com/items/{path}?limit={limit}'
    if token:
        url = url + f'&access_token={token}'
    print(url)
    return req.get(url)


def response_handler(resp = None):
    """обрабатываем запрос"""
    if _exam_resp["data"]:
    # if resp:
        for d in _exam_resp["data"]:
            print( d)

if __name__ == '__main__':
    # настоящий запрос
    # resp = get_request('routes_level_up_bot', 2, _token)
    # response_handler(resp)

    # заглушка
    response_handler()


