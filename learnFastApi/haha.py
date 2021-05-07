import requests
import json


def test1():
    resp = requests.post("http://localhost:8000/api/sum2", data=json.dumps({
        'a': 1,
        'b': 2,
    }))
    print(resp.text)


def test2():
    resp = requests.post("http://localhost:8000/api/add_later_see", data=json.dumps({
        'a': 1,
        'b': 2,
    }))
    print(resp.text)
test2()