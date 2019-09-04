from flask import FLASK

app = Flask(__name__)


@app.route("/")
def test():
    return '<h1>Deployed on Heroku !</h1>'


