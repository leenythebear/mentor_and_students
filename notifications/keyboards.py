from telegram import InlineKeyboardButton, InlineKeyboardMarkup


def main_menu_keyboard():
    keyboard = [[
        InlineKeyboardButton("Ближайшие занятия", callback_data='future_lessons'),
        InlineKeyboardButton("Прошедшие занятия", callback_data='past_lessons'),
    ]]
    return InlineKeyboardMarkup(keyboard)


def future_lessons_keyboard():
    keyboard = [[InlineKeyboardButton("Посмотреть уроки сегодня", callback_data='today')],
                [InlineKeyboardButton("Посмотреть уроки завтра", callback_data='tomorrow')],
                [InlineKeyboardButton("Посмотреть уроки послезавтра", callback_data='2_days')],
                [InlineKeyboardButton("Главное меню", callback_data="main_menu")]]

    return InlineKeyboardMarkup(keyboard)


def lessons_keyboard(lessons):
    keyboard = [[
        InlineKeyboardButton(
            f"{lesson.time} - {lesson.student.first_name} {lesson.student.last_name}",
            callback_data=f"{lesson.pk}")
    ] for lesson in lessons]
    keyboard.append([InlineKeyboardButton("Назад", callback_data="future_lessons")])
    return InlineKeyboardMarkup(keyboard)
