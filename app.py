from flask import Flask, render_template, request, url_for, redirect, session, flash
import json

app = Flask(__name__)
app.config["SECRET_KEY"] = "key" # key to sign cookie

# def current_user():
    # current user data for the session

@app.errorhandler(404)
def page_not_found():
    return render_template('404.html'), 404

@app.route("/", methods=["GET", "POST"])
def login():
    # user login page
    return render_template("index.html")

@app.route("/certificates", methods=["GET", "POST"])
def certificates():
    # main page displaying all certificates
    user = current_user()
    return render_template("certificates.html")

@app.route("/certificates/user_view", methods=["GET"])
def user_view():
    # user is only allowed to view general certificate data
    return render_template("cert_user_view.html")

@app.route("/certificates/admin_view", methods=["GET"])
def admin_view():
    # admin is allowed to view full certificate data; upload, modify or delete certificates
    return render_template("cert_admin_view.html")


if __name__ == "__main__":
    app.run(debug=True, port=5050)