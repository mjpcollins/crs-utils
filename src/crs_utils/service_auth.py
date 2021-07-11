import os
import requests
from subprocess import PIPE, Popen


def get_auth_token(url):
    if os.getenv("CLOUD", "False") == "True":
        return get_service_to_service_token(url)
    return get_local_auth_token()


def get_local_auth_token():
    pipe = Popen(args=['gcloud', 'auth', 'print-identity-token'],
                 shell=True,
                 stdout=PIPE,
                 stderr=PIPE)
    raw = pipe.stdout.read()
    decoded = raw.decode('utf-8')
    token = decoded.replace('\n', '')
    return token


def get_service_to_service_token(url):
    token_url = f'http://metadata/computeMetadata/v1/instance/service-accounts/default/identity?audience={url}'
    token_request_headers = {'Metadata-Flavor': 'Google'}
    token_response = requests.get(url=token_url,
                                  headers=token_request_headers)
    token = token_response.content.decode("utf-8")
    return token


