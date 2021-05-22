import time
import telebot
import kb

from parsing.n1 import n1_data
from parsing.avito import avito_data
from parsing.cian import cian_data

from config import TOKEN
bot = telebot.TeleBot(TOKEN)

district = ''
room = ''
max_price = ''
min_price = ''
start_file = ''

district_n1 = ''
url_n1 = ''


district_avito = ''
url_avito = ''


district_cian = ''
url_cian = ''

# создание хэндлера старта
@bot.message_handler(commands=['start'])
def start_message(message):
	bot.send_message(message.chat.id, 'Пройди проверку на то, что ты не робот 🤖\n'
		'PS: Нажми ➡️ /main')

# создание хэндлера главное меню
@bot.message_handler(commands=['main'])
def main(message):
	bot.send_message(message.chat.id, 'Ты находишься в Главном меню, для поиска объявлений по аренде недвижимости в городе Челябинск, нажми соответствующую кнопку',
		reply_markup=kb.search)

# создание хэндлера сообщений
@bot.message_handler(content_types=['text'])
def messages(message):
	if message.text == '🏠 Главное меню':
		bot.send_message(message.chat.id, 'Ты находишься в Главном меню, для поиска объявлений по аренде недвижимости в городе Челябинск, нажми соответствующую кнопку',
			reply_markup=kb.search)

	elif message.text == '🔍 Поиск объявлений':
		bot.send_message(message.chat.id, 'Введи мне некоторые данные для поиска объявленией\n'
			'1) Выбери район, они представлены на кнопках, хочешь искать квартиры во всех районах, нажми соответствующую кнопку\n'
			'Если хочешь отменить поиск, нажми Отмена',
			reply_markup=kb.district_cancel)
		bot.register_next_step_handler(message, district_handler)

