import random

#importi potrebni za response i cookies:
from flask import Flask, render_template, request, make_response

#importi potrebni za db:
from flask import redirect, url_for
from sqla_wrapper import SQLAlchemy

app = Flask(__name__)


@app.route("/", methods=["GET"])
def index():
    secret_number = request.cookies.get("secret_number")  # check if there is already a cookie named secret_number

    response = make_response(render_template("index.html"))
    if not secret_number:  # if not, create a new cookie
        new_secret = random.randint(1, 30)
        response.set_cookie("secret_number", str(new_secret))

    return response


@app.route("/result", methods=["POST"])
def result():
    guess = int(request.form.get("guess"))
    secret_number = int(request.cookies.get("secret_number"))

    if guess == secret_number:
        message = "Correct! The secret number is {0}".format(str(secret_number))
        response = make_response(render_template("result.html", message=message))
        response.set_cookie("secret_number", str(random.randint(1, 30)))  # set the new secret number
        return response
    elif guess > secret_number:
        message = "Your guess is not correct... try something smaller."
        return render_template("result.html", message=message)
    elif guess < secret_number:
        message = "Your guess is not correct... try something bigger."
        return render_template("result.html", message=message)

@app.route("/simple_db")
def db():
    return render_template("simple_db.html")

@app.route("/add-message", methods=["POST"])
def add_message():
    username = request.form.get("username")
    text = request.form.get("text")

    print("{0}: {1}".format(username, text))

    return redirect("/")


#ovaj dio koda se dotice db.

db = SQLAlchemy("sqlite:///db.sqlite")


class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    author = db.Column(db.String, unique=False)
    text = db.Column(db.String, unique=False)


db.create_all()

if __name__ == '__main__':
    app.run(use_reloader=True)  # if you use the port parameter, delete it before deploying to Heroku