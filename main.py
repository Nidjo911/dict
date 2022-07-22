from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/about")
def aa():
    return render_template("about.html")

@app.route("/questions")
def bb():
    return render_template("questions.html")

if __name__ == '__main__':
    app.run(use_reloader=True)