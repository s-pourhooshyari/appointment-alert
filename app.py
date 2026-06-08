from flask import Flask
from apscheduler.schedulers.background import BackgroundScheduler

from checker import check

app = Flask(__name__)

scheduler = BackgroundScheduler()


scheduler.add_job(
    func=check,
    trigger="interval",
    minutes=5
)

scheduler.start()


@app.route("/")
def home():

    return "Appointment Alert Running"


@app.route("/check")
def manual():

    return check()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
