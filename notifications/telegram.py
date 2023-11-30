import os

from dotenv import load_dotenv
from telegram import Update
from telegram.ext import CallbackContext, Updater, ConversationHandler, CommandHandler, CallbackQueryHandler

from notifications.keyboards import main_menu_keyboard, future_lessons_keyboard

(
    ROLE,
    FUTURE_LESSONS,
) = range(2)


def start(update: Update, context: CallbackContext):
    keyboard = main_menu_keyboard()
    update.message.reply_text(
        'Привет, что ты хочешь сделать?',
        reply_markup=keyboard
    )
    return ROLE


def main_menu(update: Update, context: CallbackContext):
    query = update.callback_query
    keyboard = main_menu_keyboard()
    query.edit_message_reply_markup(keyboard)
    return FUTURE_LESSONS


def get_future_lessons(update: Update, context: CallbackContext):
    query = update.callback_query
    keyboard = future_lessons_keyboard()
    query.edit_message_reply_markup(keyboard)
    return FUTURE_LESSONS


def get_todays_lessons(update: Update, context: CallbackContext):
    query = update.callback_query
    message = "Сегодня урок в 12:45 МСК"
    keyboard = future_lessons_keyboard()
    query.edit_message_text(
        message,
        reply_markup=keyboard
    )
    return FUTURE_LESSONS


def start_bot():
    load_dotenv()
    token = os.getenv('TELEGRAM_TOKEN')
    updater = Updater(token=token)
    dispatcher = updater.dispatcher
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],
        states={
            ROLE:
                [
                    CallbackQueryHandler(get_future_lessons, pattern='future_lessons'),
                ],
            FUTURE_LESSONS:
                [
                    CallbackQueryHandler(get_todays_lessons, pattern='today'),
                ]
        },
        fallbacks=[
            CommandHandler('rerun', start),
            CommandHandler('start', start)
        ]
    )
    dispatcher.add_handler(conv_handler)

    updater.start_polling()
    updater.idle()
