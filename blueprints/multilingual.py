import datetime
import json
import os

from flask import render_template, Blueprint, g

B_DAY = int(os.getenv("B_DAY"))
B_MONTH = int(os.getenv("B_MONTH"))
B_YEAR = int(os.getenv("B_YEAR"))

multilingual = Blueprint('multilingual', __name__, url_prefix='/<lang_code>')


@multilingual.url_defaults
def add_language_code(endpoint, values):
    values.setdefault('lang_code', g.lang_code)


@multilingual.url_value_preprocessor
def pull_lang_code(endpoint, values):
    g.lang_code = values.pop('lang_code')


@multilingual.route('/')
def index():
    sail_images = os.listdir("static/sail/")

    today = datetime.date.today()
    age = today.year - B_YEAR
    birthday = datetime.date(today.year, B_MONTH, B_DAY)
    if today < birthday:
        age -= 1

    gitea = "https://git.nawinds.top/nawinds"
    telegram = "nawinds"
    github = "nawinds"
    instagram = "nawinds"
    vk = "nawinds"
    email = "me@nawinds.top"

    with open("projects.json", "r", encoding="UTF-8") as fcc_file:
        projects = json.load(fcc_file)

    return render_template("index.jinja2",
                           sail_images=sail_images, age=age, year=today.year,
                           gitea=gitea, github=github, telegram=telegram,
                           instagram=instagram, vk=vk, email=email,
                           projects=projects)
