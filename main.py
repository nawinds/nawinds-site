import os

import requests
from flask import Flask, render_template, send_file, request, g, redirect, url_for
from flask_babel import Babel, _

from blueprints.multilingual import multilingual, LANGUAGES

TG_BOT_TOKEN = os.getenv("TOKEN")
TG_CHAT_ID = os.getenv("CHAT")
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")

app = Flask(__name__)
app.register_blueprint(multilingual)

babel = Babel(app)


def get_locale():
    if g.get('lang_code', None) not in LANGUAGES:
        if request.cookies.get('lang', None) not in LANGUAGES:
            if not request.accept_languages.best_match(LANGUAGES):
                ip_country = request.headers.get("CF-IPCountry")
                g.lang_code = "ru" if ip_country == "RU" else "en"
            else:
                g.lang_code = request.accept_languages.best_match(LANGUAGES)
        else:
            g.lang_code = request.cookies.get('lang')
    return g.lang_code


babel.init_app(app, locale_selector=get_locale)


@app.route('/')
def index():
    g.lang_code = get_locale()
    return redirect(url_for('multilingual.index'))


@app.route("/api/v1/stats/social-click/<site_name>")
def social_click(site_name):
    requests.get(f"https://api.telegram.org/bot{TG_BOT_TOKEN}/sendMessage?"
                 f"chat_id={TG_CHAT_ID}&text=Nawinds:%20Переход%20по%20ссылке%20на%20{site_name}")
    return "OK"


@app.route("/api/v1/projects/get_version")
def get_project_version():
    github_repo = request.args.get("github_repo")
    headers = {"Accept": "application/vnd.github+json",
               "Authorization": "Bearer " + GITHUB_TOKEN,
               "X-GitHub-Api-Version": "2022-11-28"}
    r = requests.get(f"https://api.github.com/repos/{github_repo.strip()}/releases",
                     headers=headers)
    if not r.json():
        return "No releases for this project", 404
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
    return render_template("error.jinja2", status_code="404",
                           error_heading=_("not_found_header"),
                           error_description=_("not_found_desc")), 404


if __name__ == '__main__':
    app.run("0.0.0.0", port=5001)
