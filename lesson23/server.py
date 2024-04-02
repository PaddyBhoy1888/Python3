from flask import Flask, render_template, request
from weather import get_current_weather
# from waitress import serve

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    return render_template('Hello World')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
    # serve(app, host="0.0.0.0", port=8000)
