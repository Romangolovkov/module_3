from telebot import TeleBot
from telebot.types import Message
from dotenv import load_dotenv
import os

load_dotenv('.env')
TG_TOKEN = os.getenv('TG_TOKEN2')

bot = TeleBot('6842615828:AAHHErih_PG-CrJGIUoiQUUGC4KR3K4VH7w')


class Client:
    def __init__(self, name: str, surname: str, date_birthday: str, id: int) -> None:
        self.name = name
        self.surname = surname
        self.date_birthday = date_birthday
        self.id = id
        self.products: list[Product] = []
    
    def __str__(self) -> str:
        text: str = f'Клиент {self.name} {self.surname}, д.р.:{self.date_birthday}, id карточки: {self.id}, покупки:\n'
        for product in self.products:
            text += product.__str__()
        return text


class Product:
    def __init__(self, price: str, name: str, date_buy: str) -> None:
        self.price = price
        self.name = name
        self.date_buy = date_buy

    def __str__(self) -> str:
        return f'  - {self.name}, цена: {self.price}, дата покупки {self.date_buy}\n'


database: dict[int: Client] = dict()


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message: Message) -> None:
    welcome_text: str = """
    Привет! Я бот для учета клиентов. Вот так со мной работать:
    - Чтобы добавить клиента, отправьте в одном сообщении /add_client Имя. Фамилию. Дату рождения. ID карточки
    - Чтобы удалить клиента, отправьте в одном сообщении /del_client ID карточки
    - Чтобы добавить товар, отправьте в одном сообщении /add_product ID карточки клиента. Цену. Название. Дату покупки
    - Чтобы посмотреть список клиентов, отправьте /show_clients
    - Чтобы посмотреть эту памятку снова, отправьте /help
    """
    user_id: int = message.chat.id
    bot.send_message(user_id, welcome_text)


@bot.message_handler(commands=['add_client'])
def add_client(message: Message) -> None:
    user_id: int = message.chat.id
    text: str = message.text[11:].strip()

    if not text:
        bot.send_message(user_id, 'Вы не указали данные клиента! Памятка - /help')
        return
    
    client_data = text.split('.')

    if len(client_data) != 4:
        bot.send_message(user_id, 'Вы неправильно указали данные клиента! Памятка - /help')
        return
    
    client = Client(client_data[0], client_data[1], client_data[2], int(client_data[3]))
    database[client.id] = client
    bot.send_message(user_id, 'Клиент успешно добавлен в базу!')


@bot.message_handler(commands=['del_client'])
def del_client(message: Message) -> None:
    user_id: int = message.chat.id
    text: str = message.text[11:].strip()
    id: int = int(text)

    if not id:
        bot.send_message(user_id, 'Вы не указали ID карточки клиента! Памятка - /help')
        return
    
    if id in database:
        del database[id]
        bot.send_message(user_id, 'Клиент успешно удалён!')
    else:
        bot.send_message(user_id, 'Клиент с таким ID карточки нет в базе!')


@bot.message_handler(commands=['add_product'])
def add_product(message: Message) -> None:
    user_id: int = message.chat.id
    text: str = message.text[12:].strip()
    if not text:
        bot.send_message(user_id, 'Вы не указали данные товара! Памятка - /help')
        return
    
    product_data = text.split('.')

    if len(product_data) != 4:
        bot.send_message(user_id, 'Вы неправильно указали данные товара! Памятка - /help')
        return
        
    product = Product(product_data[1], product_data[2], product_data[3])
    database[int(product_data[0])].products.append(product)
    bot.send_message(user_id, 'Товар успешно добавлен!')


@bot.message_handler(commands=['show_clients'])
def show_clients(message: Message) -> None:
    user_id: int = message.chat.id
    
    if not database:
        bot.send_message(user_id, 'Список клиентов пуст!')
        return

    text: str = "Список клиентов:\n"
    for i, client in enumerate(list(database.values()), start=1):
        text += f'{i}) {client.__str__()}\n'

    bot.send_message(user_id, text)
        
if __name__ == '__main__':
    bot.infinity_polling()