def district_handler(message):
	global district, district_n1, district_avito, district_cian
	district = message.text
	if district == '❌ Отмена':
		bot.send_message(message.chat.id, 'Ты возвращён в Главное меню, для поиска объявлений по городу Екатеринбург, нажми соответствующую кнопку',
			reply_markup=kb.search)

	elif district == 'Калининский':
		district_n1 = 'district-Kalininskiy-rayon/'
		district_avito = '&district=10'
		district_cian = '&district%5B0%5D=313'
		bot.send_message(message.chat.id, f'Ты выбрал район - {district}\n'
			'2) Пришли мне количество комнат (1-4), если вариантов несколько, то напиши мне их слитно в порядке возрастания\n\n'
			'Пример: "Хочу только однокомнатную квартиру" — 1\n'
			'Пример: "Хочу однокомнатную, двухкомнатную квартиру" — 12\n'
			'Не правильно ввёл район, нажми ✏️ Редактровать\n'
			'Если хочешь отменить поиск, нажми Отмена',
			reply_markup=kb.edit_cancel)
		bot.register_next_step_handler(message, room_handler)

	elif district == 'Курчатовский':
		district_n1 = 'district-Kurchatovskiy-rayon/'
		district_avito = '&district=11'
		district_cian = '&district%5B0%5D=312'
		bot.send_message(message.chat.id, f'Ты выбрал район - {district}\n'
			'2) Пришли мне количество комнат (1-4), если вариантов несколько, то напиши мне их слитно в порядке возрастания\n\n'
			'Пример: "Хочу только однокомнатную квартиру" — 1\n'
			'Пример: "Хочу однокомнатную, двухкомнатную квартиру" — 12\n'
			'Не правильно ввёл район, нажми ✏️ Редактровать\n'
			'Если хочешь отменить поиск, нажми Отмена',
			reply_markup=kb.edit_cancel)
		bot.register_next_step_handler(message, room_handler)

	elif district == 'Ленинский':
		district_n1 = 'district-Leninskiy-rayon/'
		district_avito = '&district=12'
		district_cian = '&district%5B0%5D=314'
		bot.send_message(message.chat.id, f'Ты выбрал район - {district}\n'
			'2) Пришли мне количество комнат (1-4), если вариантов несколько, то напиши мне их слитно в порядке возрастания\n\n'
			'Пример: "Хочу только однокомнатную квартиру" — 1\n'
			'Пример: "Хочу однокомнатную, двухкомнатную квартиру" — 12\n'
			'Не правильно ввёл район, нажми ✏️ Редактровать\n'
			'Если хочешь отменить поиск, нажми Отмена',
			reply_markup=kb.edit_cancel)
		bot.register_next_step_handler(message, room_handler)

	elif district == 'Металлургический':
		district_n1 = 'district-Metallurgicheskiy-rayon/'
		district_avito = '&district=13'
		district_cian = '&district%5B0%5D=315'
		bot.send_message(message.chat.id, f'Ты выбрал район - {district}\n'
			'2) Пришли мне количество комнат (1-4), если вариантов несколько, то напиши мне их слитно в порядке возрастания\n\n'
			'Пример: "Хочу только однокомнатную квартиру" — 1\n'
			'Пример: "Хочу однокомнатную, двухкомнатную квартиру" — 12\n'
			'Не правильно ввёл район, нажми ✏️ Редактровать\n'
			'Если хочешь отменить поиск, нажми Отмена',
			reply_markup=kb.edit_cancel)
		bot.register_next_step_handler(message, room_handler)

	elif district == 'Советский':
		district_n1 = 'district-Sovetskiy-rayon/'
		district_avito = '&district=14'
		district_cian = '&district%5B0%5D=316'
		bot.send_message(message.chat.id, f'Ты выбрал район - {district}\n'
			'2) Пришли мне количество комнат (1-4), если вариантов несколько, то напиши мне их слитно в порядке возрастания\n\n'
			'Пример: "Хочу только однокомнатную квартиру" — 1\n'
			'Пример: "Хочу однокомнатную, двухкомнатную квартиру" — 12\n'
			'Не правильно ввёл район, нажми ✏️ Редактровать\n'
			'Если хочешь отменить поиск, нажми Отмена',
			reply_markup=kb.edit_cancel)
		bot.register_next_step_handler(message, room_handler)

	elif district == 'Тракторозаводский':
		district_n1 = 'district-Traktorozavodskiy-rayon/'
		district_avito = '&district=15'
		district_cian = '&district%5B0%5D=317'
		bot.send_message(message.chat.id, f'Ты выбрал район - {district}\n'
			'2) Пришли мне количество комнат (1-4), если вариантов несколько, то напиши мне их слитно в порядке возрастания\n\n'
			'Пример: "Хочу только однокомнатную квартиру" — 1\n'
			'Пример: "Хочу однокомнатную, двухкомнатную квартиру" — 12\n'
			'Не правильно ввёл район, нажми ✏️ Редактровать\n'
			'Если хочешь отменить поиск, нажми Отмена',
			reply_markup=kb.edit_cancel)
		bot.register_next_step_handler(message, room_handler)

	elif district == 'Центральный':
		district_n1 = 'district-Centralnyi-rayon/'
		district_avito = '&district=16'
		district_cian = '&district%5B0%5D=318'
		bot.send_message(message.chat.id, f'Ты выбрал район - {district}\n'
			'2) Пришли мне количество комнат (1-4), если вариантов несколько, то напиши мне их слитно в порядке возрастания\n\n'
			'Пример: "Хочу только однокомнатную квартиру" — 1\n'
			'Пример: "Хочу однокомнатную, двухкомнатную квартиру" — 12\n'
			'Не правильно ввёл район, нажми ✏️ Редактровать\n'
			'Если хочешь отменить поиск, нажми Отмена',
			reply_markup=kb.edit_cancel)
		bot.register_next_step_handler(message, room_handler)

	elif district == 'Все районы':
		district_n1 = '&district=1306617%2C1306616%2C1306615%2C1306614%2C1306613%2C1306612%2C1306611'
		district_avito = 'district=10-11-12-13-14-15-16'
		district_cian = '&district%5B0%5D=312&district%5B1%5D=313&district%5B2%5D=314&district%5B3%5D=316&district%5B4%5D=317&district%5B5%5D=318'
		bot.send_message(message.chat.id, f'Ты выбрал все районы\n'
			'2) Пришли мне количество комнат (1-4), если вариантов несколько, то напиши мне их слитно в порядке возрастания\n\n'
			'Пример: "Хочу только однокомнатную квартиру" — 1\n'
			'Пример: "Хочу однокомнатную, двухкомнатную квартиру" — 12\n'
			'Не правильно ввёл район, нажми ✏️ Редактровать\n'
			'Если хочешь отменить поиск, нажми Отмена',
			reply_markup=kb.edit_cancel)
		bot.register_next_step_handler(message, room_handler)

	else:
		bot.send_message(message.chat.id, 'Ты вводишь не правильный район 🙃\n'
			'Нужно начать сначала, нажми Главное меню',
			reply_markup=kb.main)


