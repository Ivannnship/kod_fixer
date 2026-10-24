import telebot
# from config import token
from logic import get_weather, speak

bot = telebot.TeleBot("8511906268:AAFe6N_VxXO7AnNE6i44ueuKt7lg15EZPSs")


@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(message.chat.id, "Привет, я бот, который поможет узнавать"
                                      "тебе погоду.")

    # /weather Москва -> ["/weather", "Москва"]
    @bot.message_handler(commands=["weather"])
    def weather(message):
        parts = message.text.split(maxsplit=1)
        if len(parts) < 2:
            bot.send_message(message.chat.id, "Укажите город после"
                                              "команды /weather")
            return
        else:
            city = parts[1]
            weather_info = get_weather(city)
            bot.send_message(message.chat.id, weather_info)
            speak(weather_info)


bot.polling()
