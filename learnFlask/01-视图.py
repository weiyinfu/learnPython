from flask import Flask

from flask.views import View, MethodView


class MyView(View):
    """
    在视图中可以添加各种模板进行渲染
    """

    def dispatch_request(self):
        rendered = f"""
<html>
<head></head>
<body>
<h1>天下大势为我所控</h1>
</body>
</html>
"""
        return rendered


class MyMethodView(MethodView):
    def get(self):
        return "get method"

    def post(self):
        return "post method"


app = Flask(__name__)

app.add_url_rule('/', view_func=MyView.as_view('myview'))
app.add_url_rule('/method_view', view_func=MyMethodView.as_view('method_view'))
if __name__ == "__main__":
    app.run()
