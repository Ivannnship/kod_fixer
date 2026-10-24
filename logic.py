import requests
import pyttsx3


def get_weather(city: str) -> str:
    url = f"https://wttr.in/{city}?format=%С+%t+%m+%w+%h"
    response = requests.get(url)
    if response.status_code == 200:
        return response.text.strip()
    else:
        return "Данных о погоде нет."


def speak(text: str):
    engine = pyttsx3.init()

    rate = engine.getProperty('rate')
    print(rate)
    engine.setProperty('rate', 100)

    volume = engine.getProperty('volume')
    print(volume)
    engine.setProperty('volume', 1.5)

    voices = engine.getProperty('voices')
    # print(voices)
    engine.setProperty('voice', voices[0].id)

    engine.say(text)
    engine.runAndWait()


if __name__ == "__main__":
    weather = get_weather("Москва")
    print(weather)
    speak(weather)
