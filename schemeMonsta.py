from copy import copy
import logging
import inspect
import sys

from crossdomain import crossdomain
from flask import Flask, jsonify

from api import contact, home, me
from api.base_page import RoutedPage

app = Flask(__name__)

# Logging
app.logger.addHandler(logging.StreamHandler())
app.logger.setLevel(logging.INFO)

api_modules = [contact, home, me]
clsmembers = set([cls for mod in api_modules 
                    for cls in inspect.getmembers(mod, 
                        lambda x: inspect.isclass(x) and issubclass(x, RoutedPage) and x is not RoutedPage)])

app.logger.info(clsmembers)

# Read this on why I did this:
# https://docs.python.org/3/faq/programming.html#why-do-lambdas-defined-in-a-loop-with-different-values-all-return-the-same-result
view_maker = lambda name: (lambda: jsonify(name))

for name, member in clsmembers:
    app.add_url_rule(member.path(), endpoint=name.lower(),
                     view_func=crossdomain('*')(view_maker(member.options_dict())))

if __name__ == '__main__':
    app.run()
