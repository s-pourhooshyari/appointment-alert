from flask import Flask
import requests
import os

app = Flask(__name__)

BOT_TOKEN = os.environ.get("BOT_TOKEN")
CHAT_ID = os.environ.get("CHAT_ID")

URL = "https://reservationv5.frontdesksuite.com/us/us/ReserveTime/TimeSelection?pageId=0481fc5c-fd6f-4971-9213-1edbaae1660a&buttonId=3b944ef0-52fa-4b3c-99cd-3618b7693390&culture=da"


def send_message(text):
    if BOT_TOKEN and CHAT_ID:
        requests.get(
            f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
            params={
                "chat_id": CHAT_ID,
                "text": text
            },
            timeout=20
        )


@app.route("/")
def check():

    try:
        headers = {
            "User-Agent": "Mozilla/5.0"
        }

        r = requests.get(URL, headers=headers, timeout=30)

        html = r.text

        if "Ingen ledige tider" in html:
            return "No appointments"

        send_message(
            "🚨 Appointment may be available!\n\n"
            + URL
        )

        return "Appointment found"

    except Exception as e:
        return str(e)


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 10000))
    )
