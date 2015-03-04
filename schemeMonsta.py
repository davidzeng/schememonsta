from copy import copy
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
    def simple_path(cls):
        return cls.path()[1:] # remove the beginning slash

    @classmethod
    def options_dict(cls):
        page_list = cls.options()
        return dict(paths=dict([(x.simple_path(), dict(path=x.path(), text=x.description())) for x in page_list]),
                    page_text=cls.page_text(), page_json=cls.page_json())

    @classmethod
    def options(cls):
        return []

    @classmethod
    def description(cls):
        # what's shown to the users in the options page.
        return 'Go back to the top.'

    @classmethod
    def page_text(cls):
        # what's displayed as text on the page.
        return ''

    @classmethod
    def page_json(cls):
        # dictionary that'll get pretty printed into JSON
        return dict()

class HomePage(RoutedPage):
    @classmethod
    def path(cls):
        return '/home'

    @classmethod
    def options(cls):
        return [AboutMe, Contact]

    @classmethod
    def description(cls):
        return 'This is the home page.'

class AboutMe(RoutedPage):
    @classmethod
    def path(cls):
        return '/about_me'

    @classmethod
    def options(cls):
        return [HomePage]

    @classmethod
    def description(cls):
        return 'This page is about me.'

    @classmethod
    def page_text(cls):
        line1 = "My name is David Zeng and I am a software engineer currently working at Clinkle."
        line2 = "I specialize in working on the backend, designing API's and working on general architecture."
        return '<br/>'.join([line1, line2])

class Contact(RoutedPage):
    @classmethod
    def path(cls):
        return '/contact'

    @classmethod
    def options(cls):
        return [HomePage]

    @classmethod
    def description(cls):
        return 'How to contact me.'

    @classmethod
    def page_text(cls):
        return "Here's a list of the ways you can contact me:"

    @classmethod
    def page_json(cls):
        return dict(email='david.tao.zeng@gmail.com',
                    linkedin='https://www.linkedin.com/pub/david-zeng/9/a22/14a',
                    github='https://github.com/davidzeng')

# Logging
app.logger.addHandler(logging.StreamHandler())
app.logger.setLevel(logging.INFO)

# Auto add paths things
clsmembers = inspect.getmembers(sys.modules[__name__],
    lambda x: inspect.isclass(x) and issubclass(x, RoutedPage) and x is not RoutedPage)

# Read this on why I did this:
# https://docs.python.org/3/faq/programming.html#why-do-lambdas-defined-in-a-loop-with-different-values-all-return-the-same-result
view_maker = lambda name: (lambda: jsonify(name))

for name, member in clsmembers:
    app.add_url_rule(member.path(), endpoint=name.lower(),
                     view_func=crossdomain('*')(view_maker(member.options_dict())))

if __name__ == '__main__':
    app.run()
