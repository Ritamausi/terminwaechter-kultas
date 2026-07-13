import os

import time

import asyncio

import requests

from telegram import Bot

BOT_TOKEN = os.getenv("BOT_TOKEN")

CHAT_ID = os.getenv("CHAT_ID")

URL = os.getenv("URL")

bot = Bot(BOT_TOKEN)

async def check():

    try:

        response = requests.get(URL, timeout=20)

        text = response.text.lower()

        suchbegriffe = [

            "termin verfügbar",

            "verfügbar",

            "freie termine",

            "auswählen"

        ]

        for wort in suchbegriffe:

            if wort in text:

                await bot.send_message(

                    chat_id=CHAT_ID,

                    text="🚨 Möglicherweise ist ein Termin verfügbar!"

                )

                return

    except Exception as e:

        print(e)

while True:

    asyncio.run(check())

    time.sleep(120)
