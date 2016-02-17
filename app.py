# coding: utf-8

from datetime import datetime

from flask import Flask
from flask import render_template, request
import logging
import telegram
from token import token

# from views.todos import todos_view

app = Flask(__name__)
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# 动态路由
# app.register_blueprint(todos_view, url_prefix='/todos')
global bot
bot = telegram.Bot(token=token)

@app.route('/')
def index():
    return r'{"drakeet":"hehe"}'


@app.route('/<token>', methods=['POST'])
def echo(token):
    if request.method == "POST":
        update = telegram.Update.de_json(request.get_json(force=True))
        chat_id = update.message.chat.id
        # Telegram understands UTF-8, so encode text for unicode compatibility
        text = update.message.text.encode('utf-8')
        if '/echo ' in text:
            text = text[6:]
        # repeat the same message back (echo)
        bot.sendMessage(chat_id=chat_id, text=text)
    return 'ok'
