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
        #app.logger.info(cls)
        #app.logger.info(page_list)
        return dict(paths=dict([(x.simple_path(), dict(path=x.path(), text=x.text())) for x in page_list]))

    @classmethod
    def options(cls):
        return []

    @classmethod
    def text(cls):
        return 'Go back to the top.'

class HomePage(RoutedPage):
    @classmethod
    def path(cls):
        return '/home'

    @classmethod
    def options(cls):
        return [AboutMe, Contact]

    @classmethod
    def text(cls):
        return 'This is the home page.'

class AboutMe(RoutedPage):
    @classmethod
    def path(cls):
        return '/about_me'

    @classmethod
    def options(cls):
        return [HomePage]

    @classmethod
    def text(cls):
        return 'This page is about me.'

class Contact(RoutedPage):
    @classmethod
    def path(cls):
        return '/contact'

    @classmethod
    def options(cls):
        return [HomePage]

    @classmethod
    def text(cls):
        return 'How to contact me.'

# Logging
app.logger.addHandler(logging.StreamHandler())
app.logger.setLevel(logging.INFO)

# Auto add paths things
clsmembers = inspect.getmembers(sys.modules[__name__],
    lambda x: inspect.isclass(x) and issubclass(x, RoutedPage) and x is not RoutedPage)

for name, member in clsmembers:
    app.add_url_rule(member.path(), name.lower(), lambda: jsonify(member.options_dict()))

if __name__ == '__main__':
    app.run()