def room_handler(message):
	global room, url_n1, url_avito, url_cian
	room = message.text
	if room == '❌ Отмена':
		bot.send_message(message.chat.id, 'Ты возвращён в Главное меню, для поиска объявлений по городу Челябинск, нажми соответствующую кнопку',
			reply_markup=kb.search)

	elif room == '✏️ Редактровать':
		bot.send_message(message.chat.id, 'Вижу, ты решил отредактировать район Челябинска\n'
			'1) Выбери снова район, они представлены на кнопках, хочешь искать квартиры во всех районах, нажми соответствующую кнопку\n'
			'Если хочешь отменить поиск, нажми Отмена',
			reply_markup=kb.district_cancel)
		bot.register_next_step_handler(message, district_handler)

	elif room == '1':
		url_n1 = f'https://chelyabinsk.n1.ru/search/?rubric=flats&deal_type=sell/{district_n1}&rooms=1'
		url_avito = 'https://www.avito.ru/chelyabinsk/kvartiry/prodam/1-komnatnye-ASgBAQICAUSSA8YQAUDKCBSAWQ?{district_n1}'
		url_cian = 'https://ekb.cian.ru/cat.php?deal_type=rent&engine_version=2&offer_type=flat&region=4743&room1=1&type=4&with_neighbors=0&sort=creation_date_desc'
		bot.send_message(message.chat.id, 'Ты выбрал однокомнатную квартиру!\n'
			'3) Отправь максимальную цену квартиры, валюта рубли\n'
			'Не правильно ввёл количество комнат, нажми ✏️ Редактровать\n'
			'Если хочешь отменить поиск, нажми Отмена',
			reply_markup=kb.edit_cancel)
		bot.register_next_step_handler(message, max_price_handler)

	elif room == '2':
		url_n1 = f'https://chelyabinsk.n1.ru/search/?rubric=flats&deal_type=sell/{district_n1}&rooms=2'
		url_avito = 'https://www.avito.ru/chelyabinsk/kvartiry/prodam/2-komnatnye-ASgBAQICAUSSA8YQAUDKCBSCWQ?{district_n1}'
		url_cian = 'https://ekb.cian.ru/cat.php?deal_type=rent&engine_version=2&offer_type=flat&region=4743&room2=1&type=4&with_neighbors=0&sort=creation_date_desc'
		bot.send_message(message.chat.id, 'Ты выбрал двухкомнатную квартиру!\n'
			'3) Отправь максимальную цену квартиры, валюта рубли\n'
			'Не правильно ввёл количество комнат, нажми ✏️ Редактровать\n'
			'Если хочешь отменить поиск, нажми Отмена',
			reply_markup=kb.edit_cancel)
		bot.register_next_step_handler(message, max_price_handler)

	elif room == '3':
		url_n1 = f'https://chelyabinsk.n1.ru/search/?rubric=flats&deal_type=sell/{district_n1}&rooms=3'
		url_avito = 'https://www.avito.ru/chelyabinsk/kvartiry/prodam/3-komnatnye-ASgBAQICAUSSA8YQAUDKCBSEWQ?{district_n1}'
		url_cian = 'https://ekb.cian.ru/cat.php?deal_type=rent&engine_version=2&offer_type=flat&region=4743&room3=1&type=4&with_neighbors=0&sort=creation_date_desc'
		bot.send_message(message.chat.id, 'Ты выбрал трёхкомнатную квартиру!\n'
			'3) Отправь максимальную цену квартиры, валюта рубли\n'
			'Не правильно ввёл количество комнат, нажми ✏️ Редактровать\n'
			'Если хочешь отменить поиск, нажми Отмена',
			reply_markup=kb.edit_cancel)
		bot.register_next_step_handler(message, max_price_handler)

	elif room == '4':
		url_n1 = f'https://chelyabinsk.n1.ru/search/?rubric=flats&deal_type=sell/{district_n1}&rooms=4'
		url_avito = 'https://www.avito.ru/chelyabinsk/kvartiry/prodam/4-komnatnye-ASgBAQICAUSSA8YQAUDKCBSGWQ?{district_n1}'
		url_cian = 'https://ekb.cian.ru/cat.php?deal_type=rent&engine_version=2&offer_type=flat&region=4743&room4=1&type=4&with_neighbors=0&sort=creation_date_desc'
		bot.send_message(message.chat.id, 'Ты выбрал четырёхкомнатную квартиру!\n'
			'3) Отправь максимальную цену квартиры, валюта рубли\n'
			'Не правильно ввёл количество комнат, нажми ✏️ Редактровать\n'
			'Если хочешь отменить поиск, нажми Отмена',
			reply_markup=kb.edit_cancel)
		bot.register_next_step_handler(message, max_price_handler)

	elif room == '5':
		url_n1 = f'https://chelyabinsk.n1.ru/search/?rubric=flats&deal_type=sell{district_n1}&rooms=5%2B'
		url_avito = 'https://www.avito.ru/chelyabinsk/kvartiry/prodam-ASgBAgICAUSSA8YQ?{district_n1}&f=ASgBAQICAUSSA8YQAUDKCGSKWZqsAZisAZasAZSsAYhZ'
		url_cian = 'https://ekb.cian.ru/cat.php?deal_type=rent&engine_version=2&offer_type=flat&region=4743&room4=1&type=4&with_neighbors=0&sort=creation_date_desc'
		bot.send_message(message.chat.id, 'Ты выбрал пятикомнатную квартиру!\n'
			'3) Отправь максимальную цену квартирs, валюта рубли\n'
			'Не правильно ввёл количество комнат, нажми ✏️ Редактровать\n'
			'Если хочешь отменить поиск, нажми Отмена',
			reply_markup=kb.edit_cancel)
		bot.register_next_step_handler(message, max_price_handler)

	elif room == '6':
		url_n1 = f'https://chelyabinsk.n1.ru/search/?rubric=flats&deal_type=sell{district_n1}&rooms=5%2B'
		url_avito = 'https://www.avito.ru/chelyabinsk/kvartiry/prodam-ASgBAgICAUSSA8YQ?{district_n1}&f=ASgBAQICAUSSA8YQAUDKCGSKWZqsAZisAZasAZSsAYhZ'
		url_cian = 'https://ekb.cian.ru/cat.php?deal_type=rent&engine_version=2&offer_type=flat&region=4743&room4=1&type=4&with_neighbors=0&sort=creation_date_desc'
		bot.send_message(message.chat.id, 'Ты выбрал шестикомнатную квартиру!\n'
			'3) Отправь максимальную цену квартиры, валюта рубли\n'
			'Не правильно ввёл количество комнат, нажми ✏️ Редактровать\n'
			'Если хочешь отменить поиск, нажми Отмена',
			reply_markup=kb.edit_cancel)
		bot.register_next_step_handler(message, max_price_handler)

	elif room == 'Студия':
		url_n1 = f'https://chelyabinsk.n1.ru/search/?rubric=flats&deal_type=sell{district_n1}&type=studija'
		url_avito = 'https://www.avito.ru/chelyabinsk/kvartiry/prodam/studii-ASgBAQICAUSSA8YQAUDKCBT~WA?{district_n1}'
		url_cian = 'https://ekb.cian.ru/cat.php?deal_type=rent&engine_version=2&offer_type=flat&region=4743&room4=1&type=4&with_neighbors=0&sort=creation_date_desc'
		bot.send_message(message.chat.id, 'Ты выбрал студию квартиру!\n'
			'3) Отправь максимальную цену квартиры, валюта рубли\n'
			'Не правильно ввёл количество комнат, нажми ✏️ Редактровать\n'
			'Если хочешь отменить поиск, нажми Отмена',
			reply_markup=kb.edit_cancel)
		bot.register_next_step_handler(message, max_price_handler)


	else:
		bot.send_message(message.chat.id, 'Ты вводишь не правильное количество комнат 🙃\n'
			'Нужно начать сначала, нажми Главное меню',
			reply_markup=kb.main)

