import logging
import inspect
import sys

from crossdomain import crossdomain
from flask import Flask, jsonify

app = Flask(__name__)

class RoutedPage:
    @classmethod
    def path(cls):
        return NotImplementedError

    @classmethod
    def back_page(cls):
        return None

    @classmethod
    def options_dict(cls):
        page_list = cls.options() + [cls]
        return dict(paths=[(x.path(), x.text()) for x in page_list])

    @classmethod
    def options(cls):
        return []

    @classmethod
    def text(cls):
        return 'Go back to the top.'

class HomePage(RoutedPage):
    @classmethod
    def path(cls):
        return "/home"

    @classmethod
    def options(cls):
        return [AboutMe]

    @classmethod
    def text(cls):
        return 'This is the home page.'

class AboutMe(RoutedPage):
    @classmethod
    def path(cls):
        return "/about_me"

    @classmethod
    def back_page(cls):
        return AboutMe

    @classmethod
    def options(cls):
        return [HomePage]

    @classmethod
    def text(cls):
        return 'This page is about me.'

@app.route("/")
@crossdomain(origin='*')
def main_page():
    app.logger.info('home stuff')
    test_dict = dict(paths=dict(foo='/foo', bar="/bar"))
    return jsonify(**test_dict)

@app.route("/foo")
@crossdomain(origin='*')
def foo():
    test_dict = dict(paths=dict(main="/", bar="/bar"))
    return jsonify(**test_dict)

@app.route("/bar")
@crossdomain(origin='*')
def bar():
    test_dict = dict(paths=dict(main="/", foo="/foo"))
    return jsonify(**test_dict)

app.route("/test")(lambda: jsonify(dict(a=1)))

# Logging
app.logger.addHandler(logging.StreamHandler())
app.logger.setLevel(logging.INFO)

# Auto add paths things
clsmembers = inspect.getmembers(sys.modules[__name__],
    lambda x: inspect.isclass(x) and issubclass(x, RoutedPage) and x is not RoutedPage)
for name, member in clsmembers:
    app.add_url_rule(member.path(), name.lower(), lambda: jsonify(member.options_dict()))

if __name__ == "__main__":
    app.run()
