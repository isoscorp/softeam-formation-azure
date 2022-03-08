from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/')
def hello():
    items = [
        {"item": "item_1"},
        {"item": "item_2"},
    ]
    return jsonify(items)


app.run(port=80)
