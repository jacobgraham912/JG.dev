# routes/general.py
from flask import Blueprint, render_template

general_routes = Blueprint("general_routes", __name__)

@general_routes.route("/")
def index():
    return render_template("index.html")

@general_routes.route("/projects")
def projects():
    return render_template("projects.html")

@general_routes.route("/about")
def about():
    return render_template("about.html")

@general_routes.route("/resume")
def resume():
    return render_template("resume.html")
