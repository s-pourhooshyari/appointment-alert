import requests
import os

BOT_TOKEN = os.environ.get("BOT_TOKEN")
CHAT_ID = os.environ.get("CHAT_ID")

URL = "https://reservationv5.frontdesksuite.com/us/us/ReserveTime/TimeSelection?pageId=0481fc5c-fd6f-4971-9213-1edbaae1660a&buttonId=3b944ef0-52fa-4b3c-99cd-3618b7693390&culture=da"

STATE_FILE = "state.txt"


def send_message(text):

    requests.get(
        f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
        params={
            "chat_id": CHAT_ID,
            "text": text
        },
        timeout=20
    )


def get_last_state():

    if not os.path.exists(STATE_FILE):
        return ""

    with open(STATE_FILE, "r") as f:
        return f.read()


def save_state(value):

    with open(STATE_FILE, "w") as f:
        f.write(value)


def check():

    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    response = requests.get(
        URL,
        headers=headers,
        timeout=30
    )

    html = response.text

    if "Ingen ledige tider" in html:
        current = "NO"

    else:
        current = "YES"

    previous = get_last_state()

    if current != previous:

        save_state(current)

        if current == "YES":
            send_message(
                f"🚨 Appointment may be available!\n\n{URL}"
            )

        else:
            send_message(
                "❌ No appointments available."
            )

    return current
