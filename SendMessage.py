import os
import requests
import json
from VaultService import VaultService

openWeatherUrl = "https://api.openweathermap.org/data/2.5/weather?id={}&units=metric&appid={}"
weatherMessage = "🇵🇱{}\n 🌡Current T: {}°C\n 💌Highest T: {}\n 💌Lowest T: {}\n 💧{}"
telegramMessage = "https://api.telegram.org/bot{}/sendMessage"
cityId = 3094802

vaultService = VaultService(token=os.environ.get('VAULT_TOKEN'))
vaultChatId = vaultService.get_chat_id_secret()
vaultWeatherToken = vaultService.get_open_weather_api_key_secret()
vaultApiKey = vaultService.get_api_key_secret()


class SendMessage:
    print("Weather bot started...")

    def get_weather_message(self):
        response = requests.get(openWeatherUrl.format(cityId, vaultWeatherToken))
        if response.status_code == 200:
            print('OpenWeather: ok')
        else:
            print('OpenWeather: ' + response.text)
        data = json.loads(response.text)
        temp = round(data["main"]["temp"])
        temp_max = round(data["main"]["temp_max"])
        temp_min = round(data["main"]["temp_min"])
        weather = data["weather"][0]["description"].capitalize()
        message = weatherMessage.format(data['name'], temp, temp_max, temp_min, weather)
        return message

    def send_message(self):
        response = requests.get(telegramMessage.format(vaultApiKey), {
            'chat_id': vaultChatId,
            'text': self.get_weather_message()
        })
        if response.status_code == 200:
            print('Telegram: ok')
        else:
            print('Telegram: ' + response.text)

