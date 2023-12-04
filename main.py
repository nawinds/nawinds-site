import os

import requests
from flask import Flask, render_template, send_file, request, g, redirect, url_for
from flask_babel import Babel

from blueprints.multilingual import multilingual, LANGUAGES

TG_BOT_TOKEN = os.getenv("TOKEN")
TG_CHAT_ID = os.getenv("CHAT")
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")

app = Flask(__name__)
app.register_blueprint(multilingual)

babel = Babel(app)


def get_locale():
    if not g.get('lang_code', None):
        if not request.cookies.get('lang', None):
            g.lang_code = request.accept_languages.best_match(LANGUAGES)
        else:
            g.lang_code = request.cookies.get('lang')
    return g.lang_code


babel.init_app(app, locale_selector=get_locale)


@app.route('/')
def index():
    if not request.cookies.get('lang', None):
        g.lang_code = request.accept_languages.best_match(LANGUAGES)
    else:
        g.lang_code = request.cookies.get('lang')
    return redirect(url_for('multilingual.index'))


@app.route("/api/v1/stats/social-click/<site_name>")
def social_click(site_name):
    requests.get(f"https://api.telegram.org/bot{TG_BOT_TOKEN}/sendMessage?"
                 f"chat_id={TG_CHAT_ID}&text=Nawinds:%20Переход%20по%20ссылке%20на%20{site_name}")
    return "OK"


@app.route("/api/v1/projects/get_version")
def get_project_version():
    github_repo = request.args.get("github_repo")
    headers = {"Authorization": "Bearer " + GITHUB_TOKEN}
    r = requests.get(f"https://api.github.com/repos/{github_repo.strip()}/releases",
                     headers=headers)
    return r.json()[0]["name"]


@app.route("/favicon.ico")
def favicon():
    return send_file("static/icons/favicon/favicon.ico")


@app.route("/robots.txt")
def robots():
    return send_file("static/robots.txt")


@app.route("/sitemap.xml")
def sitemap():
    return send_file("static/sitemap.xml")


@app.route("/lucky")
def lucky():
    return render_template("lucky.jinja2")


@app.route("/killer")
def killer():
    return render_template("killer.jinja2")


@app.errorhandler(404)
def not_found(e):
    return render_template("error.jinja2", status_code="404", error_heading="Страница не найдена",
                           error_description="Этой страницы не существует. "
                                             "Вы можете перейти на <a href=\"/\">главную</a>."), 404


if __name__ == '__main__':
    app.run("127.0.0.1", port=5000)
