from telebot import TeleBot
from telebot.types import Message
from dotenv import load_dotenv
import os

load_dotenv('.env')
TG_TOKEN = os.getenv('TG_TOKEN')

bot = TeleBot(TG_TOKEN)


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message: Message) -> None:
    welcome_text = """
    Привет! Я бот для управления задачами. Вот так со мной работать:
    - Чтобы добавить задачу, отправьте в одном сообщении /add_task Название. Описание.
    - Чтобы посмотреть ваши задачи, отправьте /show_tasks
    - Чтобы посмотреть эту памятку снова, отправьте /help
    """

    user_id: int = message.chat.id
    bot.send_message(user_id, welcome_text)


    if __name__ == '__main__':
        bot.infinity_polling()
