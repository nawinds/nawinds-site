import datetime
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

    projects = [
        {
            "title": "Telegram бот для inline-поиска стикеров",
            "hashtags": [
                {
                    "color": "yellow",
                    "text": "#Активный"
                },
                {
                    "color": "green",
                    "text": "#В_разработке"
                },
                {
                    "color": "orange",
                    "text": "#English"
                }
            ],
            "open_link": {
                "url": "https://t.me/SSrchBot",
                "title": "Открыть бот"
            },
            "source_link": "https://github.com/nawinds/inline-stickers-search-bot",
            "github_repo": "nawinds/inline-stickers-search-bot",
            "description": [
                "<p>Бот для поиска стикеров в инлайн-режиме. Описания всем стикерам пользователи задают сами "
                "и поиск осуществляется по этим описаниям.</p>"
                "<ul><li>При поиске могут быть исправлены раскладка клавиатуры и опечатки</li>"
                "<li>Описания к стикерам объединяются в отдельные множества стикеров. Этими множествами "
                "можно делиться с другими пользователями</li>"
                "<li>В последующих версиях будет добавлена функция избранных стикеров (при пустом поисковом "
                "запросе)</li></ul>"
            ]
        },
        {
            "title": "Private-Net.work Notes",
            "hashtags": [
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
            "github_repo": "Private-Net-work/Private-Net.work-site",
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
                    "color": "yellow",
                    "text": "#Активный"
                },
                {
                    "color": "green",
                    "text": "#Завершённый"
                }
            ],
            "source_link": "https://github.com/nawinds/nawinds-site",
            "github_repo": "nawinds/nawinds-site",
            "description": ["<p>Этот сайт :)</p>",
                            "<p>Бэкенд написан на Python с использованием фреймворка Flask, а фронтенд "
                            "написан вручную без использования каких-либо библиотек.</p>"]
        },
        {
            "title": "Telegram бот для мониторинга сервисов systemd",
            "hashtags": [
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
            "github_repo": "nawinds/systemd_services_monitoring",
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
                    "color": "red",
                    "text": "#Разработка_приостановлена"
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
                            "оплатой <a href='https://git.nawinds.top/nawinds/order_tg_bot/src/branch/"
                            "feature/db_models' target='_blank'>здесь</a>.</p>"]
        }
    ]

    return render_template("index.jinja2",
                           sail_images=sail_images, age=age, year=today.year,
                           gitea=gitea, github=github, telegram=telegram,
                           instagram=instagram, vk=vk, email=email,
                           projects=projects)
