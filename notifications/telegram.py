import os

from dotenv import load_dotenv
from telegram import Update
from telegram.ext import CallbackContext, Updater, ConversationHandler, CommandHandler, CallbackQueryHandler

from notifications.db_functions import get_today_lessons, get_tomorrow_lessons, get_day_after_tomorrow_lessons
from notifications.keyboards import main_menu_keyboard, future_lessons_keyboard, lessons_keyboard

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


def show_today_lessons(update: Update, context: CallbackContext):
    query = update.callback_query
    user_id = update.effective_user['id']

    today_lessons = get_today_lessons(user_id)
    keyboard = lessons_keyboard(today_lessons)
    message = "Ваши сегодняшние уроки:"

    query.edit_message_text(
        message,
        reply_markup=keyboard
    )
    return FUTURE_LESSONS


def show_tomorrow_lessons(update: Update, context: CallbackContext):
    query = update.callback_query
    user_id = update.effective_user['id']

    tomorrow_lessons = get_tomorrow_lessons(user_id)
    keyboard = lessons_keyboard(tomorrow_lessons)
    message = "Ваши завтрашние уроки:"

    query.edit_message_text(
        message,
        reply_markup=keyboard
    )
    return FUTURE_LESSONS


def show_day_after_tomorrow_lessons(update: Update, context: CallbackContext):
    query = update.callback_query
    user_id = update.effective_user['id']

    tomorrow_lessons = get_day_after_tomorrow_lessons(user_id)
    keyboard = lessons_keyboard(tomorrow_lessons)
    message = "Ваши уроки послезавтра:"

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
                    CallbackQueryHandler(main_menu, pattern='main_menu'),
                    CallbackQueryHandler(get_future_lessons, pattern='future_lessons'),
                    CallbackQueryHandler(show_today_lessons, pattern='today'),
                    CallbackQueryHandler(show_tomorrow_lessons, pattern='tomorrow'),
                    CallbackQueryHandler(show_day_after_tomorrow_lessons, pattern='2_days'),
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
