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

    gitea = "https://git.nawinds.top/nawinds"
    telegram = "nawinds"
    github = "nawinds"
    instagram = "nawinds"
    vk = "nawinds"
    email = "me@nawinds.top"

    projects = [
        {
            "title": "Private-Net.work Notes",
            "hashtags": [
                {
                    "color": "white",
                    "text": "v2.1.2"
                },
                {
                    "color": "yellow",
                    "text": "#Активный"
                },
                {
                    "color": "green",
                    "text": "#Завершённый"
                },
                {
                    "color": "orange",
                    "text": "#English"
                }
            ],
            "open_link": {
                "url": "https://private-net.work",
                "title": "Открыть сайт"
            },
            "source_link": "https://github.com/Private-Net-work/Private-Net.work-site",
            "description": [
                "<p>Сайт, который поможет скрыть самые приватные данные от просмотра "
                "третьими лицами при передаче собеседнику.</p>",
                "<p>Вместо того чтобы отправлять чувствительные к перехвату данные в "
                "открытом виде в мессенджерах, отправляйте собеседнику ссылку на "
                "одноразовую записку, сгенерированную этим сайтом. "
                "После первого просмотра записки по ссылке, "
                "она удаляется на нашем сервере. Если Ваш собеседник первым откроет записку, "
                "после него уже никто не сможет узнать, что в ней было. "
                "А если кто-то прочитает записку вперёд собеседника, "
                "то он, как минимум, об этом узнает, когда не сможет её открыть.</p>"
            ]
        },
        {
            "title": "Сайт nawinds.top",
            "hashtags": [
                {
                    "color": "white",
                    "text": "v1.1.0"
                },
                {
                    "color": "yellow",
                    "text": "#Активный"
                },
                {
                    "color": "green",
                    "text": "#Завершённый"
                }
            ],
            "source_link": "https://github.com/nawinds/nawinds-site",
            "description": ["<p>Этот сайт :)</p>",
                            "<p>Бэкенд написан на Python с использованием фреймворка Flask, а фронтенд "
                            "написан вручную без использования каких-либо библиотек.</p>"]
        },
        {
            "title": "Telegram бот для мониторинга сервисов systemd",
            "hashtags": [
                {
                    "color": "white",
                    "text": "v1.0.0"
                },
                {
                    "color": "yellow",
                    "text": "#Активный"
                },
                {
                    "color": "green",
                    "text": "#Завершённый"
                },
                {
                    "color": "blue",
                    "text": "#Для_программистов"
                },
                {
                    "color": "orange",
                    "text": "#English"
                }
            ],
            "source_link": "https://github.com/nawinds/systemd_services_monitoring",
            "description": ["<p>Telegram бот для мониторинга и управления сервисами systemd на сервере.</p>",
                            "<p>Реализованные функции:</p>",
                            "<ul style='margin-bottom:0'>"
                            "<li>Список статусов UP/DOWN для всех сервисов</li>"
                            "<li>Получение файла логов для выбранного сервиса (journalctl)</li>"
                            "<li>Выполнение systemctl команд start, stop, restart, status прямо из бота</li>"
                            "<li>Уведомления о падениях сервисов и возобновлениях их работы</li>"
                            "<li>Автоматический перезапуск упавших сервисов</li></ul>"]
        },
        {
            "title": "Telegram бот EAS",
            "hashtags": [
                {
                    "color": "white",
                    "text": "v1.0.0"
                },
                {
                    "color": "yellow",
                    "text": "#Активный"
                },
                {
                    "color": "green",
                    "text": "#В_разработке"
                }
            ],
            "open_link":
                {
                    "url": "https://t.me/EASPoizon_bot",
                    "title": "Открыть бота"
                },
            "source_link": "https://git.nawinds.top/nawinds/order_tg_bot",
            "description": ["<p>Telegram бот для совершения заказов на доставку товаров.</p>",
                            "<p>В версии 1.0.0 бота реализованы функции просмотра информации о компании "
                            "и подсчёта суммы заказа в соответствии с установленным администраторами курсом.</p>",
                            "<p>Вы можете посмотреть незавершённую версию бота с корзиной, оформлением заказа и "
                            "оплатой <a href='' target='_blank'>здесь</a>.</p>"]
        }
    ]

    return render_template("index.jinja2",
                           sail_images=sail_images, age=age, year=today.year,
                           gitea=gitea, github=github, telegram=telegram,
                           instagram=instagram, vk=vk, email=email,
                           projects=projects)


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
    app.run("0.0.0.0", port=80)
