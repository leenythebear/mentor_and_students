from telegram import InlineKeyboardButton, InlineKeyboardMarkup


def main_menu_keyboard():
    keyboard = [[
        InlineKeyboardButton("Ближайшие занятия", callback_data='future_lessons'),
        InlineKeyboardButton("Прошедшие занятия", callback_data='past_lessons'),
    ]]
    return InlineKeyboardMarkup(keyboard)


def future_lessons_keyboard():
        keyboard = [
            [InlineKeyboardButton("Посмотреть уроки сегодня", callback_data='today')],
            [InlineKeyboardButton("Посмотреть уроки завтра", callback_data='tomorrow')],
            [InlineKeyboardButton("Посмотреть уроки на 3 дня", callback_data='3_days')]
                    ]

        return InlineKeyboardMarkup(keyboard)
