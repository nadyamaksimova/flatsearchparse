import telebot
from telebot import types

button_main = types.KeyboardButton('🏠 Главное меню')
button_search = types.KeyboardButton('🔍 Поиск объявлений')
button_cancel = types.KeyboardButton('❌ Отмена')
button_edit = types.KeyboardButton('✏️ Редактровать')
button_done = types.KeyboardButton('📝 Приготовить файлы')
button_district1 = types.KeyboardButton('Калининский')
button_district2 = types.KeyboardButton('Курчатовский')
button_district3 = types.KeyboardButton('Ленинский')
button_district4 = types.KeyboardButton('Металлургический')
button_district5 = types.KeyboardButton('Советский')
button_district6 = types.KeyboardButton('Тракторозаводский')
button_district7 = types.KeyboardButton('Центральный')
button_all = types.KeyboardButton('Все районы')
button_main_fake = types.KeyboardButton('🏠 Глaвнoe мeню')

main_fake = types.ReplyKeyboardMarkup(True, True)

main = types.ReplyKeyboardMarkup(True, True)

cancel = types.ReplyKeyboardMarkup(True, True)

edit_cancel = types.ReplyKeyboardMarkup(True, True)

search = types.ReplyKeyboardMarkup(True, True)

done_edit_cancel = types.ReplyKeyboardMarkup(True, True)

district_cancel = types.ReplyKeyboardMarkup(True, True)

main_fake.row(button_main_fake)

main.row(button_main)

cancel.row(button_cancel)

edit_cancel.row(button_edit)
edit_cancel.row(button_cancel)

search.row(button_search)

district_cancel.row(button_district1, button_district2)
district_cancel.row(button_district3, button_district4)
district_cancel.row(button_district5, button_district6)
district_cancel.row(button_district7, button_all)
district_cancel.row(button_cancel)

done_edit_cancel.row(button_done)
done_edit_cancel.row(button_edit)
done_edit_cancel.row(button_cancel)