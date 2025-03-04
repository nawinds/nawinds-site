import datetime
import json
import os

from flask import render_template, Blueprint, g, request, abort

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
    if g.lang_code not in LANGUAGES:
        abort(404)


@multilingual.route('/')
def index():
    show_new_domain_msg = request.args.get("new_domain", "0") == "1"

    sail_images = os.listdir("static/sail/")

    today = datetime.date.today()
    age = today.year - B_YEAR
    birthday = datetime.date(today.year, B_MONTH, B_DAY)
    if today < birthday:
        age -= 1

    linkedin = "https://www.linkedin.com/in/nikitaaksenov"
    telegram = "nawinds"
    github = "nawinds"
    instagram = "nawinds"
    vk = "nawinds"
    tg_channel = "https://t.me/+bNmTupyrLWlmNTAy"

    with open("projects.json", "r", encoding="UTF-8") as fcc_file:
        projects = json.load(fcc_file)

    show_switch_lang_popup = (not request.cookies.get("lang", None) and g.lang_code !=
                              request.accept_languages.best_match(LANGUAGES)
                              ) or (request.cookies.get("lang", None) and g.lang_code !=
                                    request.cookies.get("lang") and g.lang_code !=
                                    request.accept_languages.best_match(LANGUAGES))

    return render_template("index.jinja2",
                           sail_images=sail_images, age=age, year=today.year,
                           linkedin=linkedin, github=github, telegram=telegram,
                           instagram=instagram, vk=vk, tg_channel=tg_channel,
                           projects=projects, show_switch_lang_popup=show_switch_lang_popup,
                           show_new_domain_msg=show_new_domain_msg)


# @multilingual.route('/edit')
# def edit():
#     sail_images = os.listdir("static/sail/")
#
#     today = datetime.date.today()
#     age = today.year - B_YEAR
#     birthday = datetime.date(today.year, B_MONTH, B_DAY)
#     if today < birthday:
#         age -= 1
#
#     linkedin = "https://www.linkedin.com/in/nikitaaksenov"
#     telegram = "nawinds"
#     github = "nawinds"
#     instagram = "nawinds"
#     vk = "nawinds"
#     tg_channel = "https://t.me/+bNmTupyrLWlmNTAy"
#
#     with open("projects.json", "r", encoding="UTF-8") as fcc_file:
#         projects = json.load(fcc_file)
#
#     show_switch_lang_popup = (not request.cookies.get("lang", None) and g.lang_code !=
#                               request.accept_languages.best_match(LANGUAGES)
#                               ) or (request.cookies.get("lang", None) and g.lang_code !=
#                                     request.cookies.get("lang") and g.lang_code !=
#                                     request.accept_languages.best_match(LANGUAGES))
#
#     return render_template("edit.jinja2",
#                            sail_images=sail_images, age=age, year=today.year,
#                            linkedin=linkedin, github=github, telegram=telegram,
#                            instagram=instagram, vk=vk, tg_channel=tg_channel,
#                            projects=projects, show_switch_lang_popup=show_switch_lang_popup)
