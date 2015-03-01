from crossdomain import crossdomain
from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
@crossdomain(origin='*')
def main():
	test_dict = dict(paths=dict(foo="/foo",
                                bar="/bar"))
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

if __name__ == "__main__":
    app.run()