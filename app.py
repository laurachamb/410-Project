
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("index.html")
# split up pages by metric
@app.route("/followers")
def followers():
    #eventually when we have interfaces, we can plug in variables to fill out our tables
    return render_template("followers.html")


@app.route("/likes")
def likes():
    #eventually when we have interfaces, we can plug in variables to fill out our tables
    return render_template("likes.html")

@app.route("/impressions")
def impressions():
    #eventually when we have interfaces, we can plug in variables to fill out our tables
    return render_template("impressions.html")