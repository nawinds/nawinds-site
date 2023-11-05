import datetime
import json
import os

from flask import render_template, Blueprint, g, request

B_DAY = int(os.getenv("B_DAY"))
B_MONTH = int(os.getenv("B_MONTH"))
B_YEAR = int(os.getenv("B_YEAR"))
LANGUAGES = ['en', 'ru']

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

    if (not request.cookies.get("lang", None) and g.lang_code !=
        request.accept_languages.best_match(LANGUAGES)
    ) or (request.cookies.get("lang", None) and g.lang_code !=
          request.cookies.get("lang") and g.lang_code !=
          request.accept_languages.best_match(LANGUAGES)):
        show_switch_lang_popup = True
    else:
        show_switch_lang_popup = False

    return render_template("index.jinja2",
                           sail_images=sail_images, age=age, year=today.year,
                           gitea=gitea, github=github, telegram=telegram,
                           instagram=instagram, vk=vk, email=email,
                           projects=projects, show_switch_lang_popup=show_switch_lang_popup)