def max_price_handler(message):
	global max_price
	max_price = message.text
	if max_price == '❌ Отмена':
		bot.send_message(message.chat.id, 'Ты возвращён в Главное меню, для поиска объявлений по городу Челябинск, нажми соответствующую кнопку',
			reply_markup=kb.search)

	elif max_price == '✏️ Редактровать':
		bot.send_message(message.chat.id, 'Вижу, ты решил отредактировать количество комнат\n'
			'2) Пришли мне количество комнат (1-4) снова, если вариантов несколько, то напиши мне их слитно в порядке возрастания\n\n'
			'Пример: "Хочу только однокомнатную квартиру" — 1\n'
			'Пример: "Хочу однокомнатную, двухкомнатную квартиру" — 12\n'
			'Если хочешь отменить поиск, нажми Отмена',
			reply_markup=kb.cancel)
		bot.register_next_step_handler(message, room_handler)

	else:
		bot.send_message(message.chat.id, f'Ты указал максимальную цену — {max_price} руб.\n'
			'4) Отправь минимальную цену квартиры, валюта рубли\n'
			'Если минимальные рамки тебе не нужны, напиши 0\n'
			'Не правильно ввёл количество комнат, нажми ✏️ Редактровать\n'
			'Если хочешь отменить поиск, нажми Отмена',
			reply_markup=kb.edit_cancel)
		bot.register_next_step_handler(message, min_price_handler)


