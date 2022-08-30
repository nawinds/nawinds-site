from flask import Flask, render_template, send_file
import datetime
import requests
import os


app = Flask(__name__)

B_DAY = int(os.getenv("B_DAY"))
B_MONTH = int(os.getenv("B_MONTH"))
B_YEAR = int(os.getenv("B_YEAR"))
TG_BOT_TOKEN = os.getenv("TOKEN")
TG_CHAT_ID = os.getenv("CHAT")


@app.route("/")
def index():
    sail_images = os.listdir("static/sail/")

    today = datetime.date.today()
    age = today.year - B_YEAR
    birthday = datetime.date(today.year, B_MONTH, B_DAY)
    if today < birthday:
        age -= 1

    telegram = "nawinds"
    github = "nawinds"
    instagram = "nawinds"
    vk = "nawinds"
    email = "me@nawinds.top"

    return render_template("index.jinja2", sail_images=sail_images, age=age,
                           telegram=telegram, github=github, instagram=instagram,
                           vk=vk, email=email, year=today.year)


@app.route("/api/v1/stats/social-click/<site_name>")
def social_click(site_name):
    requests.get(f"https://api.telegram.org/bot{TG_BOT_TOKEN}/sendMessage?"
                 f"chat_id={TG_CHAT_ID}&text=Nawinds:%20Переход%20по%20ссылке%20на%20{site_name}")
    return "OK"


@app.route("/favicon.ico")
def favicon():
    return send_file("static/icons/favicon/favicon.ico")


@app.route("/robots.txt")
def robots():
    return send_file("static/robots.txt")


def not_found(e):
    return render_template("error.jinja2", status_code="404", error_heading="Страница не найдена",
                           error_description="Этой страницы не существует. "
                                             "Вы можете перейти на <a href=\"/\">главную</a>."), 404


app.register_error_handler(404, not_found)


if __name__ == '__main__':
    app.run("0.0.0.0", port=80)
