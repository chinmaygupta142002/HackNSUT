from flask import Flask, render_template, request
from pymongo import MongoClient


client = MongoClient("mongodb://localhost:27017")
db = client["HackNSUT'23"]
collections = db["authentication"]

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("login.html")


@app.route("/login")
def func():
    email = request.args.get("email")
    password = request.args.get("password")
    if collections.find_one({"email": email, "password": password}):
        return "Logged In"
    return "Failed"


if __name__ == "__main__":
    app.run(debug=True)

