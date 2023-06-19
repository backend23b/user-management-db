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


def users(update: Update, context: CallbackContext):
    # get all users from database
    users = db.get_all_users()

    # send users as message
    text = '<b>Available Users</b>\n\n'
    for user in users:
        text += f"{user['firstname']} {user['lastname']} - @{user['username']}\n"
    update.message.reply_html(
        text=text
    )