import telebot
from telebot.types import Message
from decouple import config

from calculator import calculate


# Password and token are in .env file
token: str = config('token', default='')
password: str = config('password', default='')

bot: telebot.TeleBot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def request_password(message: Message) -> None:
    """Asks for a password"""

    bot.send_message(message.chat.id, 'Please enter password')
    bot.register_next_step_handler(message, check_password)


def check_password(message: Message) -> None:
    """Verifies the correctness of the password"""
    if message.text == password:
        send_start_message(message)
    else:
        request_password(message)


def send_start_message(message: Message) -> None:
    """Send start message to user"""

    chat_id: int = message.chat.id
    bot.send_message(chat_id, "Hello, I'm a calculator bot. I will be able to calculate equations with 2 "
                              "and 3 operators. Example:\n2+2\n2*9\n2*6/8\n100-2*10+39")
    bot.register_next_step_handler(message, send_result_message)


def send_result_message(message: Message) -> None:
    """Send result to user"""

    result: str = calculate(message.text)
    bot.send_message(message.chat.id, result)
    bot.register_next_step_handler(message, send_result_message)


if __name__ == '__main__':
    bot.infinity_polling()


