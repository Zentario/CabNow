from flask import Flask

app = Flask(__name__)


@app.route("/")
def test():
    return '<h1>Deployed on Heroku !</h1><h3>SE Project</h3>'


