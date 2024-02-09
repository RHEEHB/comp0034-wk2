from flask import current_app as app

app = Flask(__name__)


@app.route('/')
def hello():
    return f"Hello!"
