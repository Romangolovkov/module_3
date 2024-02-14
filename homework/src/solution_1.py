from telebot import TeleBot
from telebot.types import Message
from dotenv import load_dotenv
import os

load_dotenv('.env')
TG_TOKEN = os.getenv('TG_TOKEN2')

bot = TeleBot(TG_TOKEN)

class Task:
    def __init__(self, date: str, name: str, description: str, tag: str) -> None:
        self.date = date
        self.name = name
        self.description = description
        self.tag = tag

    def __str__(self) -> str:
        return f'{self.date} - {self.name},{self.description} (тег:{self.tag})'


tasks: dict[int: list[Task]] = dict()


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message: Message) -> None:
    welcome_text = """
    Привет! Я бот для управления делами. Вот так со мной работать:
    - Чтобы добавить дело, отправьте в одном сообщении /add_task Дата. Название. Описание. Тег
    - Чтобы посмотреть ваш список дел, отправьте /show_tasks
    - Чтобы посмотреть эту памятку снова, отправьте /help
    """
    user_id: int = message.chat.id
    bot.send_message(user_id, welcome_text)


@bot.message_handler(commands=['add_task'])
def add_task(message: Message) -> None:
    user_id: int = message.chat.id

    text: str = message.text[9:].strip()
    

    if not text:
        bot.send_message(user_id, 'Вы не указали дело. Памятка - /help')
        return
    
    task_parts = text.split('.')

    if len(task_parts) != 4:
        bot.send_message(user_id, 'Вы неправильно указали дело. Памятка - /help')
        return
        
    task = Task(task_parts[0], task_parts[1], task_parts[2], task_parts[3])
    if not tasks.get(user_id):
        tasks[user_id] = [task]
    else:
        tasks[user_id].append(task)
    bot.send_message(user_id, 'Дело успешно добавлено в список дел')


@bot.message_handler(commands=['show_tasks'])
def show_tasks(message: Message) -> None:
    user_id: int = message.chat.id
    
    if not tasks.get(user_id):
        bot.send_message(user_id, 'Ваш список дел пуст')
        return
        
    text = "Ваш список дел:\n"
    for i, task in enumerate(tasks[user_id], start=1):
        text += f'{i}) {task.__str__()}\n'

    bot.send_message(user_id, text)


@bot.message_handler()
def text(message: Message) -> None:
    user_id: int = message.chat.id

    text: str = message.text.strip()
    if not (text.startswith('/add_task') or text.startswith('/show_tasks') or text.startswith('/help')):
        bot.send_message(user_id, 'Вы не указали команду, либо сделали это неправильно. Попробуйте ещё раз. Памятка - /help')


if __name__ == '__main__':
    bot.infinity_polling()