def min_price_handler(message):
	global min_price
	min_price = message.text
	if min_price == '❌ Отмена':
		bot.send_message(message.chat.id, 'Ты возвращён в Главное меню, для поиска объявлений по городу Челябинск, нажми соответствующую кнопку',
			reply_markup=kb.search)

	elif min_price == '✏️ Редактровать':
		bot.send_message(message.chat.id, 'Вижу, ты решил отредактировать максимальную цену!\n'
			'3) Отправь максимальную цену квартиры снова, валюта рубли\n'
			'Если хочешь отменить поиск, нажми Отмена',
			reply_markup=kb.cancel)
		bot.register_next_step_handler(message, max_price_handler)

	else:
		bot.send_message(message.chat.id, f'Ты указал минимальную цену — {min_price} руб.\n'
			'Не правильно ввёл минимальную цену, нажми ✏️ Редактровать\n'
			'Если хочешь отменить поиск, нажми Отмена\n'
			'Хочешь завершить, нажми Приготовить файл с объявлениями недвижимости',
			reply_markup=kb.done_edit_cancel)
		bot.register_next_step_handler(message, start_file_handler)

def start_file_handler(message):
	global start_file
	start_file = message.text
	if start_file == '❌ Отмена':
		bot.send_message(message.chat.id, 'Ты возвращён в Главное меню, для поиска объявлений по городу Челябинск, нажми соответствующую кнопку',
			reply_markup=kb.search)

	elif start_file == '✏️ Редактровать':
		bot.send_message(message.chat.id, 'Вижу, ты решил отредактировать минимальную цену!\n'
			'4) Отправь минимальную цену квартиры, валюта рубли\n'
			'Если минимальные рамки тебе не нужны, напиши 0\n'
			'Если хочешь отменить поиск, нажми Отмена',
			reply_markup=kb.cancel)
		bot.register_next_step_handler(message, min_price_handler)

	elif start_file == '📝 Приготовить файлы':
		n1_get = f'{url_n1}&price_max={max_price}&price_min={min_price}'
		avito_get = f'{url_avito}{district_avito}&pmax={max_price}&pmin={min_price}'
		cian_get = f'{url_cian}{district_cian}&maxprice={max_price}&minprice={min_price}'

		bot.send_message(message.chat.id, "Вот ссылки для парсинга:\n"
		f'N1: {n1_get}\n\n'
		f'AVITO: {avito_get}\n\n')
		f'CIAN: {cian_get}'
		
		n1_data(n1_get)
		time.sleep(5)


		avito_data(avito_get)
		time.sleep(5)

		cian_data(cian_get)
		time.sleep(5)

		try:
			n1 = open('/i/search_flat-master/n1.csv', 'rb')
			bot.send_document(message.chat.id, n1)
			time.sleep(3)
		except Exception:
			bot.send_message(message.chat.id, 'Что то пошло не так с сайтом N1')


		try:
			avito = open('/i/search_flat-master/avito.csv', 'rb')
			bot.send_document(message.chat.id, avito)
			time.sleep(3)
		except Exception:
			bot.send_message(message.chat.id, 'Что то пошло не так с сайтом AVITO')

		try:
			cian = open('/i/search_flat-master/cian.csv', 'rb')
			bot.send_document(message.chat.id, cian)
			time.sleep(3)
		except:
			bot.send_message(message.chat.id, 'Что то пошло не так с сайтом CIAN')


		bot.send_message(message.chat.id, "Извини, но следующее обращение по техническим причинам возможно, только через 5 минут",
			reply_markup=kb.main_fake)
		time.sleep(300)

		bot.send_message(message.chat.id, "Я снова доступен, переходи в Главное меню",
			reply_markup=kb.main)


if __name__ == '__main__':
	bot.polling(none_stop=True, interval=0)
