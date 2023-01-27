import requests
from os.path import *

host = 'http://127.0.0.1:1239'
fp = abspath(__file__)


def upload_one():
    file = {'file': open(fp, 'rb')}
    resp = requests.post(url=f"{host}/api/upload_one", files=file)
    print(resp.json())


def upload_two():
    resp = requests.post(url=f"{host}/api/upload_two", params={'username': 'wieyinfu'}, files={'f': open(fp, 'rb')})
    print(resp.json())


def upload_three():
    resp = requests.post(url=f"{host}/api/upload_three", data={'username': 'wieyinfu'}, files={'f': open(fp, 'rb')})
    print(resp.json())


# upload_one()
# upload_two()
upload_three()
