from flask import Flask
import json

app = Flask(__name__)



def read_users():
    with open('users.json', 'r') as infile:
        data = json.load(infile)
    return data

def write_users(data):
    with open('users.json', 'w') as outfile:
        json.dump(data, outfile)


def read_drivers():
    with open('drivers.json', 'r') as infile:
        data = json.load(infile)
    return data

def write_drivers(data):
    with open('drivers.json', 'w') as outfile:
        json.dump(data, outfile)


@app.route("/")
def test():
    return '<h1>Deployed on Heroku !</h1><h3>SE Project</h3>'


@app.route("/test")
def test_v1():
    return "<h1>File contents</h1><h4>" + str(read_drivers()) + "</h4>" + "<h4>" + str(read_users()) + "</h4>"


# For testing only
# if __name__ == "__main__":
#     app.run(host="127.0.0.1", port=5000, debug=True)