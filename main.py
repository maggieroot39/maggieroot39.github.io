from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/proj")
def projects():
    return render_template("projects.html")

@app.route("/podcast")
def podcast():
    return render_template("podcast.html")

@app.route("/gallery")
def gallery():
    return render_template("gallery.html")

@app.route("/restaurants")
def restaurants():
    return render_template("restaurants.html")

@app.route("/game")
def game():
    return "TO BE ADDED"

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)