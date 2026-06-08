from flask import Flask
import requests
import os

app = Flask(__name__)

BOT_TOKEN = os.environ.get("BOT_TOKEN")
CHAT_ID = os.environ.get("CHAT_ID")

@app.route("/")
def home():
    if BOT_TOKEN and CHAT_ID:
        text = "✅ Appointment Alert Bot is running!"
        requests.get(
            f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
            params={
                "chat_id": CHAT_ID,
                "text": text
            },
            timeout=20
        )
    return "Bot is running!"
