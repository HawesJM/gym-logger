from flask import render_template, request, redirect, url_for

from gymlogger import app

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/profile")
def profile():
    return render_template("profile.html")
