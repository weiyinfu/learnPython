import json

import flask
from flask import request

app = flask.Flask(__name__)


@app.route("/api/sum", methods=['POST'])
def get():
    content=request.get_data(as_text=True)
    print(content)
    form = json.loads(content)
    a, b = form['a'], form['b']
    return str(a + b)


if __name__ == '__main__':
    app.run()
