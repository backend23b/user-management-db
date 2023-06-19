from telegram import Update
from telegram.ext import CallbackContext

# import db
from db import DB

# create db obj
db = DB('db.json')


def start(update: Update, context: CallbackContext):
    # add user into database
    user = update.effective_user
    output = db.add_user(
        user_id=user.id,
        firstname=user.first_name,
        lastname=user.last_name,
        username=user.username
    )

    # send welcome message
    if output == False:
        update.message.reply_html(
            text=f'<b>Hi {user.first_name}</b>\n\nWelcome back!'
        )
    if output == True:
        update.message.reply_html(
            text=f'<b>Hello {user.first_name}</b>\n\nWelcome to our bot!'
        )
