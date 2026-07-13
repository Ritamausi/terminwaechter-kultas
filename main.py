import os
import time
import requests
from bs4 import BeautifulSoup
from telegram import Bot

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

URL ="https://scheduler.clinicore.eu/drkultas?showCards=true"

print("Bot startet...")

bot = Bot(token=BOT_TOKEN)

print("Bot wurde erstellt.")


def check():
    response = requests.get(URL, timeout=30)
    text = response.text.lower()

    suchbegriffe = [
        "termin verfügbar",
        "verfügbar",
        "freie termine",
        "auswählen"
    ]

    for wort in suchbegriffe:
        if wort in text:
            bot.send_message(
                chat_id=CHAT_ID,
                text="🚨 Es könnte ein freier Clinicore-Termin verfügbar sein!"
            )
            return True

    return False


while True:
    try:
        check()
    except Exception as e:
        print(e)

    time.sleep(120)
