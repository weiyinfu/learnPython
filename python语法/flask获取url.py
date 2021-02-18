import flask
from flask import request

app = flask.Flask(__name__)


@app.route("/")
def get():
    return f"""
url:{request.url}
path:{request.path}
host:{request.host}
url_root:{request.url_root}
base_url:{request.base_url}
host_url:{request.host_url}
sheme:{request.scheme}
query_string:{request.query_string}
full_path:{request.full_path}
"""


app.run()
