import time
import requests
from .service_auth import get_auth_token


def get_with_retry(url, headers=None, retries=5):
    if headers.get('Authorization') is None:
        headers = add_token_to_headers(url, headers)
    response = requests.post(url=url,
                             headers=headers)
    data = {'url': url, 'headers': headers, 'retries': retries}
    return handle_response(response, data, post_with_retry)


def post_with_retry(url, headers=None, json=None, retries=5):
    if headers.get('Authorization') is None:
        headers = add_token_to_headers(url, headers)
    response = requests.post(url=url,
                             headers=headers,
                             json=json)
    data = {'url': url, 'headers': headers, 'json': json, 'retries': retries}
    return handle_response(response, data, post_with_retry)


def add_token_to_headers(url, headers=None):
    if headers is None:
        headers = {}
    token = get_auth_token(url)
    headers['Authorization'] = f'Bearer: {token}'
    return headers


def handle_response(response, data, func):
    if response.status_code == 429:
        if data['retries'] > 1:
            response = func(**data)
            time.sleep(1)
    return response


